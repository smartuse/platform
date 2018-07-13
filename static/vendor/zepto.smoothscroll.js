// ==================================================
// Smooth Scroll
// ==================================================

function smoothScroll(el, to, duration) {

  'use strict';

  if (duration < 0) {
    return;
  }
  var difference = to - el.scrollTop() - el.offset().top;
  var perTick = difference / duration * 10;

  $(this).scrollToTimerCache = setTimeout(function() {
    if (!isNaN(parseInt(perTick, 10))) {
      el[0].scrollTo(0, el.scrollTop() + perTick);
      smoothScroll(el, to, duration - 10);
    }
  }.bind(this), 10);
}

$('[data-scroll]').on('click', function(e) {
  e.preventDefault();
  smoothScroll($(window), $($(e.currentTarget).attr('href')).offset().top, 600);
});
