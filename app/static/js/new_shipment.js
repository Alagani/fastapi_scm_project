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