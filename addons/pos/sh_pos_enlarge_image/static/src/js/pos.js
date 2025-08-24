odoo.define("sh_pos_enlarge_image.screens", function (require) {
    "use strict";

    var models = require("point_of_sale.models");
    var core = require("web.core");
    var DB = require("point_of_sale.DB");

    const ProductScreen = require("point_of_sale.ProductScreen");
    const Registries = require("point_of_sale.Registries");
    const { useBarcodeReader } = require("point_of_sale.custom_hooks");
    const { useListener } = require("web.custom_hooks");
    const { useState, useSubEnv } = owl.hooks;
    const PosComponent = require("point_of_sale.PosComponent");
    const AbstractAwaitablePopup = require("point_of_sale.AbstractAwaitablePopup");
    var QWeb = core.qweb;
    var _t = core._t;

    class ProductEnlargePopup extends AbstractAwaitablePopup {
        constructor() {
            super(...arguments);
            useSubEnv({ attribute_components: [] });
        }
    }
    ProductEnlargePopup.template = "ProductEnlargePopup";

    Registries.Component.add(ProductEnlargePopup);

    const EnlargeProductScreen = (ProductScreen) =>
        class extends ProductScreen {
            constructor() {
                super(...arguments);
                useListener("click-product-enlarge-icon", this.on_click_enlarge_icon);
            }
            get_enlarge_product_image_url(product_id) {
                return window.location.origin + "/web/image?model=product.product&field=image_128&id=" + product_id;
            }
            async on_click_enlarge_icon(event) {
                const product = event.detail;                
                // const categ_id = product.categ_id[0];
                
                // Pricelist type Compute
                let categ_array = [];
                categ_array.push(product.categ.id);
                let aux = product.categ.parent;
                let sw = false;                
                while(sw == false) {
                    if(aux){
                        categ_array.push(aux.id);
                        aux = aux.parent;
                    } else
                        sw = true;
                }                
                
                const lst_price = product.lst_price;
                var self = this;
                let title = product.display_name;
                var image_url = this.get_enlarge_product_image_url(product.id);
                let desc_sale = product.description_sale;
                const description = product.description;
                var stock_quant = [];

                // Stock Multicompany
                if(self.env.pos.config.sh_enable_stock_multicompany) {
                    var partner_id = self.env.pos.get_client();
					await this.rpc({
						model: 'stock.quant',
						method: 'get_single_product_company',
						args: [0,product.id],
					}).then(function(output) {
                        stock_quant = output;
					});
                }

                //  Order Pricelist ID
                const pricelist_id = product.pos.attributes.selectedOrder.pricelist.id;
                const pricelist = _.filter(product.pos.pricelists, function(line) {
                    return line.id == pricelist_id;
                });
                let product_pricelist = [];
                if(pricelist[0].items[0].compute_price == 'formula'){
                    let product_categlist = [];
                    for(var i=0; i<=categ_array.length-1; i++){
                        product_categlist = _.filter(pricelist[0].items, function(line) {                            
                            return line.categ_id[0] == categ_array[i];
                        });
                        if (product_categlist.length > 0) break;
                    }                    
                    _.each(product_categlist, function(line) {
                        const fixed_price = lst_price - (lst_price * (line.price_discount/100));
                        const object = {
                            'min_quantity': line.min_quantity,
                            'fixed_price': fixed_price.toFixed(0)
                        };
                        product_pricelist.push(object);
                    });
                } else {
                    product_pricelist = _.filter(pricelist[0].items, function(line) {
                        return line.product_tmpl_id[0] == product.product_tmpl_id;
                    });
                }

                let { confirmed, payload } = await this.showPopup("ProductEnlargePopup", {
                    title: title,
                    desc_sale: desc_sale,
                    image_url: image_url,
                    pricelist: product_pricelist,
                    description: description,
                    stock_quant: stock_quant
                });

                if (confirmed) {
                } else {
                    return;
                }
            }
        };

    Registries.Component.extend(ProductScreen, EnlargeProductScreen);

    return {
        ProductEnlargePopup,
        ProductScreen,
    };
});
