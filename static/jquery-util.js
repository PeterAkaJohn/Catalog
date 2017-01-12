$(document).ready(function() {
      $('.flash').delay(2000).fadeOut(1000);
});

$(window).scroll(function() {
    if ($(this).scrollTop() >= 60) { // this refers to window
        $("nav").addClass("navbar-scrolled");
    }

    if ($(this).scrollTop() <=0) {
      $("nav").removeClass("navbar-scrolled");
    }
});
