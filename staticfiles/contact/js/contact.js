document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contact-form');
    const integerFieldIds = ['id_board_length', 'id_board_volume', 'id_body_height', 'id_body_weight'];
    const integerFields = integerFieldIds.map(id => document.getElementById(id)).filter(Boolean);
    const messageField = document.getElementById('id_message');

    integerFields.forEach(field => {
        field.addEventListener('input', function() {
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

    if (messageField) {
        const charCount = document.createElement('div');
        charCount.id = 'char-count';
        messageField.parentNode.insertBefore(charCount, messageField.nextSibling);

        messageField.addEventListener('input', function() {
            const maxLength = 3000;
            const remaining = maxLength - this.value.length;
            charCount.textContent = `${remaining} characters remaining`;

            if (remaining < 0) {
                charCount.style.color = 'red';
                this.setCustomValidity(`Message must be ${maxLength} characters or less.`);
                this.classList.add('error');
            } else {
                charCount.style.color = '';
                this.setCustomValidity('');
                this.classList.remove('error');
            }
            this.reportValidity();
        });
    }

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
        if (messageField && messageField.value.length > 3000) {
            messageField.setCustomValidity('Message must be 3000 characters or less.');
            messageField.reportValidity();
            isValid = false;
        }
        if (!isValid) {
            event.preventDefault();
        }
    });
});
