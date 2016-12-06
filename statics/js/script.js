$(document).ready(function(){
    alert("connected to the server successfully!");
    $("#search").click(function(){
        var word = $("#word").val();
        var post_data = {"word":word};
        $.ajax({
            type:"post",
            url:"/",
            data:post_data,
            cache:false,
            success:function(data){
                alert(data);
            },
            error:function(){
                alert("error!");
            },
        });
    });
});