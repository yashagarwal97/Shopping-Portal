$(document).ready(function(){
	b=location.href;
	c=b.split('/');
	d=c[c.length -1];
	console.log('gulshan');
	viewAllItems(d);
})
var viewAllItems = function(d){
	$.ajax({
		type : 'GET',
		url : 'http://127.0.0.1:5000/sellertable/category/' +d,
		success: function(response){
			allitems=response['Category']
			viewAllItemsInHtml(allitems);
		},
		error: function(a,status,b){
			console.log(status);
		},
	})
}
var viewAllItemsInHtml=function(allitems){
	var string= '<thead><tr><td>Name</td> <td> description </td> <td> Price </td> </tr></thead>';
	var len=allitems.length;
	console.log("gulshan")
	for(var i=0;i-len< 0 ;i+=1)
	{
		string+='<tr>' + '<td>' + allitems[i]['name'] + '</td>' + '<td>' + allitems[i]['description'] + '</td>' 
		+ '<td>' + allitems[i]['price'] + '</td>' + '<td>' + '<a href=\"{{url_for(\"sellertable.categorytable"\ , typ=\"electrical_appliance"\ )}}"\>' + 'View that item'+ '</a>' + '</td>'+ '</tr>' ;
	}
	
	$("#allitems").html(string);
	return;
}
