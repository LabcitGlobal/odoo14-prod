odoo.define('aces_pos_note.NotePaymentScreen', function (require) {
    'use strict';

    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');

    const NotePaymentScreen = (PaymentScreen) =>
        class extends PaymentScreen {
            async validateOrder(isForceValidate) {
                if (await this._isOrderValid(isForceValidate)) {
                    // remove pending payments before finalizing the validation
                    for (let line of this.paymentLines) {
                        if (!line.is_done()) this.currentOrder.remove_paymentline(line);
                    }

                    if(this.env.pos.config.enable_order_note) {
                        var currentOrder = this.env.pos.get_order();
                        currentOrder.set_order_note($('#order_note').val());
                    }

                    await this._finalizeValidation();
                }
            }
        };

    Registries.Component.extend(PaymentScreen, NotePaymentScreen);

    return NotePaymentScreen;
});
