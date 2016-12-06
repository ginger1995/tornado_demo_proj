$(document).ready(function(){
    alert("connected to the server successfully!");
    $("#search").click(function(){
        var word = $("#word").val();
        alert("you are going to search: "+word);
    });
});