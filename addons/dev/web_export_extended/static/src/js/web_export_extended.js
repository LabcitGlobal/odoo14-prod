odoo.define('web_export_extended.web_export_extended' , function(require) {
    "use strict";
    var core = require('web.core');
    var _t = core._t;
    var Dialog = require('web.Dialog');
    var ListController = require('web.ListController');
    var ActionMenus = require("web.ActionMenus");
    var rpc = require('web.rpc');
    var DataExport = require('web.DataExport');
    var session = require('web.session');


    var ViewExtended = ListController.include({
     _onExportData: function () {
            var record = this.model.get(this.handle);
            new DataExportPassword(this, record).open();
        },
    });

     var DataExportPassword = Dialog.extend({
        template: 'ExportPasswordView',
	    events: {},
	    init: function(parent, dataset) {
	        var self = this;
	        var options = {
	            buttons: [
	                {text: _t("Close"), click: function () { self.$el.parents('.modal').modal('hide'); }},
	                {text: _t("Check Password"), click: function () { self.check_password(); }}
	            ],
	            close: function () { self.close();}
	        };

	        this._super(parent, options);
	        this.records = {};
	        this.dataset = dataset;
	        this.parent = parent;
	    },
	    start: function() {
	    	var self = this;
	        this._super.apply(this, arguments);
	    },
	    close: function() {
	        this._super();
	    },
	    check_password: function(){
	    	var self = this;
	    	var password = this.$el.find('#export_password').val();
	    	if (!password){
	    		alert(_t("Please enter the password"));
	            return;
	    	}
	    	console.log("++++++++++password+++++++++++==",password)
	    	rpc.query({
                model: 'res.users',
                method: 'export_check_credentials',
                args:[session.uid,password],
	    	}).then(function(result){

	    	   console.log("++++++++++result+++++++++++==",result)

	    	        if(result){
	    	        console.log("++++++++++if+++++++++",result);

                            self.close();
                            new DataExport(self.parent, self.dataset).open();
                    }else{
                    console.log("++++++++++else+++++++++",result);
                        alert(_t("Password is wrong!"));
    	                return;
                    }
	    	});
	    },
    })
    console.log("------this-----",this);

    ActionMenus.include({
        start: function () {
            var self = this;
            this._super(this, arguments);
	    _.each(self.items['other'], function(items, index){
                if(items.label == 'Export'){
                    rpc.query({
                    	model: 'res.users',
                    	method: 'has_group',
                    	args:['web_export_extended.group_display_export'],
                    }).then(function (result) {

			if(!result){
			    self.items['other'].splice(index,1);
                            self._redraw();
                        }
                     });
                }

            });
        },
    });


});
