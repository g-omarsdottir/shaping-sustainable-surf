// Client-side validation for improved UX
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('subscriber-form');
    const emailField = document.getElementById('id_email');
    const termsCheckbox = document.getElementById('id_accepted_terms');

    // Function to clear the form and remove error states
    function clearForm() {
        form.reset(); // This clears all form fields
        emailField.value = ''; // Explicitly clear email field
        termsCheckbox.checked = false; // Uncheck the terms checkbox
        clearErrors();
    }

    // Function to clear errors
    function clearErrors() {
        emailField.setCustomValidity('');
        emailField.classList.remove('error');
        termsCheckbox.setCustomValidity('');
        termsCheckbox.classList.remove('error');
        // Clear any Django form errors
        const errorElements = form.querySelectorAll('.errorlist');
        errorElements.forEach(el => el.remove());
    }

    // Clear form on page load and browser refresh
    clearForm();

    // Function to clean email address
    function cleanEmail(email) {
        return email.toLowerCase().trim();
    }

    // Add event listener for email input focus
    emailField.addEventListener('focus', clearErrors);

    // Add event listener for email input
    emailField.addEventListener('input', function() {
        const cleanedEmail = cleanEmail(this.value);
        this.value = cleanedEmail;
    });

    // Add event listener for accepted terms checkbox
    termsCheckbox.addEventListener('change', clearErrors);

    // Add event listener for form submission
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        clearErrors();
        
        // Clean email address
        const cleanedEmail = cleanEmail(emailField.value);
        emailField.value = cleanedEmail;

        let isValid = true;

        // Check if email is valid
        if (!cleanedEmail || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(cleanedEmail)) {
            emailField.setCustomValidity('Please enter a valid email address.');
            emailField.classList.add('error');
            isValid = false;
        }

        // Check if terms are accepted
        if (!termsCheckbox.checked) {
            termsCheckbox.setCustomValidity('You must accept the terms.');
            termsCheckbox.classList.add('error');
            isValid = false;
        }

        // If form is valid, submit it
        if (isValid) {
            form.submit();
        } else {
            // Display errors
            emailField.reportValidity();
            termsCheckbox.reportValidity();
        }
    });
});
