
$("#target").click(() => {
  const name = $("#name").val();

  if (name) {
    $.ajax({
      url: "http://localhost:5000/recherche",
      type: "POST",
      data: 'search=${name}',
      success: mafonctionsuccess,
//      error:errorfunc,
    });
  }
});

const mafonctionsuccess = (data, statut) => {
  $("#chat").prepend("<p> GrandPy Bot : " + data + "</p>");

  $("#chat").prepend("<p> Vous : " + $("#name").val() + "</p>");

  $("#question").text("Avez-vous un autre endroit ou aller ?")
};

//const errorfunc =
