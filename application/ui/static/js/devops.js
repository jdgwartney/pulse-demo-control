$('#action_1_1').click(function () {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/v1/api/scenario/1?action_id=1",
        success: function (data) {
        }
    })
});

function launchApplication(l_url, l_windowName) {
    if (typeof launchApplication.winRefs == 'undefined') {
        launchApplication.winRefs = {};
    }
    if (typeof launchApplication.winRefs[l_windowName] == 'undefined' || launchApplication.winRefs[l_windowName].closed) {
        var l_width = screen.availWidth;
        var l_height = screen.availHeight;
        var l_params = 'status=1' +
            ',resizable=1' +
            ',scrollbars=1' +
            ',width=' + l_width +
            ',height=' + l_height +
            ',left=0' +
            ',top=0';
        l_params = 'status=1' + ',resizable=1' + ',scrollbars=1';


        launchApplication.winRefs[l_windowName] = window.open(l_url, l_windowName, l_params);
        // launchApplication.winRefs[l_windowName] = window.open(l_url, l_windowName);
        launchApplication.winRefs[l_windowName].moveTo(0, 0);
        launchApplication.winRefs[l_windowName].resizeTo(l_width, l_height);
    } else {
        launchApplication.winRefs[l_windowName].focus()
    }
}

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

$("#step_3_1_action").click(function () {
    var progression = 0,
        progress = setInterval(function () {
            $('#code-fix-progress').css("width", progression + "%");
            $('#code-fix-progress').attr("aria-valuenow", progression + "%");
            $('#code-fix-progress').text(progression + '%');

            if (progression == 100) {
                clearInterval(progress);
                $('#code-fix-progress').text('Done!');
            } else
                progression += 10;

        }, 1000);
});


