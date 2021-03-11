
// Default map when opening GrandPy page
let mymap = L.map('mapid').setView([48.8751155, 2.3489782], 14);
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoiaWdub3R1czExMSIsImEiOiJja2xpbmJqNHMxeHd1MnhwN3dlNTY2ZGQ0In0.0hPZ8Aamq8wrHMrOs1Wfcw', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
}).addTo(mymap);

// Takes name value from html and send it to /research
const searching = () => {
  const name = $("#name").val();

  if (name) {
    $("#name").prop('disabled', true)
    $("#target").hide()
    $("#loadbutton").show()
    $.ajax({
      url: "/research",
      type: "POST",
      data: `search=${name}`,
      success: successfunc,
      error: errorfunc,
      complete: enablebutton
    });
  }
};

//When click on html target button, calls searching function
$("#target").click(searching);
//When a key is pressed, if it it 'enter', calls searching function
$("#name").keypress((event) =>{

  const keycode = (event.keyCode ? event.keyCode : event.which);
  if(keycode == '13'){
      searching();
  }
});

//When successfunc is called, add to html chat messages, with requested place
//and its answer, then change map focus to that place
// Conv part : each time successfunc is called, give conv id to chat message,
//so the user can click this message and the map shows the corresponding place
let conv = 0
const successfunc = (data) => {
  conv += 1
  $("#chat").append("<p> Vous : " + $("#name").val() + "</p>");
  $("#chat").append(`<div id='${conv}' ><p> GrandPy Bot : Voici son adresse : ` + data.address + ".</p><p>Mais le savais-tu ? " + data.story + ".</p><p>Y aurait-il un autre lieu que tu aimerais connaître davantage ?</p></div>");
  $("#name").val('');
  $(`#${conv}`).click((event) => {
    mymap.flyTo([data.geocode_lat, data.geocode_lng])
  });

  mymap.flyTo([data.geocode_lat, data.geocode_lng])
  L.marker([data.geocode_lat, data.geocode_lng]).addTo(mymap).bindPopup(data.address).openPopup();
};

//Message html chat when errorfunc is called
const errorfunc = (result, statut, error) => {
  $("#chat").append("<p> Vous : " + $("#name").val() + "</p>");
  $("#chat").append("<p> GrandPy Bot : Oups! Il y a un petit problème : sois ta phrase est trop compliquée, sois le lieu que tu cherches n'existe pas!")
};

const enablebutton = () => {
  $("#target").show()
  $("#loadbutton").hide()
  $("#name").prop('disabled', false)

};
