$(document).ready(function()
{
    $.ajax(
    {
        url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
        method: "GET",
        dataType: "json",
        success: function(database)
        {
            let characterName = database.name;

            $("#character").text(characterName);
        },
        error: function()
        {
            $("#character").text("Unable to fetch character")
        }
    });
});