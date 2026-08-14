(function ($, undefined) {
    $.fn.clearable = function () {
        var $this = this;

        function toggle() {
            $(".clear-helper", $this.parent()).toggleClass("hidden", !$this.val());
        }

        $(".clear-helper", $this.parent()).on('click', function(){
            $(this).addClass('hidden'); $this.val("").focus();
            var $form = $this.closest('form');
            if ($form.length) { $form.trigger('cleared.clearable', [$this]); }
        });
        $this.on('keyup change input', toggle);

        // Match the helper's visibility to the field's initial value, since
        // it otherwise stays hidden (per the "hidden" class in the markup)
        // until the user's first keystroke -- wrong for pre-filled fields.
        toggle();

        return this;
    };
})(jQuery);
