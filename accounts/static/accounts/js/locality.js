// This example adds a search box to a map, using the
// Google Places autocomplete feature. People can enter geographical searches.
// The search box will return a pick list containing
// a mix of places and predicted search terms.

function initialize() {

  var markers = [];
  var map = new google.maps.Map(document.getElementById('map-canvas'), {
    mapTypeId: google.maps.MapTypeId.ROADMAP
  });

  var defaultBounds = new google.maps.LatLngBounds(
      new google.maps.LatLng(13.03767, 80.26028),
      new google.maps.LatLng(13.23767, 80.46028));
  map.fitBounds(defaultBounds);

  $("select#target").change(function(){ 
	  
	    var latLngString = $(this).val();
	    var latLngArray = latLngString.split(",");
	    var latLng = new google.maps.LatLng(latLngArray[0], latLngArray[1]);
	    map.panTo(latLng);    
	});
}

google.maps.event.addDomListener(window, 'load', initialize);