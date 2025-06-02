/**
 * ERROR MESSAGE AUTO-HIDE
 * Automatically hides error messages after 2 seconds when the page loads.
 * Improves user experience by clearing old error notifications.
 */
document.addEventListener('DOMContentLoaded', () => {
    setTimeout(() => {
        const errorMessage = document.getElementById('errorMessage');
        if (errorMessage) {
            errorMessage.style.display = 'none';
        }
    }, 2000);
});

/**
 * CAPTCHA GENERATOR
 * Creates a random 6-character CAPTCHA code using letters and numbers.
 * Updates the CAPTCHA display element with the new code.
 */
function generateCaptcha() {
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    let captcha = '';
    for (let i = 0; i < 6; i++) {
        captcha += characters.charAt(Math.floor(Math.random() * characters.length));
    }
    document.getElementById('captcha').textContent = captcha;
}

/**
 * FORM VALIDATION WITH CAPTCHA CHECK
 * Validates CAPTCHA input when login form is submitted.
 * Prevents form submission and refreshes CAPTCHA if validation fails.
 */
document.getElementById('loginForm').addEventListener('submit', function (e) {
    const captchaCode = document.getElementById('captcha').textContent;
    const captchaInput = document.getElementById('captchaInput').value;

    if (captchaInput !== captchaCode) {
        e.preventDefault();
        alert('Invalid CAPTCHA. Please try again.');
        generateCaptcha(); // Refresh CAPTCHA
    }
});

/**
 * INITIALIZATION
 * Generates initial CAPTCHA code when the page loads.
 */
window.onload = generateCaptcha;