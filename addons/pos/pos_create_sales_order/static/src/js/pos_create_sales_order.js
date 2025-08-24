odoo.define('pos_create_sales_order.CreateSalesOrderButtonWidget', function(require) {
	"use strict";

	var models = require('point_of_sale.models');
	const ProductScreen = require('point_of_sale.ProductScreen');
	var core = require('web.core');
	const { Gui } = require('point_of_sale.Gui');
	const Popup = require('point_of_sale.ConfirmPopup');
	var field_utils = require('web.field_utils');
	var rpc = require('web.rpc');
	var session = require('web.session');
	var time = require('web.time');
	var utils = require('web.utils');
	const PosComponent = require('point_of_sale.PosComponent');
    const Registries = require('point_of_sale.Registries');
	var _t = core._t;

	// Start CreateSalesOrderButtonWidget
	class CreateSalesOrderButtonWidget extends PosComponent {
        constructor() {
            super(...arguments);
        }

		renderElement(){
			var self = this;
				
			var order = self.env.pos.get('selectedOrder');

			var partner_id = false
			if (order.get_client() != null)
				partner_id = order.get_client().id;
			
			 // Popup Occurs when no Customer is selected...
			if (!partner_id) {
				self.showPopup('noCustomerPopup', {});
				return;
			}

			var orderlines = order.orderlines;
			var cashier_id = self.env.pos.get_cashier().user_id[0];
			// Popup Occurs when not a single product in orderline...
				if (orderlines.length === 0) {
					self.showPopup('CustomErrorPopup', {});
					return;
				}
			
			var pos_product_list = [];
			for (var i = 0; i < orderlines.length; i++) {
				var product_items = {
					'id': orderlines.models[i].product.id,
					'quantity': orderlines.models[i].quantity,
					'uom_id': orderlines.models[i].product.uom_id[0],
					'price': orderlines.models[i].price,
					'discount': orderlines.models[i].discount,
				};
				
				pos_product_list.push({'product': product_items });
			}
			
			this.rpc({
				model: 'pos.create.sales.order',
				method: 'create_sales_order',
				args: [partner_id, partner_id, pos_product_list, cashier_id],
			
			}).then(function(output) {
				
				alert('Cotizacion creada con exito !!!!');
				self.showScreen('ProductScreen');  
				

			});
			// this.env.pos.delete_current_order();

		}
	};

	CreateSalesOrderButtonWidget.template = 'CreateSalesOrderButtonWidget';

    Registries.Component.add(CreateSalesOrderButtonWidget);

    return CreateSalesOrderButtonWidget;
	// End CreateSalesOrderButtonWidget	


});
