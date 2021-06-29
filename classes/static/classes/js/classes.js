let clicked;
let class_pk;

$(".class-signup-btn").click(function() {
    if(!event.detail || event.detail == 1){
        curr_button = $(this)
    curr_color = $(this).data('color')
    if(curr_color == 'yellow'){
        clicked = false;
    }
    if(curr_color == 'green'){
        clicked = true;
    }
    class_pk = $(this).data('classid');
    let curr_class = $(this).parent()
    $.ajax({
        type: "POST",
        url: "/classes/",
        data:{
            'class_pk': class_pk    
        },
        dataType: "json",
        success: function(resp){
            if(clicked == false){
                curr_class.addClass("green-bg");
                curr_class.removeClass("yellow-bg");
                curr_button.data('color', 'green');

            }
            else if(clicked == true){
                curr_class.addClass("yellow-bg");
                curr_class.removeClass("green-bg");
                curr_button.data('color', 'yellow');
            }
            //alert(resp.message)
            $("#notifcation-modal").removeClass("hidden");
            $("#modal-txt").html(resp.message);
            $(".close-btn").on("click", function () {
                $("#notifcation-modal").addClass("hidden");
    });

            console.log("Passed data");
        },
        error: function(){
            console.log("Error");
        }
        
    });
    }
});