axios
  .get(`https://jsonplaceholder.typicode.com/users`)
  .then(response => {
    $.each(response.data, function(index, item) {
      let eachrow =
        "<tr>" +
        "<td data-label='Id'>" +
        item.id +
        "</td>" +
        "<td data-label='Nome'>" +
        item.name +
        "</td>" +
        "</tr>";
      $("#tbClientes > tbody").append(eachrow);
    });
  })
  .catch(error => {
    console.log(error);
  });
