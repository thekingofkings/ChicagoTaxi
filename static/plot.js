google.maps.event.addDomListener( window, 'load', initialize );

CA = {};

function initialize() {
	var mapOptions = {
		center: new google.maps.LatLng( 41.881977, -87.697863 ),
		zoom: 12
	};
	map = new google.maps.Map(document.getElementById("map-canvas"),
			mapOptions);
	//google.maps.event.addListener(map, 'click', mouseClick);
	
}



function plotCAs() {
	$.ajax({
		type: 'get',
		url: 'getCAs',
		datatype: 'json',
		success: function( data ){
			for (var k in data) {
				CA[k] = data[k];
				plotCA(k, CA[k]);
			}
			return data;
		}
	});
}


function plotCA(k, seq) {
	var coords = [];
	for (var i = 0; i < seq.length; i++){
		var p = new google.maps.LatLng(seq[i][1], seq[i][0]);
		coords.push(p);
	}
	var ca = new google.maps.Polygon({
		paths: coords,
		geodesic: false,
		strokeColor: '#0000FF',
		strokeOpacity: 1.0,
		strokeWeight: 2,
		fillColor: '#0000FF',
		fillOpacity: 0.1,
		editable: false,
		map: map,
		visible: true
	});
	
	ca.id = k;
	ca.bound = seq;
	
	google.maps.event.addListener(ca, 'mouseover', highlightCA);
	google.maps.event.addListener(ca, 'mouseout', dehighlightCA);
}



function highlightCA( event ) {
	this.setOptions( {'fillOpacity': 0.9} );
	message( 'ID: ' + this.id + '    #coords: ' + this.bound.length );
	$('#'+this.id).css('background-color', '#90EE90');
}


function dehighlightCA( event ) {
	this.setOptions( {'fillOpacity': 0.15 } );
	message( '' );
	$('#'+this.id).css('background-color', '#D8BFD8');
}


function message( content )
{
	$('#line').html( content )
}

