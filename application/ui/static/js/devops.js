$('#action_1_1').click(function () {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/v1/api/scenario/1?action_id=1",
        success: function (data) {
        }
    })
});

function open_pulse_window(url, item) {
    var pulse_window = localStorage.getItem(item);
    if (pulse_window) {
        console.log("changing focus to: " + url);
        pulse_window.focus();
    } else {
        pulse_window = window.open(url, item);
        localStorage.setItem(item, pulse_window);
        pulse_window.focus();
    }
}

$("#step_3_1_action").click(function() {
    var progression = 0,
    progress = setInterval(function() 
    {
        $('#code-fix-progress').css("width", progression + "%");
        $('#code-fix-progress').attr("aria-valuenow", progression + "%");
        $('#code-fix-progress').text(progression + '%');

        if(progression == 100) {
            clearInterval(progress);
            $('#code-fix-progress').text('Done!');
        } else
            progression += 10;

    }, 1000);
});


