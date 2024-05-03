$(document).ready(function()
{
    $("#add_item").click(function()
    {
        let newElement = $("li").text("Item");

        $("ul.my_list").append(newElement);
    });
});
