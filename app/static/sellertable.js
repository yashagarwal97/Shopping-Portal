$(document).ready()(function(){
	getitemsofseller()
})

var getitemsofseller= function()
{
	$.ajax({
          url: 'http://127.0.0.1:5000/cartitems',
          method: 'GET',
          
          success: function (response) {
            console.log("success: it works");
            console.log(response);
        	addtable(response.items)},
          error: function(response){ 
            console.log("error: it doesn't work");
            console.log(response);
          },
       });
}
var addtable=function(itemlist)
{
	text= $('itemtable').html()
	for i in range(len(itemlist)):
		text+='<tr><td>'+ str(i+1) + '</td><td>' + itemlist[i].name + '</td>'
		text +='<td>' + itemlist[i].quantity + '</td></tr>'
	$('itemlist').html(text)


}
