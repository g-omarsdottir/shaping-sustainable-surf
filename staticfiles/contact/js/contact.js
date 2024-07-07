document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('contact_form');
    const integerFields = document.querySelectorAll('input[inputmode="numeric"]');

    integerFields.forEach(field => {
        field.addEventListener('input', function () {
            if (this.value && !(/^\d*$/.test(this.value))) {
                this.setCustomValidity('Please enter only numbers for this field.');
                this.classList.add('error');
                this.value = '';
            } else {
                this.setCustomValidity('');
                this.classList.remove('error');
            }
            this.reportValidity();
        });
    });

    form.addEventListener('submit', function(event) {
        let isValid = true;
        integerFields.forEach(field => {
            if (field.value !== '' && !(/^\d+$/.test(field.value))) {
                field.setCustomValidity('Please enter only numbers for this field.');
                field.reportValidity();
                isValid = false;
            } else {
                field.setCustomValidity('');
            }
        });

        if (!isValid) {
            event.preventDefault();
        }
    });
});
