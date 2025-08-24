odoo.define('lc_pos_disable_options.buttons', function (require) {
    "use strict";
    
    const models = require('point_of_sale.models');
    // const components = {
    //     NumpadWidget: require('point_of_sale.NumpadWidget'),
    // };
    // const { patch } = require('web.utils');

    models.load_fields('pos.config',['disable_discount', 'disable_price', 'disable_payment']);

    // patch(components.NumpadWidget, 'disabled-buttons', {
    //     mounted() {
    //         if(this.env.pos.config.disable_quantity) {
    //             $($('.numpad').find('.mode-button')[0]).toggleClass('enabled-mode').prop('enabled');
    //         } else {
    //             $($('.numpad').find('.mode-button')[0]).toggleClass('disabled-mode').prop('disabled');
    //         }
    //         if(this.env.pos.config.disable_discount) {
    //             $($('.numpad').find('.mode-button')[1]).toggleClass('enabled-mode').prop('enabled');
    //         } else {
    //             $($('.numpad').find('.mode-button')[1]).toggleClass('disabled-mode').prop('disabled');
    //         }
    //         if(this.env.pos.config.disable_price) {
    //             $($('.numpad').find('.mode-button')[2]).toggleClass('enabled-mode').prop('enabled');
    //         } else {
    //             $($('.numpad').find('.mode-button')[2]).toggleClass('disabled-mode').prop('disabled');
    //         }           
    //     }

    // });

});