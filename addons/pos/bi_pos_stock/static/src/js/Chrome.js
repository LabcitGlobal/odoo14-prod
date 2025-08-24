odoo.define('bi_pos_stock.Chrome', function(require) {
	'use strict';

	const Registries = require('point_of_sale.Registries');
	const Chrome = require('point_of_sale.Chrome');

	const BiChrome = (Chrome) =>
		class extends Chrome {
			constructor() {
				super(...arguments);
			}
			get is_stock_sync() {
				// if(this.env && this.env.pos && this.env.pos.config && this.env.pos.config.show_stock_location == 'specific'){
				if(this.env && this.env.pos && this.env.pos.config && this.env.pos.config.pos_sync){
					return true
				}
				else{
					return false
				}
			}
		}
	Registries.Component.extend(Chrome, BiChrome);
	return Chrome;
});
