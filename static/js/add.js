$("a.add").bind("click", function () {
    var film = $(this);

    $.get($(film).attr("href"), function (data) {
        $(film).parent().hide();
    });

    return false;
});
