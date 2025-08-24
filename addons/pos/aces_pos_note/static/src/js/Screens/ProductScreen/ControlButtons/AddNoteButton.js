odoo.define('aces_pos_note.AddNoteButton', function(require) {
    'use strict';

    const PosComponent = require('point_of_sale.PosComponent');
    const ProductScreen = require('point_of_sale.ProductScreen');
    const { useListener } = require('web.custom_hooks');
    const Registries = require('point_of_sale.Registries');

    class AddNoteButton extends PosComponent {
        constructor() {
            super(...arguments);
            useListener('click', this.onClick);
        }
        get selectedOrderline() {
            return this.env.pos.get_order().get_selected_orderline();
        }
        async onClick() {
            if (!this.selectedOrderline) return;

            const { confirmed, payload: inputNote } = await this.showPopup('ProductNotePopup', {
                startingValue: this.selectedOrderline.get_product_note(),
                title: this.env._t('Añadir Nota'),
            });

            if (confirmed) {
                this.selectedOrderline.set_product_note(inputNote);
            }
        }
    }
    AddNoteButton.template = 'AddNoteButton';

    ProductScreen.addControlButton({
        component: AddNoteButton,
        condition: function() {
            return this.env.pos.config.enable_product_note;
        },
    });

    Registries.Component.add(AddNoteButton);

    return AddNoteButton;
});
