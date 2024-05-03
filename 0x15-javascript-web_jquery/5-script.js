$(document).ready(function()
{
    $("#add_item").click(function()
    {
        let newElement = "<li>Item</li>";

        $("ul.my_list").append(newElement);
    });
});
