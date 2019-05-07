axios
  .get(`http://127.0.0.1:8000/dividas/`)
  .then(response => {
    $.each(response.data, function(index, item) {
      let eachrow = `<tr>
                      <td data-label="Id">${item.id}</td>
                      <td data-label="Cliente">${item.id_cliente}</td>
                      <td data-label="Motivo">${item.motivo}</td>
                      <td data-label="Data">${item.data}</td>
                      <td data-label="Valor" class="text-right">${valueFormat(
                        item.valor
                      )}</td>
                      <td data-label="Alterar" class="text-center">
                        <a
                          href="/alterar/${item.id}"
                          title="Alterar"
                        >
                          <i class="fas fa-edit"></i>
                        </a>
                      </td>
                      <td data-label="Deletar" class="text-center">
                        <a
                          onClick=deletar(${item.id})
                          href="#"
                          title="Deletar"
                        >
                          <i class="fas fa-trash-alt"></i>
                        </a>
                      </td>
                    </tr>`;
      $("#tbDividas > tbody").append(eachrow);
    });
  })
  .catch(error => {
    console.log(error);
  });

function deletar(id) {
  axios
    .delete(`http://127.0.0.1:8000/dividas/${id}/`)
    .then(response => {
      window.location.reload();
    })
    .catch(error => {
      console.log(error);
    });
}

function valueFormat(value) {
  return parseFloat(value).toLocaleString("pt-BR", {
    style: "currency",
    currency: "BRL"
  });
}
