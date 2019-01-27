$("#btnLocate").click(function() {
    
    $([document.documentElement, document.body]).animate({
        scrollTop: $("#divToilet").offset().top 
    }, 2000);
});

$("#btnLocate").click(function() {
    $([document.documentElement, document.body]).animate({
        scrollTop: $("#divToilet").offset().top
    }, 2000);
});


$(document).ready(function(){
	$(window).on("scroll",function(){
  	var wn = $(window).scrollTop();
    if(wn > 300){
    	$(".navbar").css("background","rgba(3, 53, 99, 1)");
    }
    else{
        $(".navbar").css("background","transparent");
        $(".navbar").css("transition","500ms ease");

    }
  });
});