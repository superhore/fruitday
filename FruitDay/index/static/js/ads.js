$(function(){
		
	$('#bu-add').click(function(){
		var aname = $('#aname').val();
		var cellphone = $('#cellphone').val();
		var dizhi = $('#dizhi').val();
		if (aname&&cellphone&&dizhi)
			{var choice = $("<input>");
			choice.attr('type','radio');
			choice.attr('name','seled');
			var tdname = $("<td>"+aname+"</td>");
			var tdcphone = $("<td>"+cellphone+"</td>");
			var tddizhi = $("<td>"+dizhi+"</td>");
			var deltr = $("<button>删除</button>");
			deltr.click(function(){
				if(confirm('确认要删除该地址吗？')){
					var adsid = choice.attr('value');
					$.ajax({
						url:'/address/delads',
						data:{'adsid':adsid},
						type:'get',
						datatype:'json',
						success:function(data){
							console.log('delok');
						},
						error:function(err){
							console.log('delfail');
						}
					});
					$(this).parent().parent().remove();
				}
			});
			var tbtd = $("<td></td>");
			tbtd.append(deltr);
			var tbtr = $("<tr></tr>");
			tbtr.append(choice);
			tbtr.append(tdname);
			tbtr.append(tdcphone);
			tbtr.append(tddizhi);
			tbtr.append(tbtd);
			$('#ad-tbody').append(tbtr);

			$.ajax({
				url:'/address/addads',
				data:{'aname':aname,
					'address':dizhi,
					'cellphone':cellphone},
				type:'get',
				datatype:'json',
				success:function(data){
					choice.attr('value', data);
				},
				error:function(err){
					console.log('fail');
				}
			});
			}else{
				alert('地址信息不全');
		};
	});
});
	function delads(obj,adsid){
		if(confirm('确定要删除该地址吗？')){
			$.ajax({
				url:'/address/delads',
				data:{'adsid':adsid},
				type:'get',
				datatype:'json',
				success:function(data){
					console.log('del ok');
				},
				error:function(err){
					console.log('del fail');
				}
			});
			$(obj).parent().parent().remove()
		};

	};




