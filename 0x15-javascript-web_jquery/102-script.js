$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const languageCode = $('INPUT#language_code').val();
    $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
