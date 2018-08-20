allreviews=[]

var addReview=function(text,id){
        var details= text ;

        console.log(id)
        console.log(text)
        $.ajax({
                type: 'POST',
                // url:  'http://127.0.0.1:5000/reviews/addReview/'+ id,
                url: $SCRIPT_ROOT + '/reviews/addReview/' + id,
                data: { text: details },
                success: function(response){
                        console.log(response);
                        viewAllReviews(id);
                        
                },
                error: function(x,status,y){
                        console.log(status);
                        console.log("YO")
                        alert(status);

                },
        });

};
var review1 =function(id)
{
        var text = $('#Review').val();
        console.log(text)
        addReview(text,id);
}
var viewAllReviews=function(id){
        //console.log(id)
        $.ajax({
                type:'GET',
                // url:'http://127.0.0.1:5000/reviews/showReview/'+ id,
                url: $SCRIPT_ROOT + '/reviews/showReview/'+ id,
                success: function(response){
                        console.log(response);
                        allreviews=response["Review"];       
                        viewAllReviewHtml(allreviews);
                },
                error: function (a,status,b){
                        console.log(status);
                },
        })
}

var sendnotification=function(userid,itemid)
{
	console.log(userid,itemid);
         $.ajax({

                type:'POST',
                // url:'http://127.0.0.1:5000/notif/receive',
                url: $SCRIPT_ROOT + '/notif/receive',
                data: { userid: userid ,itemid: itemid },
                success: function(response){
                        console.log(response);
			$('#message').html(response);
                },
                error: function (a,status,b){
                        console.log(status);
            },
        })

}

var addtobuyerscart=function(itemid)
{
		console.log(itemid);
	       $.ajax({

                type:'POST',
                // url:'http://127.0.0.1:5000/buyertable/additem',
                url: $SCRIPT_ROOT + '/buyertable/additem',
                data: { itemid: itemid },
                success: function(response){
                        console.log(response);
			$('#message').html(response);
                        //allreviews=response["Review"];       
                        //viewAllReviewHtml(allreviews);
                },
                error: function (a,status,b){
                        console.log(status);
            },
        })

}


var  viewAllReviewHtml=function(allreviews)
{

        var cut="<thead><tr><td>Username</td><td>Review</td></tr></thead><tbody>";
        var len=allreviews.length;
        for(var i=0; i-len<0; i+=1)
        {
                // var j=i+1;
                cut+="<tr>"
                + "<td>" + allreviews[i]['user'] + "</td>"
                + "<td>" + allreviews[i]['Review'] + "</td>"
                + "</tr>";
        }
        cut+="</tbody>";
        $("#allreview").html(cut);
        return;
}
