const $textColor = $("header");
const $headerColor = $("div#red_header");

$headerColor.on("click", function () {
  $textColor.css("color", "#FF0000");
});
