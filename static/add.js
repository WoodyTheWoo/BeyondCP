$( 'button[name="add"]' ).click(function( event )
{
    var title = $(this).parent().children("a").text();
    alert( title );
});
