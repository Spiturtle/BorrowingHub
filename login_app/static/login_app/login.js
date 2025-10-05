// static/login_app/login.js

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector(".login-form");
    const usernameInput = form.querySelector("input[name='username']");
    const passwordInput = form.querySelector("input[name='password']");
    const submitBtn = form.querySelector(".login-btn");

    // Helper: show error messages below fields
    function showError(input, message) {
        removeError(input);
        const errorDiv = document.createElement("div");
        errorDiv.classList.add("login-form-errors");
        errorDiv.style.color = "#991b1b";
        errorDiv.style.fontSize = "0.9rem";
        errorDiv.style.marginTop = "4px";
        errorDiv.innerHTML = message;
        input.parentNode.appendChild(errorDiv);
        input.style.borderColor = "#ef4444";
    }

    // Helper: remove previous error messages
    function removeError(input) {
        const existingError = input.parentNode.querySelector(".login-form-errors");
        if (existingError) existingError.remove();
        input.style.borderColor = "#e5e7eb";
    }

    // Clear errors on input
    usernameInput.addEventListener("input", () => removeError(usernameInput));
    passwordInput.addEventListener("input", () => removeError(passwordInput));

    // Main form validation before submission
    form.addEventListener("submit", (e) => {
        let valid = true;

        // Clear previous errors
        [usernameInput, passwordInput].forEach(removeError);

        // Username validation
        if (usernameInput.value.trim() === "") {
            showError(usernameInput, "Username is required.");
            valid = false;
        }

        // Password validation
        if (passwordInput.value.trim() === "") {
            showError(passwordInput, "Password is required.");
            valid = false;
        }

        // If any validation failed, stop submission
        if (!valid) {
            e.preventDefault();
        }
    });

    // Add loading state to button on submit
    form.addEventListener("submit", () => {
        submitBtn.disabled = true;
        submitBtn.textContent = "Signing in...";
        
        // Re-enable after 3 seconds in case of error
        setTimeout(() => {
            submitBtn.disabled = false;
            submitBtn.textContent = "Sign In";
        }, 3000);
    });
});