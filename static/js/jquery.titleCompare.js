// jQuery Plugin Boilerplate
// A boilerplate for jumpstarting jQuery plugins development
// version 1.1, May 14th, 2011
// by Stefan Gabos

(function($) {

    $.titleCompare = function(element, options) {

        var defaults = {
            first_id_element: null,
            second_id_element: null,
            compare_url : '/compare_titles'
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
            $element.click(function() {
                first_id = plugin.settings.first_id_element.val()
                second_id = plugin.settings.second_id_element.val();

                url = plugin.settings.compare_url + '?first=' + first_id + '&second=' + second_id;
                $('#compare_result').load(url);
            })
        }

        plugin.foo_public_method = function() {
            // code goes here
        }

        var foo_private_method = function() {
            // code goes here
        }

        plugin.init();

    }

    $.fn.titleCompare = function(options) {

        return this.each(function() {
            if (undefined == $(this).data('titleCompare')) {
                var plugin = new $.titleCompare(this, options);
                $(this).data('titleCompare', plugin);
            }
        });

    }

})(jQuery);