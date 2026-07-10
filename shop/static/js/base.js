document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("signup-form");
    const errorBox = document.getElementById("error-message");

    form.addEventListener("submit", function (event) {

        errorBox.classList.remove("show");
        errorBox.textContent = "";

        const phone = document.getElementById("id_phone").value.trim();
        const password = document.getElementById("id_password").value;

        const phoneRegex = /^09\d{9}$/;

        if (!phoneRegex.test(phone)) {
            errorBox.textContent = "Phone number must start with 09 and be exactly 11 digits.";
            errorBox.classList.add("show");
            event.preventDefault();
            return;
        }

        if (password.length < 6) {
            errorBox.textContent = "Password must be at least 6 characters long.";
            errorBox.classList.add("show");
            event.preventDefault();
            return;
        }
    });
});