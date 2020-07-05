// Initialize and add the map
var map;
//Depending on the wait time, it returns different color
function getIconForLine(value) {
    if (value >= 90) {
        return "http://maps.google.com/mapfiles/ms/micons/red-dot.png";
    } else if (value >= 60 && value < 89) {
        return "http://maps.google.com/mapfiles/ms/micons/orange-dot.png";
    } else if (value >= 1 && value < 60) {
        return "http://maps.google.com/mapfiles/ms/micons/green-dot.png";
    } else if (value === 0) {
        return "http://maps.google.com/mapfiles/ms/micons/man.png";
    }
}

function initMapF() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: {
            lat: 43.783721,
            lng: -79.395882
        },
        zoom: 12
    });
    
    var data = {{hospitals|tojson}};

    for (var o of data) {
        var latitude = parseFloat(o.latitude);
        var longtitude = parseFloat(o.longtitude);
        var latLng = new google.maps.LatLng(latitude, longtitude);
        var url;
        var marker = new google.maps.Marker({
            map: map,
            position: latLng,
            label: o.name,
            icon: getIconForLine(70),
            clickable: true
        });
    }    
}

// Create the script tag, set the appropriate attributes
var script = document.createElement('script');
script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyDfE1q6TqgofF8Ywx_tM_Vb7vrziRl6THs&callback=initMap';
script.defer = true;
script.async = true;

// Attach your callback function to the `window` object
window.initMap = function() {
    console.log("kjwke");
    
    map = new google.maps.Map(document.getElementById("map"), {
        center: {
            lat: 43.783721,
            lng: -79.395882
        },
        zoom: 12
    });
};
// window.initMap = initMapF;

// Append the 'script' element to 'head'
document.head.appendChild(script);
      

// <script async defer
//     src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDfE1q6TqgofF8Ywx_tM_Vb7vrziRl6THs&callback=initMap">
// </script>