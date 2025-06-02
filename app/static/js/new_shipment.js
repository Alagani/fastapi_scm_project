// Automatically hide error and success messages after 3 seconds
setTimeout(() => {
    const errorMessage = document.getElementById('error-message');
    const successMessage = document.getElementById('success-message');
    if (errorMessage) {
        errorMessage.style.display = 'none';
    }
    if (successMessage) {
        successMessage.style.display = 'none';
    }
}, 3000);

document.addEventListener('DOMContentLoaded', function() {
    const dateInput = document.getElementById('expectedDeliveryDate');
    const today = new Date().toISOString().split('T')[0];
    dateInput.setAttribute('min', today);
    
    
});
document.addEventListener('DOMContentLoaded', function () {
    const fields = [
        { id: 'shipmentNumber', length: 7 },
        { id: 'device_id', length: 4 },
        { id: 'poNumber', length: 5 },
        { id: 'ndcNumber', length: 3 },
        { id: 'goods_number', length: 4 },
        { id: 'containerNumber', length: 7 },
        { id: 'deliveryNumber', length: 6 },
        { id: 'batchNumber', length: 5 }
    ];

    fields.forEach(field => {
        const inputElement = document.getElementById(field.id);
        if (!inputElement) return;

        inputElement.addEventListener('input', function () {
            if (this.value.length > field.length) {
                this.value = this.value.slice(0, field.length);
            }
        });
    });

    const form = document.querySelector('form[action="/new_shipment"]');
    form.addEventListener('submit', function (event) {
        let formIsValid = true;
        let firstInvalidField = null;

        fields.forEach(field => {
            const inputElement = document.getElementById(field.id);
            if (!inputElement) return;

            if (inputElement.value.length !== field.length) {
                formIsValid = false;
                if (!firstInvalidField) {
                    firstInvalidField = inputElement;
                }
            }
        });

        if (!formIsValid) {
            event.preventDefault();
            if (firstInvalidField) {
                firstInvalidField.focus();
            }
        }
    });
});