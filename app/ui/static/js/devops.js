$('#reset').click(function () {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/v1/api/action?scenario=devops&action=reset",
        success: function (data) {
        }
    })
});
$('#bad_page_to_host').click(function () {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/v1/api/action?scenario=devops&action=bad_page_to_host",
        success: function (data) {
        }
    })
});

$('#revert_bad_page_to_host').click(function () {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/v1/api/action?scenario=devops&action=revert_bad_page_to_host",
        success: function (data) {
        }
    })
});

$('#improved_page_to_host').click(function () {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/v1/api/action?scenario=devops&action=improved_page_to_host",
        success: function (data) {
        }
    })
});

$('#improved_page_to_all_hosts').click(function () {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/v1/api/action?scenario=devops&action=improved_page_to_all_hosts",
        success: function (data) {
        }
    })
});


function launchApplication(l_url, l_windowName) {
    if (typeof launchApplication.winRefs == 'undefined') {
        launchApplication.winRefs = {};
    }
    if (typeof launchApplication.winRefs[l_windowName] == 'undefined' ||
        launchApplication.winRefs[l_windowName].closed) {
        var l_width = screen.availWidth / 2;
        var l_height = screen.availHeight;
        var l_left = screen.availWidth / 2;
        var l_params = 'status=1' +
            ',resizable=1' +
            ',menubar=1' +
            ',resizable=0' +
            ',scrollbars=1' +
            ',titlebar=1' +
            ',width=' + l_width +
            ',height=' + l_height +
            ',left=' + l_left +
            ',top=0';


        launchApplication.winRefs[l_windowName] = window.open(l_url, l_windowName, l_params);
        launchApplication.winRefs[l_windowName].moveTo(l_left, 0);
        launchApplication.winRefs[l_windowName].resizeTo(l_width, l_height);
    } else {
        launchApplication.winRefs[l_windowName].focus()
    }
}

$("#fix_bad_page").click(function () {
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


