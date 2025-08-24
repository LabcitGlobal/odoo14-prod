odoo.define('lc_group_export_import.remove_actions', function (require) {
    "use strict";
    
    var core = require('web.core');
    var KanbanController = require("web.KanbanController");
    var ListController = require("web.ListController");
    var PivotController = require('web.PivotController');
    var _t = core._t;


    ListController.include({
        updateButtons: function (mode) {
            var self = this;
            this._super.apply(this, arguments);
            var session = this.getSession();
            if (!this.$buttons) {
                return;
            }
            if (session) {
                this.$buttons.find('.o_list_export_xlsx').hide();
                session.user_has_group('lc_group_export_import.group_export').then(function(has_group) {
                    if (has_group) {
                        self.$buttons.find('.o_list_export_xlsx').show();
                    }
                });
            }
        },
        _getActionMenuItems: function (state) {
            const props = this._super(...arguments);
            var export_label = _t("Export");
            var session = this.getSession();
            if (props && session){
                session.user_has_group('lc_group_export_import.group_export').then(function(has_group) {
                    if (!has_group) {
                        props.items['other'] = $.grep(props.items['other'], function(i){
                            return i && i.description && i.description != export_label;
                        });
                    }
                });
            }
            return props
        }
    });

    PivotController.include({
        renderButtons: function ($node) {
            var self = this;
            this._super.apply(this, arguments);
            var session = this.getSession();
            if (session) {
                session.user_has_group('lc_group_export_import.group_export').then(function(has_group) {
                    if (self.$buttons && !has_group) {
                        self.$buttons.find('button.o_pivot_download').hide();
                    }
                });
            }
        }
    });
    
    
});
