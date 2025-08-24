odoo.define('lc_pricelist_group.models', function (require) {
    'use strict';

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

    models.load_fields('product.product',['product_template_price_group']);

    class PricelistGroupPopup extends AbstractAwaitablePopup {        
        constructor() {            
            super(...arguments);
            useSubEnv({ attribute_components: [] });             
        }
        click_on_confirm() {
            var self = this.props;            
            var order = this.env.pos.get_order();            
            var products = _.map(order.get_orderlines(), function (line) {
                if(line.product.product_tmpl_id == self.product.product_tmpl_id)
                    line.set_unit_price(self.product.fixed_price);
            });
            this.trigger('close-popup');
        }
    }
    PricelistGroupPopup.template = "PricelistGroupPopup";

    Registries.Component.add(PricelistGroupPopup);
        
    function product_count(product, order) {        
        var update = false;
        var fixed_price = product.lst_price;
        var min_quantity = 0;
        var product_tmpl_total = 0;
        var orderlines = _.filter(order.get_orderlines(), function (line) {
            if(product.product_tmpl_id == line.product.product_tmpl_id)
                product_tmpl_total += line.quantity;
            return product.product_tmpl_id == line.product.product_tmpl_id;
        });
        var pricelist = _.filter(order.pricelist.items, function(line) {
            return line.product_tmpl_id[0] == product.product_tmpl_id;
        });
        var aux=0;
        _.each(pricelist, function(line) {
            if(product_tmpl_total >= line.min_quantity) {
                if(line.min_quantity > aux) {
                    fixed_price = line.fixed_price;
                    min_quantity = line.min_quantity;
                }
                aux = line.min_quantity;
            }
        });        
        var error = _.find(orderlines, function(line){
            return line.price != fixed_price;
        });        
        if(error) update=true;
        var result = {
            'update': update,
            'product_tmpl_id': product.product_tmpl_id,
            'product_tmpl_name': product.display_name.substr(0,product.display_name.indexOf("(")-1),
            'product_tmpl_total': product_tmpl_total,
            'pricelist_name': order.pricelist.display_name,
            'fixed_price': fixed_price,
            'min_quantity': min_quantity,
            'pricelist': pricelist
        }
        return result;
    }

    const PosPricelistGroup = (ProductScreen) =>
        class extends ProductScreen {
            constructor() {
                super(...arguments);
                useListener("click-product", this.on_click_product);
                useListener("update-selected-orderline", this.on_set_value);
            }            
            
            on_click_product(event) {

                const product = event.detail;

                if(this.env.pos.config.pricelist_group && product.product_template_price_group) {
                    const order = this.env.pos.get_order();                    
                    var validate = product_count(product,order);                    
                    if(validate.update) {
                        let { confirmed, payload } = this.showPopup("PricelistGroupPopup", {
                            product: validate,                            
                        });
        
                        if (confirmed) {                            
                        } else {
                            return;
                        }
                    }
                }
               
            }

            on_set_value(event) {
                const order = this.env.pos.get_order();                                
                if(order.get_selected_orderline()){
                    var orderline = order.get_selected_orderline();
                    if(this.env.pos.config.pricelist_group && orderline.product.product_template_price_group) {
                        var validate = product_count(orderline.product,order);
                        if(validate.update) {
                            let { confirmed, payload } = this.showPopup("PricelistGroupPopup", {
                                product: validate,                            
                            });
            
                            if (confirmed) {                            
                            } else {
                                return;
                            }
                        }
                    }
                }
            }

        };

    Registries.Component.extend(ProductScreen, PosPricelistGroup);

    return {
        PricelistGroupPopup,
        ProductScreen,
    };

});