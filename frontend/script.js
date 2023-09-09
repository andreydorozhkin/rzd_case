function showCargoFields() {
  var cargoFields = document.getElementById("cargoFields");
  cargoFields.style.display = "block";
}

function calculate() {
  var length = document.getElementById("length").value;
  var width = document.getElementById("width").value;
  var height = document.getElementById("height").value;
  var quantity = document.getElementById("quantity").value;
  var weight = document.getElementById("weight").value;
  
  // Дальнейшие расчеты с полученными данными
  var result = "Расчеты выполнены успешно";
  console.log(result);
  // Действия с полученным результатом
}