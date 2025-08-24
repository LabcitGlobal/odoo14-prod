odoo.define('lc_product_variant_pos.product', function (require) {
    "use strict";
    
    const models = require('point_of_sale.models');

    models.load_fields('product.product',['product_pos_enabled']);

});