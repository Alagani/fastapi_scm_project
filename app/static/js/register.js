// Wait for the DOM to load
document.addEventListener("DOMContentLoaded", function () {
    // Select the alert message
    const alertMessage = document.querySelector(".alert");
    if (alertMessage) {
        // Set a timeout to hide the alert after 3 seconds
        setTimeout(() => {
            alertMessage.style.display = "none";
        }, 3000);
    }
});