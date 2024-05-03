$(document).ready(function()
{
    $.ajax(
    {
        url: "https://swapi-api.alx-tools.com/api/films/?format=json",
        method: "GET",
        dataType: "json",
        success: function(database)
        {
            if (database)
                {
                    for (dicti of database.results)
                        {
                            $("UL#list_movies").append(`<li>${dicti.title}</li>`);
                        }
                }
        },
        error: function()
        {
            $("#list_movies").text("Unable to fetch title");
        }
    });
});
