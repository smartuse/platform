jQuery(function($){

  // Interactive FAQ component
  $(".faq-q").click( function () {
    var container = $(this).parents(".faq-c");
    var answer = container.find(".faq-a");
    var trigger = container.find(".faq-t");

    answer.slideToggle(200);

    if (trigger.hasClass("faq-o")) {
      trigger.removeClass("faq-o");
    }
    else {
      trigger.addClass("faq-o");
    }
  }).click();

});
