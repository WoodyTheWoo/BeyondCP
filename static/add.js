$( "a.add" ).bind( "click", function() {
    var movie_title = $(this).url().param("title");
    var movie_year = $(this).url().param("year");
    var movie_imdb_id = $(this).url().param("imdb_id");
    var film = $(this)

    $.getJSON($SCRIPT_ROOT + "/_add_movie_to_db", {
        title: movie_title,
        year: movie_year,
        imdb_id: movie_imdb_id,
        toto: "toto"
    }, function(data) {
        $(film).parent().hide();
    });

    return false;
});
