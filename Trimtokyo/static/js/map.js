let map, directionsService, directionsRenderer;
let serviceLocations = {
  "Haircut": [
    { name: "Salon A", location: { lat: 28.6139, lng: 77.2090 } },
    { name: "Salon B", location: { lat: 28.6200, lng: 77.2200 } },
    { name: "Salon C", location: { lat: 28.6300, lng: 77.2150 } }
  ],
  "Shaving": [
    { name: "Shave Point 1", location: { lat: 28.6100, lng: 77.2100 } },
    { name: "Shave Point 2", location: { lat: 28.6150, lng: 77.2250 } }
  ],
  "Hair Coloring": [
    { name: "Color Hub 1", location: { lat: 28.6180, lng: 77.2130 } },
    { name: "Color Hub 2", location: { lat: 28.6190, lng: 77.2180 } }
  ]
};

function initMap() {
  const serviceName = localStorage.getItem("selectedService") || "Haircut";
  document.getElementById("serviceTitle").innerText = `Available: ${serviceName}`;

  navigator.geolocation.getCurrentPosition(position => {
    const userLocation = {
      lat: position.coords.latitude,
      lng: position.coords.longitude
    };

    map = new google.maps.Map(document.getElementById("map"), {
      center: userLocation,
      zoom: 13
    });

    new google.maps.Marker({
      position: userLocation,
      map: map,
      title: "Your Location",
      icon: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png"
    });

    directionsService = new google.maps.DirectionsService();
    directionsRenderer = new google.maps.DirectionsRenderer({ map });

    const locations = serviceLocations[serviceName] || [];

    locations.forEach(loc => {
      const marker = new google.maps.Marker({
        position: loc.location,
        map,
        title: loc.name
      });

      marker.addListener("click", () => {
        showRoute(userLocation, loc.location);
      });
    });

  }, () => {
    alert("Please allow location access to use this feature.");
  });
}

function showRoute(origin, destination) {
  directionsService.route({
    origin,
    destination,
    travelMode: google.maps.TravelMode.DRIVING
  }, (result, status) => {
    if (status === "OK") {
      directionsRenderer.setDirections(result);
    } else {
      alert("Failed to get directions: " + status);
    }
  });
}
