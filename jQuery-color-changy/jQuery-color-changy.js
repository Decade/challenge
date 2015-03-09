// My First jQuery Function. Not much of a milestone.
// Just changes the color of the #main div when the #button button is pressed.
// But with a twist! If it has been less than half a second since the last color change,
// then ignore the button.
$( document ).ready(function(){
  var lasttime = new Date(),
      index = 0,
      colors = ['red','orange','yellow','green','blue','indigo','violet'];
  $( '#main' ).css('background-color',colors[index]);
  $( '#button' ).click(function(){
    var currtime = new Date();
    // Date arithmetic uses milliseconds
    if (currtime-lasttime > 500){
      index = (index + 1)%colors.length;
       $( '#main' ).css('background-color',colors[index]);
      lasttime = currtime;
    }
  });
});