//window width
var winWidth = $( window ).width();
$(".carousel-inner").css("font-size", winWidth/25.6);

function dropControl(){
    if(winWidth < 768){
        document.getElementById("dropdown_menu").style.position = "relative";
    } else{
        document.getElementById("dropdown_menu").style.position = "absolute";
    }

    if(document.getElementById("dropdown_menu").style.height == "82px"){
        document.getElementById("dropdown_menu").style.height = "0px";
    } else{
        document.getElementById("dropdown_menu").style.height = "82px";
    }
}

$(document).ready(function(){
  //resize font size when resolution change
  $(window).resize(function(){
    winWidth = $( window ).width();
    $(".carousel-inner").css("font-size", winWidth/25.6);
  })
});