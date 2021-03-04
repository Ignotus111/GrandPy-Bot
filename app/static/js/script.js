let mymap = L.map('mapid').setView([48.8751155, 2.3489782], 14);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
}).addTo(mymap);

let conv = 0

const searching = () => {
  const name = $("#name").val();

  if (name) {
    $.ajax({
      url: "/recherche",
      type: "POST",
      data: `search=${name}`,
      success: successfunc,
      error: errorfunc
    });
  }
};

$("#target").click(searching);
$("#name").keypress(function(event){
  var keycode = (event.keyCode ? event.keyCode : event.which);
  if(keycode == '13'){
      searching();
  }
});

const successfunc = (data, statut) => {
  conv += 1
  $("#chat").append("<p> Vous : " + $("#name").val() + "</p>");
  $("#chat").append("<p> GrandPy Bot : Voici son adresse : " + data.address + ".</p><p>Mais le savais-tu ? " + data.histoire + ".</p><p>Y aurait-il un autre lieu que tu aimerais connaître davantage ?</p>");
  $("#name").val('');
  mymap.flyTo([data.geocode_lat, data.geocode_lng])
  L.marker([data.geocode_lat, data.geocode_lng]).addTo(mymap).bindPopup(data.address).openPopup();
};

const errorfunc = (result, statut, error) => {
  $("#chat").append("<p> Vous : " + $("#name").val() + "</p>");
  $("#chat").append("<p> GrandPy Bot : Oups! Il y a un petit problème : sois ta phrase est trop compliquée, sois le lieux que tu cherches n'existe pas!")
};
