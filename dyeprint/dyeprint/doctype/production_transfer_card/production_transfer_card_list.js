frappe.listview_settings["Production Transfer Card"] = {
	onload(listview) {
		clear_transfer_card_details(listview);
		add_transfer_card_detail_styles();
		bind_transfer_card_row_toggle(listview);
	},
	before_render() {
		clear_transfer_card_details();
	},
	refresh(listview) {
		bind_transfer_card_row_toggle(listview);
	},
};

const TRANSFER_CARD_DETAIL_TABLES = [
	{
		fieldname: "胚布名称",
		label: "胚布名称",
		columns: ["批次号", "坯布代码", "坯布名称", "坯布规格", "库存匹数"],
	},
	{
		fieldname: "生产工序",
		label: "生产工序",
		columns: ["分工序代码", "分工序名称", "工序顺序号"],
	},
	{
		fieldname: "加工要求",
		label: "加工要求",
		columns: ["项目名称", "项目几级"],
	},
	{
		fieldname: "包装要求",
		label: "包装要求",
		columns: ["要求名称", "要求几级"],
	},
];

function clear_transfer_card_details(listview) {
	const root = listview
		? (listview["\x24result"] && listview["\x24result"][0]) || listview.page.main.querySelector(".result")
		: document;

	if (!root) {
		return;
	}

	root.querySelectorAll(".production-transfer-card-details").forEach((detail) => detail.remove());
}

function bind_transfer_card_row_toggle(listview) {
	const result = (listview.$result || $(listview.page.main).find(".result"))[0];

	if (!result || result.__production_transfer_card_detail_bound) {
		return;
	}

	result.__production_transfer_card_detail_bound = true;
	result.addEventListener(
		"click",
		(event) => {
			const row = event.target.closest(".list-row");

			if (!row || !result.contains(row) || should_ignore_transfer_card_click(event)) {
				return;
			}

			event.preventDefault();
			event.stopPropagation();
			event.stopImmediatePropagation();

			toggle_transfer_card_details(listview, $(row).closest(".list-row-container"));
		},
		true
	);
}

function should_ignore_transfer_card_click(event) {
	return Boolean(
		$(event.target).closest(
			[
				".list-row-head",
				".list-row-checkbox",
				".level-left .checkbox",
				".actions",
				".btn",
				".dropdown",
				".dropdown-menu",
				"a",
				"input",
				"select",
				"textarea",
			].join(", ")
		).length
	);
}

async function toggle_transfer_card_details(listview, $row_container) {
	const docname = get_transfer_card_docname(listview, $row_container);

	if (!docname) {
		return;
	}

	const $existing = $row_container.next(".production-transfer-card-details");

	if ($existing.length) {
		$existing.slideToggle(120);
		return;
	}

	const $details = $(`
		<div class="production-transfer-card-details">
			<div class="production-transfer-card-loading">${__("Loading")}...</div>
		</div>
	`);

	$row_container.after($details);

	try {
		const doc = await frappe.db.get_doc("Production Transfer Card", docname);
		$details.html(render_transfer_card_details(doc));
	} catch (error) {
		console.error(error);
		$details.html(
			`<div class="production-transfer-card-error">${__("Unable to load details")}</div>`
		);
	}
}

function get_transfer_card_docname(listview, $row_container) {
	const direct_name = $row_container.attr("data-name");

	if (direct_name) {
		return direct_name;
	}

	const child_name = $row_container.find("[data-name]").first().attr("data-name");

	if (child_name) {
		return child_name;
	}

	const row_index = $row_container.find("[data-idx]").first().attr("data-idx");
	const row = Number.isInteger(Number(row_index)) ? listview.data[Number(row_index)] : null;

	return row && row.name;
}

function render_transfer_card_details(doc) {
	const sections = TRANSFER_CARD_DETAIL_TABLES.map((table) =>
		render_transfer_card_table(table, doc[table.fieldname] || [])
	).join("");

	return `<div class="production-transfer-card-grid">${sections}</div>`;
}

function render_transfer_card_table(table, rows) {
	const header = table.columns
		.map((column) => `<th>${frappe.utils.escape_html(column)}</th>`)
		.join("");

	const body = rows.length
		? rows
				.map((row) => {
					const cells = table.columns
						.map((column) => {
							const value = row[column] || "";
							return `<td>${frappe.utils.escape_html(value)}</td>`;
						})
						.join("");

					return `<tr>${cells}</tr>`;
				})
				.join("")
		: `<tr><td colspan="${table.columns.length}" class="text-muted">${__("No Data")}</td></tr>`;

	return `
		<section class="production-transfer-card-section${table.fieldname === "胚布名称" ? " production-transfer-card-section-wide" : ""}">
			<div class="production-transfer-card-title">${frappe.utils.escape_html(table.label)}</div>
			<div class="production-transfer-card-table-wrapper">
				<table class="table table-bordered table-condensed">
					<thead><tr>${header}</tr></thead>
					<tbody>${body}</tbody>
				</table>
			</div>
		</section>
	`;
}

function add_transfer_card_detail_styles() {
	if (document.getElementById("production-transfer-card-detail-styles")) {
		return;
	}

	frappe.dom.set_style(`
		.production-transfer-card-details {
			background: var(--bg-light-gray);
			border: 1px solid var(--border-color);
			border-top: 0;
			padding: 12px 14px;
			box-sizing: border-box;
			width: calc(100% - 120px);
			margin-left: 60px;
			margin-right: 60px;
			margin-bottom: 60px;
		}

		.production-transfer-card-grid {
			display: grid;
			grid-template-columns: repeat(3, minmax(220px, 1fr));
			gap: 12px;
		}

		.production-transfer-card-section {
			min-width: 0;
		}

		.production-transfer-card-section-wide {
			grid-column: 1 / -1;
		}
		@media (max-width: 991px) {
			.production-transfer-card-grid {
				grid-template-columns: 1fr;
			}

			.production-transfer-card-details {
				width: 100%;
				margin-left: 0;
				margin-right: 0;
			}
		}

		.production-transfer-card-title {
			background: var(--subtle-fg);
			border: 1px solid var(--border-color);
			border-bottom: 0;
			color: var(--text-color);
			font-weight: 600;
			margin-bottom: 0;
			padding: 7px 9px;
		}

		.production-transfer-card-table-wrapper {
			overflow-x: auto;
			max-width: 100%;
		}

		.production-transfer-card-section-wide .production-transfer-card-table-wrapper {
			width: 100%;
			overflow-x: auto;
			overflow-y: hidden;
		}

		.production-transfer-card-details table {
			background: var(--fg-color);
			margin: 0;
			table-layout: auto;
			white-space: nowrap;
		}

		.production-transfer-card-details th,
		.production-transfer-card-details td {
			font-size: 12px;
			padding: 6px 8px;
			vertical-align: top;
		}

		.production-transfer-card-loading,
		.production-transfer-card-error {
			color: var(--text-muted);
			padding: 4px 0;
		}
	`, "production-transfer-card-detail-styles");
}
