var slideIndex = 0;
carousel();

function carousel() {
  var i;
  var x = document.getElementsByClassName("testimonials");
  var dots = document.getElementsByClassName("dot");

  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > x.length) {slideIndex = 1}
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  x[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";

  setTimeout(carousel, 5000); // Change image every 2 seconds
}
