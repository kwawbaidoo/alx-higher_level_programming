const $appendList = $ ('ul.my_list');
const $addList = $('div#add_item');
$addList.on('click,() => {
	$appendList.append('<li>Item</li>');
});
