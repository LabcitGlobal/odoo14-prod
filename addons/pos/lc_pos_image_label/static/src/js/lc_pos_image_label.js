odoo.define('lc_pos_image_label.product', function (require) {
    "use strict";
    
    const models = require('point_of_sale.models');

    models.load_fields('product.product',['label1','label2','top']);

});