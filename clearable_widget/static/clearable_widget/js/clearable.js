(function ($, undefined) {
    $.fn.clearable = function () {
        var $this = this;
        $(".clear-helper").on('click', function(){
            $this.val("").focus();
            var form = $this.closest('form');
            if (form) { $(form).trigger('cleared.clearable', [$this]); }
        });
    };
})(jQuery);
