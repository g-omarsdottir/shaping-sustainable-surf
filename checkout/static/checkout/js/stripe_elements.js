/*
    Core JavaScript functunalities from stripe:
    https://stripe.com/docs/payments/accept-a-payment

    Core CSS style from stripe: 
    https://stripe.com/docs/stripe-js
*/

document.addEventListener('DOMContentLoaded', function () {
    var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
    var clientSecret = $('#id_client_secret').text().slice(1, -1);
    var stripe = Stripe(stripePublicKey);
    console.log('Stripe object created:', stripe);

    var elements = stripe.elements();
    console.log('Elements object created:', elements);
    
    var style = {
        base: {
            color: '#000',
            fontFamily: '"Roboto Flex", sans-serif',
            fontSmoothing: 'antialiased',
            fontSize: '16px',
            '::placeholder': {
                color: '#aab7c4'
            }
        },
        invalid: {
            color: '#dc3545',
            iconColor: '#dc3545'
        }
    };
    
    var card = elements.create('card', {
        style: style
    });

    console.log('Card element container:', document.getElementById('card-element'));
    card.mount('#card-element');
    console.log('Card element mounted');
    console.log('Stripe Public Key:', stripePublicKey);

    // Event listener for changes to the card element
    card.on('change', function(event) {
        console.log('Card change event:', event);
        var displayError = document.getElementById('card-errors');
        if (event.error) {
            displayError.textContent = event.error.message;
        } else {
            displayError.textContent = '';
        }
    });

    card.on('ready', function(event) {
        console.log('Card element is ready');
    });

});

var form = document.getElementById('payment-form');
