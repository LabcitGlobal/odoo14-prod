/*  ---------------------------------------------------
    Template Name: Labcit Services
    Description: Labcit HTML template
    Author: Labcit
    Author URI: https://labcit.com/
    Version: 1.0
    Created: Labcit
---------------------------------------------------------  */

// odoo.define("tuexpres_frontend.product_pricelist", function (require) {
//     "use strict";
    
//     var publicWidget = require("web.public.widget");
//     publicWidget.registry.ProductPricelist = publicWidget.Widget.extend({
//       selector: ".pricelist",
//       events: {
//         "click": "_onClick",
//       },

//       _onClick: async function (ev,pr) {
//         var tx_qty = $('#tx_product_pricelist').find('.pricelist').attr('data-qty');
//         var tx_price = $('#tx_product_pricelist').find('.pricelist').attr('data-price');
//         console.log(tx_qty+" "+tx_price);
//       },

//     });
//   });


  function tx_pricelist(a){    
    $("input[name*='add_qty']").val(a);  
  }