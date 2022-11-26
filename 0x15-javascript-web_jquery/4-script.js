const $textColor = $('header');
const $divRedHeader = $('div#toggle_header');

$divRedHeader.on('click', () => {
  const currentClass = $textColor.attr('class');

  if (currentClass === 'green') {
    $textColor.toggleClass(`${currentClass} red`);
  }

  if (currentClass === 'red') {
    $textColor.toggleClass(`${currentClass} green`);
  }
});
