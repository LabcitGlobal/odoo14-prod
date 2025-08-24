/*
    @Author: KSOLVES India Private Limited
    @Email: sales@ksolves.com
*/

odoo.define('lc_product_variant_pos.lc_product_variant_pos', function (require) {
    "use strict";
    const LcProductItem = require('point_of_sale.ProductItem');
    const Registries = require('point_of_sale.Registries');

    console.log('Overlay');

    const lc_product_variant_pos = (LcProductItem) =>
        class extends LcProductItem {
            addOverlay (){

               var task;
               clearInterval(task);
               task = setTimeout(function () {
                   $(".overlay").parent().addClass('pointer-none');
               }, 100);
            }
        };

    Registries.Component.extend(LcProductItem,lc_product_variant_pos);
    return LcProductItem;
})