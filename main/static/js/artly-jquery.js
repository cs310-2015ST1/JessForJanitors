$(document).ready(function () {
    $(".table-hover tr").click(function (event) {
        if (event.target.type !== 'checkbox') {
            $(':checkbox', this).trigger('click');
        }
    });

    $("input[type='checkbox']").change(function (e) {
        if ($(this).is(":checked")) {
            $(this).closest('tr').addClass("success");
        } else {
            $(this).closest('tr').removeClass("success");
        }
    });
});