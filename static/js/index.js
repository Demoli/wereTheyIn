// jQuery Plugin Boilerplate
// A boilerplate for jumpstarting jQuery plugins development
// version 1.1, May 14th, 2011
// by Stefan Gabos

(function($) {

    $.titleSearch = function(element, options) {

        var defaults = {
            url: '/search_title'
        }

        var plugin = this;

        plugin.settings = {}

        var $element = $(element),
             element = element;

        plugin.init     = function() {
            plugin.settings = $.extend({}, defaults, options);
            register_events();
        }

        var register_events = function() {
            $element.autocomplete(
                {
                    source: plugin.settings.url,
                    minLength:4,
                    delay:1000
                }
            )
        }

        plugin.foo_public_method = function() {
            // code goes here
        }

        var foo_private_method = function() {
            // code goes here
        }

        plugin.init();

    }

    $.fn.titleSearch = function(options) {

        return this.each(function() {
            if (undefined == $(this).data('pluginName')) {
                var plugin = new $.titleSearch(this, options);
                $(this).data('pluginName', plugin);
            }
        });

    }

})(jQuery);