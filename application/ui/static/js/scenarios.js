$('#action_1_1').click(function () {
    alert('ajax');
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "http://127.0.0.1:5000/v1/api/scenario/1?action_id=1",
        success: function (data) {
            alert(data);
        }
    });
});


$('#action_2_1').click(function () {
    alert('ajax');
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "http://127.0.0.1:5000/v1/api/scenario/1?action_id=1",
        success: function (data) {
            alert(data);
        }
    });
});

$('#action_2_2').click(function () {
    alert('ajax');
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "http://127.0.0.1:5000/v1/api/scenario/1?action_id=1",
        success: function (data) {
            alert(data);
        }
    });
});

$('#action_3_1').click(function () {
    alert('ajax');
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "http://127.0.0.1:5000/v1/api/scenario/1?action_id=1",
        success: function (data) {
            alert(data);
        }
    });
});

$('#action_3_2').click(function () {
    alert('ajax');
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "http://127.0.0.1:5000/v1/api/scenario/1?action_id=1",
        success: function (data) {
            alert(data);
        }
    });
});

