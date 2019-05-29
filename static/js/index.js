window.onload=function(){
	var w = $(window).width();
	var h = $(window).height();
	if(w < 1425 || h < 545)
	{
		$("#left-bar").hide();
		$(".main-content").css({"margin-left":"","margin-right":"","float":""});
		//$(".main-content").animate({"margin-left":"","margin-right":"","float":"none",}, 10);
	}
	else
	{
		$("#left-bar").show(500);
		$(".main-content").css({"margin-left":"20px","margin-right":"30px","float":"right","width":"80%"});
		//$(".main-content").animate({"margin-left":"10px","margin-right":"20px","float":"right",}, 10);
	}
}

$(window).resize(function(){
	var w = $(window).width();
	var h = $(window).height();
	if(w < 1425 || h < 545)
	{
		$("#left-bar").hide();
		$(".main-content").css({"margin-left":"","margin-right":"","float":""});
	}
	else
	{
		$("#left-bar").show(500);
		$(".main-content").css({"margin-left":"20px","width":"80%","float":"right","margin-right":"30px"});
	}
});
