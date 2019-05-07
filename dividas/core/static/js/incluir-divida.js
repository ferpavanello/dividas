axios
  .get(`https://jsonplaceholder.typicode.com/users`)
  .then(response => {
    $("#selCliente").append(
      `<option value="" selected="selected">Selecione</option>`
    );
    $.each(response.data, function(index, item) {
      let eachrow = `<option value="${item.id}">${item.name}</option>`;
      $("#selCliente").append(eachrow);
    });
  })
  .catch(error => {
    console.log(error);
  });

function salvar() {
  event.preventDefault();

  console.log(document.getElementById("selCliente").value);

  const divida = {
    id_cliente: document.getElementById("selCliente").value,
    motivo: document.getElementById("motivo").value,
    valor: document.getElementById("valor").value,
    data: document.getElementById("data").value
  };

  axios
    .post("http://127.0.0.1:8000/dividas/", divida)
    .then(response => {
      location.href = "/";
    })
    .catch(error => {
      console.log(error);
    });
}
