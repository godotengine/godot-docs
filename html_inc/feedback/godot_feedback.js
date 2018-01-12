$(document).ready(function() {
	$('footer').prepend(
		'<div class="godot-feedback">' +
			'Is this page helpful? ' +
				'<a id="gf-yes">Yes</a> ' +
				'<a id="gf-no" target="_blank">No</a>' +
		'</div>');
	
	var title = $('title').text();
	title = '[FEEDBACK] ' + title;
	
	var yes_body = 'You folks are great!  Keep up the good work!';
	$('#gf-yes').attr('href',
		'mailto:docfeedback@godotengine.org' +
			'?subject=' + encodeURIComponent(title) +
			'&body=' + encodeURIComponent(yes_body));
	
	var no_body = 'When I do `$this`, it doesn\'t `$work`!';
	$('#gf-no').attr('href', 
		'https://github.com/godotengine/godot-docs/issues/new' +
			'?title=' + encodeURIComponent(title) +
			'&body=' + encodeURIComponent(no_body));
});
