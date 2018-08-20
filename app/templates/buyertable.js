listofitems=[];qnty=[];
$(document).ready(function(){
	getitemsofbuyer()
  $("#add-item-button").click(function(event){
    event.preventDefault();


  })
  $('#update-item-button').click(function(event){
    event.preventDefault();
    updateallitems();
  })
  $('#buy-button').click(function(event){
    event.preventDefault();
    buyitemsincart();
  })

})


var getitemsofbuyer= function()
{
	$.ajax({
          url: $SCRIPT_ROOT+'/cart/cartitemsofbuyer',
          method: 'GET',
          
          success: function (response) {
            console.log("success: it works");
            console.log(response);
            listofitems=response.items
            qnty=response.qnty
        	addtable(response.items)},
          error: function(response){ 
            console.log("error: it doesn't work");
            console.log(response);
          },
       });
}

var deleteitem=function(itemid)
{

$.ajax({
          url: $SCRIPT_ROOT+'/cart/delete',
          method: 'POST',
          data: { itemid: itemid },
          success: function (response) {
	   $('#message').html(response);
            console.log(response);
        	getitemsofbuyer() 
        	},
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
	var num=i+1;
	text+='<tr><td>'+ num+ '</td><td><a href="' + $SCRIPT_ROOT + '/tags/' + itemlist[i].id + '">' + itemlist[i].name + '</a></td>';
    text +='<td> <input type="number" class="my" id="' + i + '" min="0" value ="' + qnty[i] +'"></td>'
    text+='<td><input type="submit" class="btn btn-danger" value="DELETE"' + 'onclick="deleteitem('+ itemlist[i].id + ')" </td></tr>'
  }
   $('#itemtable').html(text)

    
}

var buyitemsincart=function()
{ 
      $.ajax({
          url: $SCRIPT_ROOT+'/cart/buy',
          method: 'POST',
          data: {
                },
          success: function (response) {
	    $('#message').html(response);
            console.log(response);
            getitemsofbuyer();
          },
          error: function(response){ 
          console.log("error: it doesn't work");
            console.log(response);
          },
       });
}

var updateallitems=function()
{
  for (i=0;i<listofitems.length;i++)
  {
    value=$('#'+i).val()
   qnty[i]=value
    console.log(value)
    console.log(listofitems[i].id)
     $.ajax({
          url: $SCRIPT_ROOT+'/buyertable/update',
          method: 'POST',
          data: {
                itemid: listofitems[i].id , quantity : value
                },
          success: function (response) {
	   $("#message").html(response);
            console.log(response);},
          error: function(response){ 
console.log("error: it doesn't work");
            console.log(response);
          },
       });


  }
  getitemsofbuyer()
}
