const $getHeader = $('header');
const $updateHeader = $('div#update_header');

$updateHeader.on('click', () => {
  $getHeader.text('New Header!!!');
});
