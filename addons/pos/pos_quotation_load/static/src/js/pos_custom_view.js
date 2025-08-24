odoo.define("pos_quotation_load.pos", function (require) {
    var task;
    var models = require("point_of_sale.models");
    var _super_posmodel = models.PosModel.prototype;
    var rpc = require("web.rpc");
    var core = require("web.core");
    var QWeb = core.qweb;
    var _t = core._t;

    models.load_fields("pos.order", ["sale_order_id", "sale_order_name"]);

    models.load_models([
        {
            model: "sale.order",
            domain: [["state", "in", ["draft", "sent"]]],
            loaded: function (self, sale_quotations) {
                self.sale_quotations = [];
                self.quotation_by_id = {};

                if (sale_quotations.length) {
                    self.sale_quotations = sale_quotations;
                }
                _.each(sale_quotations, function (quotation) {
                    self.quotation_by_id[quotation["id"]] = quotation;
                });
            },
        },
    ]);
    models.load_models({
        model: "sale.order.line",
        fields: ["name", "product_id", "product_uom_qty", "price_unit", "discount", "product_uom", "price_subtotal", "order_id", "tax_id"],
        domain: function (self) {
            return [];
        },
        loaded: function (self, order_lines) {
            self.order_lines = order_lines;
            self.line_by_id = {};
            var data_list = [];

            _.each(order_lines, function (line) {
                if (line.order_id[0] in self.line_by_id) {
                    var temp_list = self.line_by_id[line.order_id[0]];
                    temp_list.push(line);
                    self.line_by_id[line.order_id[0]] = temp_list;
                } else {
                    data_list = [];
                    data_list.push(line);
                    self.line_by_id[line.order_id[0]] = data_list;
                }
            });
        },
    });

    var _super_order = models.Order.prototype;
    models.Order = models.Order.extend({
        export_as_JSON: function () {
            var data = _super_order.export_as_JSON.apply(this, arguments);
            data.sale_order_id = this.sale_order_id;
            data.sale_order_name = this.sale_order_name;
            return data;
        },
        init_from_JSON: function (json) {
            this.sale_order_id = json.sale_order_id;
            this.sale_order_name = json.sale_order_name;
            _super_order.init_from_JSON.call(this, json);
        },
        get_quotation: function () {
            return this.sale_order_name;
        },
        set_quotation: function (sale_order_name) {
            this.sale_order_name = sale_order_name;
            this.trigger("change");
        },
    });
});
