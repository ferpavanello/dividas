axios
  .get(`https://jsonplaceholder.typicode.com/users`)
  .then(response => {
    $.each(response.data, function(index, item) {
      let eachrow = `<tr onClick='window.location.href="/${item.id}"'>
                      <td data-label='Id'>${item.id}</td>
                      <td data-label='Nome'>${item.name}</td>
                    </tr>`;
      $("#tbClientes > tbody").append(eachrow);
    });
  })
  .catch(error => {
    console.log(error);
  });
