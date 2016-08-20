$(document).ready(function(){

$('.dropdown-button').dropdown({
      inDuration: 300,
      outDuration: 225,
      constrain_width: false, // Does not change width of dropdown to that of the activator
      hover: true, // Activate on hover
      gutter: 0, // Spacing from edge
      belowOrigin: true, // Displays dropdown below the button
      alignment: 'left' // Displays dropdown with edge aligned to the left of button
    }
);

$(function() {
    $('#btnSignUp').click(function() {
 
        $.ajax({
            url: '/output',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                alert("hello");
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});

$('.slider').slider({full_width: true}); 
  $('.slider').slider({height: 800}); 
  //$('.slider').slider({Interval: 800}); 
  $( "#chart_div, #chart_div1, #chart_div2,#chart_div3").mouseover(function() {
    $('.slider').slider('pause');
  });
  
  $( "#chart_div, #chart_div1, #chart_div2,#chart_div3").mouseout(function() {
    $('.slider').slider('start');
  });

  });