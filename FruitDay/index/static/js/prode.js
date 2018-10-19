$(function(){
	var gc = $('#bu-count');
    var tar_a = $('#buynow');
    var val_a = tar_a.attr('href');
    tar_a.attr("href",val_a+gc.val());
    $('#bu-up').click(function(){
		var num = Number(gc.val());
		gc.val(++num);
		tar_a.attr("href",val_a+num);
	});
	$('#bu-down').click(function(){
		var num = Number(gc.val());
		if(num<=1){
			num = 1;
		}else{
			num--;
		}
		gc.val(num);
    	tar_a.attr("href",val_a+num);
	});

	gc.blur(function(){
		var num = gc.val();
		console.log(num);
		tar_a.attr("href",val_a+num);
	});


});