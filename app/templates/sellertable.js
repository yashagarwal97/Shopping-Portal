listofitems=[];
$(document).ready(function(){
	getitemsofseller()
  $("#add-item-button").click(function(event){
	event.preventDefault();
	gotoadditem();


  })
  $('#update-item-button').click(function(event){
	event.preventDefault();
	updateallitems();
  })
})


var getitemsofseller= function()
{
	$.ajax({
		  // url: 'http://127.0.0.1:5000/cart/cartitems',
		  url: $SCRIPT_ROOT +'/cart/cartitems',

		  method: 'GET',
		  
		  success: function (response) {
			console.log("success: it works");
			console.log(response);
			listofitems=response.items
			addtable(response.items)},
		  error: function(response){ 
			console.log("error: it doesn't work");
			console.log(response);
		  },
	   });
}
var addtable=function(itemlist)
{
	var text= ""
  var len = itemlist.length
	for (i=0;i<len;i++)
  {
	var num =i+1;
	  text+='<tr><td>'+ num + '</td><td><a href="' + $SCRIPT_ROOT + '/tags/' + itemlist[i].id + '">' + itemlist[i].name + '</a></td><br/>';

	text +='<td> <input type="number" id="' + i + '" min="' + itemlist[i].quantity + '" value ="' + itemlist[i].quantity +'"></td></tr><br/>'

  }
   $('#itemtable').html(text)

	
}
var updateallitems=function()
{
  for (i=0;i<listofitems.length;i++)
  {
	value=$('#'+i).val()
	console.log(value)
	console.log(listofitems[i].id)
	 $.ajax({
		  // url: 'http://127.0.0.1:5000/sellertable/update',
		  url: $SCRIPT_ROOT+ '/sellertable/update',
		  method: 'POST',
		  data: {
				itemid: listofitems[i].id , quantity : value
				},
		  success: function (response) {
			$('#message').html(response);
			console.log(response);},
		  error: function(response){ 
console.log("error: it doesn't work");
			console.log(response);
		  },
	   });


  }
  getitemsofseller()
}
var gotoadditem =function()
{
  window.location.href= window.location + '/additem'
}
