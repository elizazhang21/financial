// extra javascript

$(document).ready(function() {
	// $('select').material_select();
	$(".select2-selection--single").select2();
	$(".select2-selection--multiple").select2();

	// covered only
	queryPairs = window.location.search.substring(1).split('&');
	queryJSON = {};
	$.each(queryPairs, function() { 
		queryJSON[this.split('=')[0]] = this.split('=')[1]; 
	});
	
	if(queryJSON['covered_only'] == "false") {		
		$("#covered").prop('checked', false);
	}
	else {
		$("#covered").prop('checked', true);
	}
	
	$('#covered').click( function()  {
    	window.location.search = "?covered_only=" + document.getElementById("covered").checked;
    })

});

function submit_selection() {
	console.log(window.location.search)
	window.location.search = "?covered_only=" + document.getElementById("covered").checked +
							 "&actual_id=" + $('#tickers').val()
	console.log(window.location.search)
	
	if($('#slider-snap-lower')[0] != undefined) {
		window.location.search = "?covered_only=" + document.getElementById("covered").checked +
							 	 "&actual_id=" + $('#tickers').val() +
							 	 "&dates_lower=" + $('#slider-snap-lower')[0].innerHTML + 
								 "&dates_upper=" + $('#slider-snap-upper')[0].innerHTML;
	} 				 
}
