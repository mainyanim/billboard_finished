$("#form_comment" ).hide();
$("#buttons_container").hide();

$("#new_comment" ).click(function() {
  $("#form_comment" ).show();
  $("#buttons_container").show();
  $("#new_comment").hide();
  $("#button_area").hide();
});

$("#close_form").click(function() {
  $("#form_comment").hide();
  $("#buttons_container").hide();
  $("#new_comment").show();
  $("#button_area").show();
})

// $("#add_comment").click(function(){
// $("#hello_title").hide();
// })
