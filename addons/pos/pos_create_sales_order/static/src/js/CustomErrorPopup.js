odoo.define('pos_create_sales_order.CustomErrorPopup', function(require) {
	'use strict';

	const ErrorPopup = require('point_of_sale.ErrorPopup');
	const Registries = require('point_of_sale.Registries');

	class CustomErrorPopup extends ErrorPopup {
		go_back_screen() {
			this.showScreen('ProductScreen');
			this.trigger('close-popup');
		}
	}
	CustomErrorPopup.template = 'CustomErrorPopup';
	CustomErrorPopup.defaultProps = {
		// confirmText: 'Ok',
		// cancelText: 'Cancel',
		title: 'Pedido Vacio',
		body: 'Debe haber al menos un producto en su pedido para crear cotizacion.',
	};

	Registries.Component.add(CustomErrorPopup);

	return CustomErrorPopup;
});
