// static/registration_app/registration.js

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".register-form");
    const emailInput = form.querySelector("input[name='email']");
    const usernameInput = form.querySelector("input[name='username']");
    const password1Input = form.querySelector("input[name='password1']");
    const password2Input = form.querySelector("input[name='password2']");
    const submitBtn = form.querySelector(".register-btn");

    // Helper: show error messages below fields
    function showError(input, message) {
        removeError(input); // clear existing error first
        const errorDiv = document.createElement("div");
        errorDiv.classList.add("register-form-errors");
        errorDiv.innerHTML = `<ul><li>${message}</li></ul>`;
        input.parentNode.appendChild(errorDiv);
        input.classList.add("register-error-input");
    }

    // Helper: remove previous error messages
    function removeError(input) {
        const existingError = input.parentNode.querySelector(".register-form-errors");
        if (existingError) existingError.remove();
        input.classList.remove("register-error-input");
    }

    // Validate email format
    function validateEmail(email) {
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(email);
    }

    // Validate password strength (minimum 8 chars)
    function validatePasswordStrength(password) {
        return password.length >= 8;
    }

    // Main form validation before submission
    form.addEventListener("submit", (e) => {
        let valid = true;

        // Clear previous errors
        [emailInput, usernameInput, password1Input, password2Input].forEach(removeError);

        // Email validation
        if (emailInput.value.trim() === "") {
            showError(emailInput, "Email is required.");
            valid = false;
        } else if (!validateEmail(emailInput.value.trim())) {
            showError(emailInput, "Enter a valid email address.");
            valid = false;
        }

        // Username validation
        if (usernameInput.value.trim() === "") {
            showError(usernameInput, "Username is required.");
            valid = false;
        } else if (usernameInput.value.trim().length < 4) {
            showError(usernameInput, "Username must be at least 4 characters long.");
            valid = false;
        }

        // Password validation
        if (password1Input.value.trim() === "") {
            showError(password1Input, "Password is required.");
            valid = false;
        } else if (!validatePasswordStrength(password1Input.value.trim())) {
            showError(password1Input, "Password must be at least 8 characters long.");
            valid = false;
        }

        // Confirm password match
        if (password2Input.value.trim() === "") {
            showError(password2Input, "Please confirm your password.");
            valid = false;
        } else if (password1Input.value.trim() !== password2Input.value.trim()) {
            showError(password2Input, "Passwords do not match.");
            valid = false;
        }

        // If any validation failed, stop submission
        if (!valid) {
            e.preventDefault();
        }
    });

    // Optional: Live password match indicator
    password2Input.addEventListener("input", () => {
        removeError(password2Input);
        if (password1Input.value && password1Input.value !== password2Input.value) {
            showError(password2Input, "Passwords do not match.");
        }
    });
});
