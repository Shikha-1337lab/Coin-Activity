

$(document).ready(function(){

    $("#container-createPanel").css("display", "none");
    $("#container-loginPanel").css("display", "none");
    $(".blankDiv").css("display", "none");

    $("#btn-createAccount").click(function(){
      $("#container-loginPanel").slideUp("slow");
      $("#container-createPanel").slideDown("slow");
      $(".blankDiv").css("display", "block");
    });

    $("#create").click(function(){
        $("#container-createPanel").slideUp("slow");
        $(".blankDiv").css("display", "none");
    });

    $("#btn-login").click(function(){
        $("#container-createPanel").slideUp("slow");
        $("#container-loginPanel").slideDown("slow");
        $(".blankDiv").css("display", "block");
    });

    $("#login").click(function(){
        $("#container-loginPanel").slideUp("slow");
        $(".blankDiv").css("display", "none");
    });

    $(".blankDiv").click(function(){
      $("#container-loginPanel").slideUp("slow");
      $("#container-createPanel").slideUp("slow");
      $(".blankDiv").css("display", "none");
    });

});
