axios
  .get(`https://jsonplaceholder.typicode.com/users`)
  .then(response => {
    $.each(response.data, function(index, item) {
      let eachrow = `<tr onClick=dividasCliente()'>
                      <td data-label='Id'>${item.id}</td>
                      <td data-label='Nome'>${item.name}</td>
                    </tr>`;
      $("#tbClientes > tbody").append(eachrow);
    });
  })
  .catch(error => {
    console.log(error);
  });

function dividasCliente() {
  axios
    .get(`http://127.0.0.1:8000/dividas/`)
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
