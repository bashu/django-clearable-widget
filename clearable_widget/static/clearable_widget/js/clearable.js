(function () {
    "use strict";

    function toggle(field, helper) {
        helper.classList.toggle("hidden", !field.value);
    }

    function bind(field) {
        var helper = field.parentNode.querySelector(".clear-helper");
        if (!helper || field.dataset.clearableBound) {
            return;
        }
        field.dataset.clearableBound = "true";

        helper.addEventListener("click", function () {
            helper.classList.add("hidden");
            field.value = "";
            field.focus();
            var form = field.closest("form");
            if (form) {
                form.dispatchEvent(
                    new CustomEvent("cleared.clearable", { detail: field, bubbles: true }),
                );
            }
        });

        ["keyup", "change", "input"].forEach(function (type) {
            field.addEventListener(type, function () {
                toggle(field, helper);
            });
        });

        // Match the helper's visibility to the field's initial value, since
        // it otherwise stays hidden (per the "hidden" class in the markup)
        // until the user's first keystroke -- wrong for pre-filled fields.
        toggle(field, helper);
    }

    function clearable(root) {
        (root || document).querySelectorAll(".clear-holder input").forEach(bind);
    }

    function ready(fn) {
        if (document.readyState === "loading") {
            document.addEventListener("DOMContentLoaded", fn);
        } else {
            fn();
        }
    }

    ready(function () {
        clearable();
    });

    // Exposed so consumers can (re-)bind fields added after page load, e.g.
    // a formset row inserted via AJAX: clearable(newRowElement).
    window.clearable = clearable;
})();
