// Adjust color of the country input field to style like other placeholders
$(document).ready(function() {
    let countrySelected = $('#id_default_country').val();
    if (!countrySelected) {
        $('#id_default_country').css('color', '#aab7c4');
    }
    $('#id_default_country').change(function() {
        countrySelected = $(this).val();
        if (!countrySelected) {
            $(this).css('color', '#aab7c4');
        } else {
            $(this).css('color', '#000');
        }
    });
});

// Additional validation for email field for improved UX
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('profile-update-form');
    const emailField = document.getElementById('id_email');
    const originalEmail = form.getAttribute('data-user-email');

    // Function to restore original email
    function restoreOriginalEmail() {
        if (!emailField.value.trim()) {
            emailField.value = originalEmail;
            emailField.setCustomValidity('');
            emailField.classList.remove('error');
        }
    }

    // Function to validate email
    function validateEmail() {
        if (!emailField.value.trim()) {
            // If email field is empty, restore original and display error
            restoreOriginalEmail();
            emailField.setCustomValidity('Email field cannot be empty. Your current email has been restored.');
            emailField.classList.add('error');
            emailField.reportValidity();
            
            // Add timeout delay before removing the error state
            setTimeout(() => {
                emailField.setCustomValidity('');
                emailField.classList.remove('error');
            }, 2000); // 2 seconds delay
            return false;
        } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailField.value)) {
            // If email is invalid, display error
            emailField.setCustomValidity('Please enter a valid email address.');
            emailField.classList.add('error');
            emailField.reportValidity();
            return false;
        } else {
            // If email is valid, clear any errors
            emailField.setCustomValidity('');
            emailField.classList.remove('error');
            return true;
        }
    }

    // Add event listeners
    emailField.addEventListener('blur', restoreOriginalEmail);

    form.addEventListener('submit', function(event) {
        // Prevent default submission
        event.preventDefault();

        const isEmailValid = validateEmail();

        if (isEmailValid) {
            this.submit();
        }
    });
});
