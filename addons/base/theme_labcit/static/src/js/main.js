/*  ---------------------------------------------------
    Template Name: Labcit Services
    Description: Labcit HTML template
    Author: Labcit
    Author URI: https://labcit.com/
    Version: 1.0
    Created: Labcit
---------------------------------------------------------  */

odoo.define('theme_labcit.theme_labcit',function(require){
    'use strict';

    $(document).ready(function () {        
            const preload = document.querySelector(".preload");
            const lcmenu = document.querySelector(".lcmenu");
            const footer = document.querySelector(".div-footer");
            // console.log(footer);
            // delay(10000);        
            preload.classList.add("preload-finish");
            lcmenu.classList.replace("lcmenu","lcmenu-init");
            footer.classList.replace("div-footer","div-footer-init");
            // if (screen.width <= 540) {
            //     const mobile = document.querySelector(".mobile-play");
            //     mobile.classList.replace("mobile-play","mobile-play-init");
            // }        
    });

    // $(document).ready(function () {
    //     $('#slider-logo').owlCarousel({
    //         loop:true,
    //         margin:15,
    //         nav:false,
    //         rewind:true,
    //         autoplay:true,
    //         // autoplayTimeout:10,
    //         // dots: ($(".owl-carousel .item").length > 1) ? true: false,
    //         // loop:($(".owl-carousel .item").length > 1) ? true: false,
    //         responsive:{
    //             0:{
    //                 items:2
    //             },
    //             600:{
    //                 items:2
    //             },
    //             1000:{
    //                 items:4
    //             },
    //             1200:{
    //                 items:5
    //             }
    //         }
    //     });
    //     $('#block-process').owlCarousel({
    //         loop:true,
    //         margin:15,
    //         nav:false,
    //         autoplay:true,
    //         responsive:{
    //             0:{
    //                 items:1
    //             },
    //             600:{
    //                 items:2
    //             },
    //             1000:{
    //                 items:2
    //             },
    //             1200:{
    //                 items:3
    //             }
    //         }
    //     });
    //     $('#slider-about').owlCarousel({
    //         loop:true,
    //         margin:15,
    //         nav:false,
    //         autoplay:true,
    //         autoplayTimeout:3000,
    //         responsive:{
    //             0:{
    //                 items:1
    //             },
    //             600:{
    //                 items:1
    //             },
    //             1000:{
    //                 items:1
    //             },
    //             1200:{
    //                 items:1
    //             }
    //         }
    //     });
    // });

});