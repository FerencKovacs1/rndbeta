// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the myTopnav
var myTopnav = document.getElementById("myTopnav");

// Get the offset position of the myTopnav
var sticky = myTopnav.offsetTop;

// Add the sticky class to the myTopnav when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    myTopnav.classList.add("sticky")
  } else {
    myTopnav.classList.remove("sticky");
  }
}

// ===== Scroll to Top ====
$(window).scroll(function() {
    if ($(this).scrollTop() >= 50) {        // If page is scrolled more than 50px
        $('#return-to-top').fadeIn(200);    // Fade in the arrow
    } else {
        $('#return-to-top').fadeOut(200);   // Else fade out the arrow
    }
});
$('#return-to-top').click(function() {      // When arrow is clicked
    $('body,html').animate({
        scrollTop : 0                       // Scroll to top of body
    }, 500);
});
