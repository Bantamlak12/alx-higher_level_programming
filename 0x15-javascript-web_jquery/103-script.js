$(document).ready(function () {
  $('INPUT#btn_translate').click(performTranslation);
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      performTranslation();
    }
  });
  function performTranslation () {
    const languageCode = $('INPUT#language_code').val();
    $.getJSON(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }
});
