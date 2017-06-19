// jQuery Plugin Boilerplate
// A boilerplate for jumpstarting jQuery plugins development
// version 1.1, May 14th, 2011
// by Stefan Gabos

(function ($) {

    $.titleSearch = function (element, options) {

        var defaults = {
            search_url: '/search_title',
            get_url: '/get_title',
            load_element: $element,
            id_element: null
        }

        var plugin = this;

        plugin.settings = {}

        var $element = $(element),
            element = element;

        plugin.init = function () {
            plugin.settings = $.extend({}, defaults, options);
            register_events();
        }

        var register_events = function () {
            $element.autocomplete(
                {
                    source: plugin.settings.search_url,
                    minLength: 4,
                    delay: 1000,
                    select: function (event, ui) {
                        var id = ui.item.value
                        plugin.settings.id_element.val(id);
                        plugin.settings.id_element.change();
                        $element.val(ui.item.label);
                        plugin.settings.load_element.load(plugin.settings.get_url + '?id=' + id)
                        return false;
                    }
                }
            )
        }

        plugin.foo_public_method = function () {
            // code goes here
        }

        var foo_private_method = function () {
            // code goes here
        }

        plugin.init();

    }

    $.fn.titleSearch = function (options) {

        return this.each(function () {
            if (undefined == $(this).data('titleSearch')) {
                var plugin = new $.titleSearch(this, options);
                $(this).data('titleSearch', plugin);
            }
        });

    }

})(jQuery);