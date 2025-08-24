odoo.define('sh_pos_hide_show_numpad.pos', function (require, factory) {
    'use strict';

    const NumpadWidget = require("point_of_sale.NumpadWidget");
    const Registries = require("point_of_sale.Registries");

    const InheritNumpadWidget = (NumpadWidget) =>
        class extends NumpadWidget {
            mounted() {
                var self = this;
                super.mounted();
                if(this.env.pos.config.enable_numpad){
                    $('.sh-numpad-viewer').on('click', function () {
                        var self = this;
                        $(this).parent().siblings('.sh-numpad-data').slideToggle(function () {
                            $(self).toggleClass('fa-angle-double-down fa-angle-double-up');
                            if ($(this).is(':visible')) {
                                $('.order-scroller').animate({ scrollTop: $('.order-scroller').height() }, 500);
                                $('.sh_tgle_btn').removeClass("sh_down_tgl_btn")
                            } else {
                                $('.sh_tgle_btn').addClass("sh_down_tgl_btn")
                            }
                        });
                    });
                }
            }
        }

    Registries.Component.extend(NumpadWidget, InheritNumpadWidget);

});
