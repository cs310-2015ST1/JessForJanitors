$(document).ready(function() {

    var checked;

    $(".table-hover tr").click(function (event) {

        if (event.target.tagName !== 'SPAN' && event.target.tagName !== 'INPUT') {

            $(':checkbox', this).trigger('click');

            if(checked) {
                $(".heart", this).addClass('glyphicon-heart').removeClass('glyphicon-heart-empty');
            } else {
                $(".heart", this).addClass('glyphicon-heart-empty').removeClass('glyphicon-heart');
            }

            var installation_name;

            installation_name = $(':checkbox', this).attr("data-installation-name");

            $.get('/artly/click_installation/', {name: installation_name}, function(data){
               /*Return name back just for testing purposes*/
               $('#installation_name').html(data);
            });
//
//            $.get('/artly/click_favourite/', {name: installation_name}, function(data){
//                /*Return name back just for testing purposes*/
//                $('#installation_name').html(data);
//             });
         }
    });

    $("input[type='checkbox']").change(function (e) {
        if ($(this).is(":checked")) {
            $(this).closest('tr').addClass("success");
            checked = true;
        } else {
            $(this).closest('tr').removeClass("success");
            checked = false;
        }

        sortCheck();
    });
});