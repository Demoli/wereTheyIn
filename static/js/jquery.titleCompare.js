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

        plugin.search_elements = []

        var $element = $(element),
             element = element;

        plugin.init     = function() {
            plugin.settings = $.extend({}, defaults, options);
            plugin.search_elements = [
                plugin.settings.first_id_element,
                plugin.settings.second_id_element
            ]
            register_events();
        }

        var register_events = function() {

            $(plugin.search_elements).each(function() {
                $(this).change(function() {
                    $('#compare_result').empty();
                    var first_id = plugin.search_elements[0].val();
                    var second_id = plugin.search_elements[1].val();

                    if(first_id && second_id) {
                        url = plugin.settings.compare_url + '?first=' + first_id + '&second=' + second_id;
                        $('#compare_result').load(url);
                    }
                });
            })
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