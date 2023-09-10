const cargo_list = [];

let formSubmitted = false;
let cargoCount = 1;

const formContainer = document.getElementById("formContainer");
const addCargoButton = document.getElementById("addCargo");

function addCargoForm() {
    const newCargoForm = document.createElement("div");
    newCargoForm.setAttribute("data-cargo-id", cargoCount);
    newCargoForm.classList.add("container-form");
    newCargoForm.innerHTML = `
        <h3 >Груз ${cargoCount}</h3>
        <div class="form-group">
            <label for="length${cargoCount}">Длина</label>
            <input type="number" id="length${cargoCount}" step="1">
        </div>
        <div class="form-group">
            <label for="width${cargoCount}">Ширина</label>
            <input type="number" id="width${cargoCount}" step="1">
        </div>
        <div class="form-group">
            <label for="height${cargoCount}">Высота</label>
            <input type="number" id="height${cargoCount}" step="1">
        </div>
        <div class="form-group">
            <label for="quantity${cargoCount}">Количество</label>
            <input type="number" id="quantity${cargoCount}" step="1">
        </div>
        <div class="form-group">
            <label for="weight${cargoCount}">Вес</label>
            <input type="number" id="weight${cargoCount}" step="1">
        </div>
    `;

    cargoCount++;
    formContainer.appendChild(newCargoForm);
}

addCargoButton.addEventListener("click", addCargoForm);

/*function deleteLastCargo() {
    const lastCargoForm = document.querySelector(`[data-cargo-id="${cargoCount - 1}"]`);

    if (lastCargoForm) {
        lastCargoForm.remove();
    }
}*/

function calculateCargo() {
    if (formSubmitted) {
        return;
    }

    const cargoData = [];

    for (let i = 1; i < cargoCount; i++) {
        const length = parseInt(document.getElementById(`length${i}`).value);
        const width = parseInt(document.getElementById(`width${i}`).value);
        const height = parseInt(document.getElementById(`height${i}`).value);
        const quantity = parseInt(document.getElementById(`quantity${i}`).value);
        const weight = parseInt(document.getElementById(`weight${i}`).value);
        const name = `Груз ${i}`;

        if (isNaN(length) || isNaN(width) || isNaN(height) || isNaN(quantity) || isNaN(weight)) {
            alert(`Пожалуйста, заполните все поля для Груза ${i} корректно.`);
            return;
        } else {
            document.getElementById("calculate").addEventListener("click", function () {
                sendCargoDataToServer();
            });
        }

        const cargo = {
            name,
            length,
            width,
            height,
            quantity,
            weight
        };

        const isDuplicate = cargo_list.some(existingCargo => {
            return (
                existingCargo.name === cargo.name &&
                existingCargo.length === cargo.length &&
                existingCargo.width === cargo.width &&
                existingCargo.height === cargo.height &&
                existingCargo.quantity === cargo.quantity &&
                existingCargo.weight === cargo.weight
            );
        });

        if (!isDuplicate) {
            cargoData.push(cargo);
        }
    }
    cargo_list.push(...cargoData);
    console.log(cargo_list,  'cargo_list')
    formSubmitted = true;
}

function sendCargoDataToServer() {
    fetch('/api/v1/generator/platform', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({'cargo_list': cargo_list})
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Ошибка отправки данных на сервер');
            }
            return response.blob();
        })
        .then(blobData => {
            const url = window.URL.createObjectURL(blobData);

            const a = document.createElement('a');
            a.href = url;
            a.download = 'data.pdf';
            document.body.appendChild(a);
            a.click();

            window.URL.revokeObjectURL(url);

            formSubmitted = false;
        })
        .catch(error => {
            console.error('Произошла ошибка:', error);
        });
}

document.getElementById("calculate").addEventListener("click", calculateCargo);
