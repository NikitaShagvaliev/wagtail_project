document.addEventListener('DOMContentLoaded', function() {
    const warehouseData = [
        { id: 1, name: "Товар 1", quantity: 10, status: "В наличии" },
        { id: 2, name: "Товар 2", quantity: 5, status: "В наличии" },
        { id: 3, name: "Товар 3", quantity: 0, status: "Нет в наличии" },
        { id: 4, name: "Товар 4", quantity: 20, status: "В наличии" },
        { id: 5, name: "Товар 5", quantity: 3, status: "В наличии" }
    ];

    const tableBody = document.querySelector("#warehouse-table tbody");
    const createProductForm = document.querySelector("#create-product-form");

    function renderTable() {
        tableBody.innerHTML = '';
        warehouseData.forEach(item => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${item.name}</td>
                <td>${item.quantity}</td>
                <td>${item.status}</td>
                <td>
                    <button class="update-btn" data-id="${item.id}">Обновить</button>
                    <button class="delete-btn" data-id="${item.id}">Удалить</button>
                </td>
            `;
            tableBody.appendChild(row);
        });
    }

    renderTable();

    createProductForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const productName = document.querySelector("#product-name").value;
        const productQuantity = document.querySelector("#product-quantity").value;
        const newProduct = {
            id: warehouseData.length + 1,
            name: productName,
            quantity: parseInt(productQuantity),
            status: parseInt(productQuantity) > 0 ? "В наличии" : "Нет в наличии"
        };
        warehouseData.push(newProduct);
        renderTable();
        createProductForm.reset();
    });

    tableBody.addEventListener('click', function(event) {
        if (event.target.classList.contains('delete-btn')) {
            const productId = event.target.getAttribute('data-id');
            const productIndex = warehouseData.findIndex(item => item.id == productId);
            if (productIndex !== -1) {
                warehouseData.splice(productIndex, 1);
                renderTable();
            }
        }
    });
});