$(document).ready(function() {

    $(".table-hover tr").click(function (event) {
        if (event.target.id !== 'no-check' && event.target.type !== 'checkbox') {
            $(':checkbox', this).trigger('click');

            var installation_name;

            installation_name = $(':checkbox', this).attr("data-installation-name");

            $.get('/artly/click_installation/', {name: installation_name}, function(data){
               /*Return name back just for testing purposes*/
               $('#installation_name').html(data);
            });
         }
    });

    $("input[type='checkbox']").change(function (e) {
        if ($(this).is(":checked")) {
            $(this).closest('tr').addClass("success");
        } else {
            $(this).closest('tr').removeClass("success");
        }

        sortCheck();
    });
});