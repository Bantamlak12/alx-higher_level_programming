// `$(document).ready(function()`Ensures that the script runs after the
// document is fully loaded.
$(document).ready(function () {
  $('DIV#toggle_header').click(function () {
    const header = $('header');
    if (header.hasClass('red')) {
      header.removeClass('red');
      header.addClass('green');
    } else {
      header.removeClass('green');
      header.addClass('red');
    }
  });
});
