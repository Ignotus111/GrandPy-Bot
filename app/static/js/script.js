let mymap = L.map('mapid').setView([51.5, 0.09], 14);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
}).addTo(mymap);

$("#target").click(() => {
  const name = $("#name").val();

  if (name) {
    $.ajax({
      url: "/recherche",
      type: "POST",
      data: `search=${name}`,
      success: mafonctionsuccess,
    });
  }
});

const mafonctionsuccess = (data, statut) => {

  $("#chat").append("<p> Vous : " + $("#name").val() + "</p>");

  $("#chat").append("<p> GrandPy Bot : " + data.address + "</p>");

  //$("#question").text("Avez-vous un autre endroit ou aller ?");

  //$("#mapid").css("display", "block")

  mymap.flyTo([data.geocode_lat, data.geocode_lng])
  L.marker([data.geocode_lat, data.geocode_lng]).addTo(mymap).bindPopup(data.address).openPopup();


  };
