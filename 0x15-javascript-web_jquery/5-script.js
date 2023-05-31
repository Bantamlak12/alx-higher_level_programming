$(document).ready(function () {
  $('DIV#add_item').click(function () {
    const listItem = '<li>Item</li>';
    $('UL.my_list').append(listItem);
  });
});
