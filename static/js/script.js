/**
 * Created by kendricktan on 7/08/16.
 */
$(document).ready(function () {
    $("#landing_form").submit(function (event) {
        event.preventDefault();

        var data = $('#landing_form').serialize();

        $.ajax({
            url: '',
            type: 'post',
            data: data,
            success: function (data) {
                var my_var_string = "<strong>";

                if (data['success'] == true) {
                    my_var_string += "<span style='color: #37BC9B'>"
                }
                else {
                    my_var_string += "<span style='color: #ED5565'>"
                }

                my_var_string += "<p class='text-center'>" + data["message"] + "</p></span></strong>";

                $("#landing_response").html(my_var_string);
                $("#landing_response").collapse("show");
            }
        });
    });
})