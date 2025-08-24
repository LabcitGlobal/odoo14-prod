odoo.define("point_of_sale.QuotationLine", function (require) {
    "use strict";

    const PosComponent = require("point_of_sale.PosComponent");
    const Registries = require("point_of_sale.Registries");

    class QuotationLine extends PosComponent {
        get highlight() {
            return this.props.quotation !== this.props.selectedQuotation ? "" : "highlight";
        }
        getDate(quotation) {
            return moment(quotation.date_order).format("DD/MM/Y");
        }
    }
    QuotationLine.quotation = "QuotationLine";

    Registries.Component.add(QuotationLine);

    return QuotationLine;
});
