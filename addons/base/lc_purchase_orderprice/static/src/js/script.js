odoo.define('lc_purchase_orderprice.change_color', function (require) {
    "use strict";

    var FormView = require('web.FormView');
    var core = require('web.core');

    FormView.include({
        render: function () {
            this._super.apply(this, arguments);
            this._updateLastCostColor();
            this._bindEvents();
        },

        _bindEvents: function () {
            var self = this;
            this.$('input[name="is_different_cost"]').on('change', function () {
                self._updateLastCostColor();
            });
        },

        _updateLastCostColor: function () {
            var self = this;
            this.$('.last-cost-field').each(function () {
                var $field = $(this);
                var isDifferentCost = $field.closest('tr').find('input[name="is_different_cost"]').is(':checked');

                if (isDifferentCost) {
                    $field.addClass('different-cost');
                } else {
                    $field.removeClass('different-cost');
                }
            });
        },
    });
});