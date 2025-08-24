odoo.define("point_of_sale.QuotationListScreenWidget", function (require) {
    "use strict";

    const { debounce } = owl.utils;
    const PosComponent = require("point_of_sale.PosComponent");
    const Registries = require("point_of_sale.Registries");
    const { useListener } = require("web.custom_hooks");

    class QuotationListScreenWidget extends PosComponent {
        constructor() {
            super(...arguments);
            useListener("click-save", () => this.LoadTemplate());
            this.state = {
                query: null,
                selectedQuotation: this.props.quotation,
            };

            this.updateTemplateList = debounce(this.updateTemplateList, 70);
        }
        get_all_product_quotations() {
            return this.env.pos.sale_quotations;
        }

        get_quotation_by_customer_name(name) {
            var quotations = this.get_all_product_quotations();
            return _.filter(quotations, function (quotation) {
                if (quotation && quotation.partner_id) {
                    if (quotation.partner_id[(0, 1)].toLowerCase().indexOf(name) > -1) {
                        return true;
                    } else {
                        return false;
                    }
                }
            });
        }
        get_quotation_by_id(id) {
            var params = {
                model: "sale.order",
                method: "search_read",
                domain: [["id", "=", id]],
            };
            rpc.query(params, { async: false }).then(function (quotation) {
                return template.id === quotation;
            });
        }

        updateTemplateList(event) {
            this.state.query = event.target.value;
            const quotationlistcontents = this.quotationlistcontents;
            if (event.code === "Enter" && quotationlistcontents.length === 1) {
                this.state.selectedQuotation = quotationlistcontents[0];
            } else {
                this.render();
            }
        }
        get_quotation_by_name(name) {
            var quotations = this.get_all_product_quotations();
            return _.filter(quotations, function (quotation) {
                if (quotation["name"]) {
                    if (quotation["name"].indexOf(name) > -1) {
                        return true;
                    } else {
                        return false;
                    }
                }
            });
        }

        get quotationlistcontents() {
            if (this.state.query && this.state.query.trim() !== "") {
                var quotations = this.get_quotation_by_name(this.state.query.trim());
                if (quotations.length > 0) {
                    return quotations;
                } else {
                    var quotations = this.get_quotation_by_customer_name(this.state.query.trim());
                    return quotations;
                }
            } else {
                var quotations = this.get_all_product_quotations();
                return quotations;
            }
        }
        back() {
            this.props.resolve({ confirmed: false, payload: false });
            this.trigger("close-temp-screen");
        }

        // Getters

        get currentOrder() {
            return this.env.pos.get_order();
        }

        async LoadTemplate(event) {
            var self = this;
            if (this.state.selectedQuotation) {
                var order = this.currentOrder;

                var selectedTemplateId = this.state.selectedQuotation["id"];
                console.log(selectedTemplateId, this.env.pos.quotation_by_id);
                if (selectedTemplateId) {
                    var selectedTemplate = this.env.pos.quotation_by_id[selectedTemplateId];
                    order.sale_order_id = selectedTemplateId;
                    order.sale_order_name = selectedTemplate.name;
                    if (selectedTemplate["partner_id"]) {
                        const partner = self.env.pos.db.get_partner_by_id(selectedTemplate["partner_id"][0]);
                        order.set_client(partner);
                    }
                }

                var template_lines = this.env.pos.line_by_id[selectedTemplateId];

                if (template_lines.length) {
                    _.each(template_lines, function (line) {
                        var product_id = line.product_id.length ? line.product_id[0] : false;
                        if (product_id) {
                            var product = self.env.pos.db.get_product_by_id(product_id);
                            if (product) {
                                order.add_product(product, {
                                    quantity: line.product_uom_qty,
                                    price: line.price_unit,
                                    discount: line.discount,
                                });
                            }
                        }
                    });
                }
                this.trigger("close-temp-screen");
            } else {
                alert("Please select Quotation !");
            }
        }
        clickLine(event) {
            let quotation = event.detail.quotation;
            if (this.state.selectedQuotation === quotation) {
                this.state.selectedQuotation = null;
            } else {
                this.state.selectedQuotation = quotation;
            }
            this.render();
        }
    }
    QuotationListScreenWidget.template = "QuotationListScreenWidget";

    Registries.Component.add(QuotationListScreenWidget);

    return QuotationListScreenWidget;
});
