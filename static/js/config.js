$(document).ready(function () {

    var FieldCount = 1;

    $("#addQuality").bind("click", function () {

        FieldCount++;
        $("#quality").append('<div name="quality_' + FieldCount + '">\
            <input type="text" name="quality_name_' + FieldCount + '" placeholder="Quality name">\
            <input type="text" name="quality_rss_' + FieldCount + '" placeholder="RSS link">\
            </div>');

        return false;
    });

    $("#submit").bind("click", function () {

        var dict = [];

        for (var i = 1; i <= FieldCount; i++) {
            var quality = {};

            quality.title = $('input[name="quality_name_' + i + '"]').val();
            quality.rss = $('input[name="quality_rss_' + i + '"]').val();
            dict.push(quality);
        }

        $.post('/_config_done', JSON.stringify(dict));

        return false;

    })
});
