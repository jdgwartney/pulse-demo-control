$('#action_1_1').click(function () {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/v1/api/scenario/1?action_id=1",
        success: function (data) {
        }
    })
});


$('#action_2_1').click(function () {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/v1/api/scenario/2?action_id=1",
        success: function (data) {
        }
    });
});

$('#action_2_2').click(function () {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/v1/api/scenario/2?action_id=1",
        success: function (data) {
        }
    });
});

$('#action_3_1').click(function () {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/v1/api/scenario/3?action_id=1",
        success: function (data) {
        }
    });
});

$('#action_3_2').click(function () {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/v1/api/scenario/3?action_id=1",
        success: function (data) {
        }
    });
});

