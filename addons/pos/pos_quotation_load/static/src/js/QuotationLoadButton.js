odoo.define("pos_quotation_load.LoadQuotationButton", function (require) {
    "use strict";

    const PosComponent = require("point_of_sale.PosComponent");
    const ProductScreen = require("point_of_sale.ProductScreen");
    const { useListener } = require("web.custom_hooks");
    const Registries = require("point_of_sale.Registries");
    const Chrome = require("point_of_sale.Chrome");
    const { Gui } = require("point_of_sale.Gui");

    class LoadQuotationButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener("click-quotation-load-icon", this.onClickTemplateLoad);
        }
        get_quotation() {
            if (this.env.pos.get_order()) {
                return this.env.pos.get_order().sale_order_name || "Cargar Cotizacion";
            } else {
                return "Cargar Cotizacion";
            }
        }

        onClickTemplateLoad() {
            const { confirmed, payload } = this.showTempScreen("QuotationListScreenWidget");
            if (confirmed) {
            }
        }
    }
    LoadQuotationButton.template = "LoadQuotationButton";

    ProductScreen.addControlButton({
        component: LoadQuotationButton,
        condition: function () {
            return this.env.pos.config.sh_enable_quotation_load;
        },
    });

    Registries.Component.add(LoadQuotationButton);

    return LoadQuotationButton;
});
