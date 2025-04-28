// Generate a random CAPTCHA code
function generateCaptcha() {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let captcha = '';
    for (let i = 0; i < 6; i++) {
        captcha += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    document.getElementById('captcha').textContent = captcha;
}

// Validate CAPTCHA on form submission
document.getElementById('loginForm').addEventListener('submit', function (e) {
    const captchaCode = document.getElementById('captcha').textContent;
    const captchaInput = document.getElementById('captchaInput').value;

    if (captchaInput !== captchaCode) {
        e.preventDefault();
        alert('Invalid CAPTCHA. Please try again.');
        generateCaptcha(); // Refresh CAPTCHA
    }
});

// Generate CAPTCHA on page load
window.onload = generateCaptcha;

// Hide the error message after 3 seconds
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        const errorMessage = document.getElementById('errorMessage');
        if (errorMessage) {
            errorMessage.style.display = 'none';
        }
    }, 2000);
});