$(document).ready(function(){
    $("#btnPlus").click(function(event){
        alert("The paragraph was clicked."+dish_name);
    });
});


$(document).ready(function(){
    $("div.card-"+rest_id).click(function(){
        window.location.href="/restaurants/"+rest_id;
    });
});