$(document).ready(function() {

    var checked;

    var index;

    $(".table-hover tr").click(function (event) {

        if (event.target.tagName !== 'SPAN' && event.target.tagName !== 'INPUT') {

            $(':checkbox', this).trigger('click');

            index = parseInt($(':checkbox', this).attr("data-installation-id").substring(4)) - 1;

            if(checked) {
                //$(".heart", this).addClass('glyphicon-heart').removeClass('glyphicon-heart-empty');
                markers[index].setIcon(highlightedIcon());
            } else {
                //$(".heart", this).addClass('glyphicon-heart-empty').removeClass('glyphicon-heart');
                markers[index].setIcon(normalIcon());
            }
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

        sortByCheckbox();
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