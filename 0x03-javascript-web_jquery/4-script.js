$("div#toggle_header").click(function() {
  if ($("header").hasClass("red")) {
      $("header").removeClass("red")
      $("header").addClass("green")
  }
  else {
      $("header").removeClass("green")
      $("header").addClass("red")
  }
})
// always either green or red, changing on div click
