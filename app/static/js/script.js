
$("#target").click(() => {
  const name = $("#name").val();

  if (name) {
    $.ajax({
      url: "http://localhost:5000/recherche",
      type: "POST",
      data: `search=${name}`,
      success: mafonctionsuccess,
    });
  }
});

const mafonctionsuccess = (data, statut) => {
  $("#chat").prepend("<p> GrandPy Bot : " + data.geocode + "</p>");

  $("#chat").prepend("<p> Vous : " + $("#name").val() + "</p>");

  $("#question").text("Avez-vous un autre endroit ou aller ?")


  };


//link https://maps.googleapis.com/maps/api/staticmap?center=Brooklyn+Bridge,New+York,NY&zoom=13&size=600x300&maptype=roadmap
//&markers=color:blue%7Clabel:S%7C40.702147,-74.015794
//&key=AIzaSyC9AQ4HpPaEmS10krYP7j3rSChGsnOAYrU
