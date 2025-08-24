odoo.define('aces_pos_note.aspl_product_note', function (require) {
    "use strict";

    var models = require('point_of_sale.models');

    var _super_order = models.Order.prototype;
    models.Order = models.Order.extend({
        initialize: function() {
            _super_order.initialize.apply(this,arguments);
            this.order_note = this.order_note || false;
            this.save_to_db();
        },
        export_as_JSON: function() {
            var submitted_order = _super_order.export_as_JSON.call(this);
            var new_val = {
                order_note: this.get_order_note(),
            }
            $.extend(submitted_order, new_val);
            return submitted_order;
        },
        export_for_printing: function() {
          var result = _super_order.export_for_printing.apply(this,arguments);
          result.order_note = this.get_order_note();
          return result;
        },
        set_order_note: function(order_note) {
            this.order_note = order_note;
        },
        get_order_note: function() {
            return this.order_note;
        },
    });

    var _super_orderline = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
        initialize: function(attr, options) {
            _super_orderline.initialize.call(this,attr,options);
            this.line_note = this.line_note || "";
        },
        set_product_note: function(line_note){
            this.line_note = line_note;
            this.trigger('change',this);
        },
        get_product_note: function(){
            return this.line_note;
        },
        can_be_merged_with: function(orderline) {
            if (orderline.get_product_note() !== this.get_product_note()) {
                return false;
            } else {
                return _super_orderline.can_be_merged_with.apply(this,arguments);
            }
        },
        clone: function(){
            var orderline = _super_orderline.clone.call(this);
            orderline.line_note = this.line_note;
            return orderline;
        },
        export_as_JSON: function(){
            var json = _super_orderline.export_as_JSON.call(this);
            json.line_note = this.line_note;
            return json;
        },
        init_from_JSON: function(json){
            _super_orderline.init_from_JSON.apply(this,arguments);
            this.line_note = json.line_note;
        },
        export_for_printing: function() {
            var line = _super_orderline.export_for_printing.apply(this,arguments);
            line.line_note = this.get_product_note();
            return line;
        },
    });

});
