const idLink = location.href.split("/").pop();

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

    carregaValores();
  })
  .catch(error => {
    console.log(error);
  });

function carregaValores() {
  axios
    .get(`http://127.0.0.1:8000/dividas/${idLink}`)
    .then(response => {
      document.getElementById("selCliente").value = response.data.id_cliente;
      document.getElementById("motivo").value = response.data.motivo;
      document.getElementById("valor").value = response.data.valor;
      document.getElementById("data").value = response.data.data;
    })
    .catch(error => {
      console.log(error);
    });
}

function salvar() {
  event.preventDefault();

  const divida = {
    id: idLink,
    id_cliente: document.getElementById("selCliente").value,
    motivo: document.getElementById("motivo").value,
    valor: document.getElementById("valor").value,
    data: document.getElementById("data").value
  };

  axios
    .put(`http://127.0.0.1:8000/dividas/${idLink}/`, divida)
    .then(response => {
      location.href = "/";
    })
    .catch(error => {
      console.log(error);
    });
}
