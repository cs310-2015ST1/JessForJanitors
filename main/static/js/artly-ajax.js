$(document).ready(function() {

    var checked;

    var index;

    $(".table-hover tr").click(function (event) {

        if (event.target.tagName !== 'SPAN' && event.target.tagName !== 'INPUT') {

            $(':checkbox', this).trigger('click');

            index = parseInt($(':checkbox', this).attr("data-installation-id").substring(4) - 1);

            if(checked) {
                $(".heart", this).addClass('glyphicon-heart').removeClass('glyphicon-heart-empty');
                markers[index].setIcon(highlightedIcon());
            } else {
                $(".heart", this).addClass('glyphicon-heart-empty').removeClass('glyphicon-heart');
                markers[index].setIcon(normalIcon());
            }

            var installation_name;

            installation_name = $(':checkbox', this).attr("data-installation-name");
            installation_id = $(':checkbox', this).attr("data-installation-id");

            $.get('/artly/click_installation/', {name: installation_name}, function(data){
               /*Return name back just for testing purposes*/
               $('#installation_name').html(data);
            });

            $.get('/artly/click_save/', {id: installation_id}, function(data){
                /*Return name back just for testing purposes*/
                $('#installation_id').html(data);
            });
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

    $('#markers_info .marker').hover(
      // mouse in
      function () {
        // first we need to know which <div class="marker"></div> we hovered
        var index = $('#markers_info .marker').index(this);
        markers[index].setIcon(highlightedIcon());
      },
      // mouse out
      function () {
        // first we need to know which <div class="marker"></div> we hovered
        var index = $('#markers_info .marker').index(this);
        markers[index].setIcon(normalIcon());
      }

    );

});