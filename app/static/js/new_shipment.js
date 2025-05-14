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