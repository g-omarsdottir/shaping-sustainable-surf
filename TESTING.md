# ![logo](/documentation/logo_wave.png) Testing Documentation for Shaping Sustainable Surf

This document outlines the testing procedures and results for the ecommerce project Shaping Sustainable Surf.

For development documentation, please refer to the [README.md](README.md).

View the live project [here](https://shaping-sustainable-surf-8794b08a1b3a.herokuapp.com/).<br>  
*(To open in a new window, press "ctrl" (or ⌘ for Mac) + click on the link)*

## Overview

Thorough and continuous testing was performed throughout the development process to ensure:
- Seamless functionality of the code
- Adherence to official standards and guidelines
- Optimal user experience across various devices and browsers

## Table of Contents

- [Automated Testing](#automated-testing)
    - [Python Validation](#python)
    - [JavaScript Validation](#javascript)
    - [HTML Validation](#html)
    - [CSS Validation](#css)
- [Performance Testing Google Lighthouse](#performance-testing)
- [Accessibility Testing](#accessibility-testing)
    - [WAVE Web Accessibility Evaluation Tool](#wave-web-accessibility-evaluation-tool)
    - [Coolors Contrast Checker](#coolors-contrast-checker)
- [Manual Testing](#manual-testing)
- [Security Testing](#security-testing)
- [User Story Testing](#user-story-testing)
- [Responsiveness Testing](#responsiveness-testing)
- [Browser Compatibility](#browser-compatibility)
- [Bugs](#bugs)
    - [Known Bugs](#known-bugs)
    - [Resolved Bugs](#resolved-bugs)
- [Programs Used](#programs-used)

## Automated Testing

This section covers the automated tests performed on the project's code. It includes validation of Python, JavaScript, HTML, and CSS using industry-standard tools to ensure code quality and adherence to best practices.

### Python

[Python Linter Validator](https://pep8ci.herokuapp.com/) provided by the Code Institute according to the PEP 8 style guide was used for validating the Python code throughout the development process.<br>

The webhooks.py file raises two issue with the linter due to the line lenght exceeding the maximum line length of 79 characters. Strictly adhering to the guideline here causes issues in code performance and all orders are created in webhooks as a consequence. The issue raised by the linter is not considered a quality issue and is therefore ignored.<br>

| App      | File        | Screenshot                                                                                                                   | Result |
|----------|-------------|------------------------------------------------------------------------------------------------------------------------------|--------|
| checkout | webhooks.py | <details> <summary>**Click to View**</summary> ![checkout-webhooks](/documentation/validator/checkout-webhooks.png)</details> | noqa   |


The Django’s Allauth templates do not pass through the linter because Django templates have their own style requirements to ensure proper rendering and translation of the templates and do not follow the PEP 8 guidelines. Thus, these are not included in the linter validation.<br>

All other custom written Python code files passed through the Python Linter Validator according to the PEP 8 style without issues and passed all checks. This ensures the code adheres to PEP 8 guidelines.

| App                 | File               | Screenshot                                                                                                                                 | Result |
|---------------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------|--------|
| about               | admin.py           | <details> <summary>**Click to View**</summary> ![about-admin](/documentation/validator/about-admin.png)</details>                           | Passed |
| about               | models.py          | <details> <summary>**Click to View**</summary> ![about-models](/documentation/validator/about-models.png)</details>                         | Passed |
| about               | urls.py            | <details> <summary>**Click to View**</summary> ![about-urls](/documentation/validator/about-urls.png)</details>                             | Passed |
| about               | views.py           | <details> <summary>**Click to View**</summary> ![about-views](/documentation/validator/about-views.png)</details>                           | Passed |
|                     |                    |                                                                                                                                            |        |
| cart                | admin.py           | <details> <summary>**Click to View**</summary> ![cart-admin](/documentation/validator/cart-admin.png)</details>                             | Passed |
| cart                | context.py         | <details> <summary>**Click to View**</summary> ![cart-context](/documentation/validator/cart-context.png)</details>                         | Passed |
| cart                | forms.py           | <details> <summary>**Click to View**</summary> ![cart-forms](/documentation/validator/cart-forms.png)</details>                             | Passed |
| cart                | models.py          | <details> <summary>**Click to View**</summary> ![cart-models](/documentation/validator/cart-models.png)</details>                           | Passed |
| cart                | urls.py            | <details> <summary>**Click to View**</summary> ![cart-urls](/documentation/validator/cart-urls.png)</details>                               | Passed |
| cart                | views.py           | <details> <summary>**Click to View**</summary> ![cart-views](/documentation/validator/cart-views.png)</details>                             | Passed |
|                     |                    |                                                                                                                                            |        |
| checkout            | admin.py           | <details> <summary>**Click to View**</summary> ![checkout-admin](/documentation/validator/checkout-admin.png)</details>                     | Passed |
| checkout            | forms.py           | <details> <summary>**Click to View**</summary> ![checkout-forms](/documentation/validator/checkout-forms.png)</details>                     | Passed |
| checkout            | models.py          | <details> <summary>**Click to View**</summary> ![checkout-models](/documentation/validator/checkout-models.png)</details>                   | Passed |
| checkout            | signals.py         | <details> <summary>**Click to View**</summary> ![checkout-signals](/documentation/validator/checkout-signals.png)</details>                 | Passed |
| checkout            | urls.py            | <details> <summary>**Click to View**</summary> ![checkout-urls](/documentation/validator/checkout-urls.png)</details>                       | Passed |
| checkout            | views.py           | <details> <summary>**Click to View**</summary> ![checkout-views](/documentation/validator/checkout-views.png)</details>                     | Passed |
| checkout            | webhook handler.py | <details> <summary>**Click to View**</summary> ![checkout-webhook-handler](/documentation/validator/checkout-webhook-handler.png)</details> | Passed |
|                     |                    |                                                                                                                                            |        |
| contact             | admin.py           | <details> <summary>**Click to View**</summary> ![contact-admin](/documentation/validator/contact-admin.png)</details>                       | Passed |
| contact             | forms.py           | <details> <summary>**Click to View**</summary> ![contact-forms](/documentation/validator/contact-forms.png)</details>                       | Passed |
| contact             | models.py          | <details> <summary>**Click to View**</summary> ![contact-models](/documentation/validator/contact-models.png)</details>                     | Passed |
| contact             | urls.py            | <details> <summary>**Click to View**</summary> ![contact-urls](/documentation/validator/contact-urls.png)</details>                         | Passed |
| contact             | views.py           | <details> <summary>**Click to View**</summary> ![contact-views](/documentation/validator/contact-views.png)</details>                       | Passed |
|                     |                    |                                                                                                                                            |        |
| home                | urls.py            | <details> <summary>**Click to View**</summary> ![home-urls](/documentation/validator/home-urls.png)</details>                               | Passed |
| home                | views.py           | <details> <summary>**Click to View**</summary> ![home-views](/documentation/validator/home-views.png)</details>                             | Passed |
|                     |                    |                                                                                                                                            |        |
| newsletter          | admin.py           | <details> <summary>**Click to View**</summary> ![newsletter-admin](/documentation/validator/newsletter-admin.png)</details>                 | Passed |
| newsletter          | forms.py           | <details> <summary>**Click to View**</summary> ![newsletter-forms](/documentation/validator/newsletter-forms.png)</details>                 | Passed |
| newsletter          | models.py          | <details> <summary>**Click to View**</summary> ![newsletter-models](/documentation/validator/newsletter-models.png)</details>               | Passed |
| newsletter          | signals.py         | <details> <summary>**Click to View**</summary> ![newsletter-signals](/documentation/validator/newsletter-signals.png)</details>             | Passed |
| newsletter          | urls.py            | <details> <summary>**Click to View**</summary> ![newsletter-urls](/documentation/validator/newsletter-urls.png)</details>                   | Passed |
| newsletter          | views.py           | <details> <summary>**Click to View**</summary> ![newsletter-views](/documentation/validator/newsletter-views.png)</details>                 | Passed |
|                     |                    |                                                                                                                                            |        |
| products            | admin.py           | <details> <summary>**Click to View**</summary> ![products-admin](/documentation/validator/products-admin.png)</details>                     | Passed |
| products            | models.py          | <details> <summary>**Click to View**</summary> ![products-models](/documentation/validator/products-models.png)</details>                   | Passed |
| products            | urls.py            | <details> <summary>**Click to View**</summary> ![products-urls](/documentation/validator/products-urls.png)</details>                       | Passed |
| products            | views.py           | <details> <summary>**Click to View**</summary> ![products-views](/documentation/validator/products-views.png)</details>                     | Passed |
|                     |                    |                                                                                                                                            |        |
| profiles            | forms.py           | <details> <summary>**Click to View**</summary> ![profiles-forms](/documentation/validator/profiles-forms.png)</details>                     | Passed |
| profiles            | models.py          | <details> <summary>**Click to View**</summary> ![profiles-models](/documentation/validator/profiles-models.png)</details>                   | Passed |
| profiles            | urls.py            | <details> <summary>**Click to View**</summary> ![profiles-urls](/documentation/validator/profiles-urls.png)</details>                       | Passed |
| profiles            | views.py           | <details> <summary>**Click to View**</summary> ![profiles-views](/documentation/validator/profiles-views.png)</details>                     | Passed |
|                     |                    |                                                                                                                                            |        |
| shaping-surf (core) | settings.py        | <details> <summary>**Click to View**</summary> ![settings](/documentation/validator/settings.png)</details>                                 | Passed |
| shaping-surf (core) | urls.py            | <details> <summary>**Click to View**</summary> ![urls](/documentation/validator/urls.png)</details>                                         | Passed |


### JavaScript 

The [JSHint Validator]( https://jshint.com/), a JavaScript Code Quality Tool was used to validate the JavaScript code. All custom written JavaScript code passed without errors through the validator.

| App        | Folder    | File               | Screenshot                                                                                                           | Result |
|------------|-----------|--------------------|----------------------------------------------------------------------------------------------------------------------|--------|
| checkout   | static    | stripe_elements.js | <details> <summary>**Click to View**</summary> ![checkout-js](/documentation/validator/checkout-js.png)</details>     | Passed |
| contact    | static    | contact.js         | <details> <summary>**Click to View**</summary> ![contact-js](/documentation/validator/contact-js.png)</details>       | Passed |
| newsletter | static    | newsletter.js      | <details> <summary>**Click to View**</summary> ![newsletter-js](/documentation/validator/newsletter.js.png)</details> | Passed |
| products   | static | products.js     | <details> <summary>**Click to View**</summary> ![tutorials-js](/documentation/validator/tutorials-js.png)</details>   | Passed |
| root dir   | templates | base.html          | <details> <summary>**Click to View**</summary> ![base-js](/documentation/validator/base-js.png)</details>             | Passed |

### HTML

The [World Wide Web Consortium's Validation Service for Markup](https://validator.w3.org/) was used to check the HTML.

The rendered HTML source code  of each page from the browser of the deployed project by direct input into the validator was tested. The HTML source code of the rendered website is used to validate code with Django template tags. The HTML code passed through the validator without errors.
<br>

**HTML Validator Results:**

<details>
<summary>Click to View Validation by URI</summary>

![html-validation-uri](/documentation/validator/html-validation-uri.png)
</details>

<details>
<summary>Click to View Home</summary>

![html-home](/documentation/validator/html-home.png)
</details>

<details>
<summary>Click to View Tutorials</summary>

![html-tutorials](/documentation/validator/html-tutorials.png)
</details>

<details>
<summary>Click to View Tutorial Details</summary>

![html-tutorials-details](/documentation/validator/html-tutorials-detail.png)
</details>

<details>
<summary>Click to View About Us</summary>

![html-about-us](/documentation/validator/html-about-us.png)
</details>

<details>
<summary>Click to View Surfboards</summary>

![html-surfboard](/documentation/validator/html-surfboard.png)
</details>

<details>
<summary>Click to View Surfboard Details</summary>

![html-surfboard-detail](/documentation/validator/html-surfboard-detail.png)
</details>

<details>
<summary>Click to View FAQ</summary>

![html-faq](/documentation/validator/html-faq.png)
</details>

<details>
<summary>Click to View Resources</summary>

![html-resources](/documentation/validator/html-resources.png)
</details>

<details>
<summary>Click to View Newsletter</summary>

![html-newsletter](/documentation/validator/html-newsletter.png)
</details>

<details>
<summary>Click to View Newsletter Subscribed Success</summary>

![html-newsletter-success](/documentation/validator/html-newsletter-success.png)
</details>

<details>
<summary>Click to View Contact</summary>

![html-contact](/documentation/validator/html-contact.png)
</details>

<details>
<summary>Click to View Contact Success</summary>

![html-contact-success](/documentation/validator/html-contact-success.png)
</details>

<details>
<summary>Click to View Allauth</summary>

![html-allauth](/documentation/validator/html-allauth.png)
</details>

<details>
<summary>Click to View Profile</summary>

![html-profile](/documentation/validator/html-profile.png)
</details>

<details>
<summary>Click to View Profile Update</summary>

![html-profile-update](/documentation/validator/html-profile-update.png)
</details>

<details>
<summary>Click to View Profile Delete</summary>

![html-profile-delete](/documentation/validator/html-profile-delete.png)
</details>

<details>
<summary>Click to View Cart</summary>

![html-cart](/documentation/validator/html-cart.png)
</details>

<details>
<summary>Click to View Checkout</summary>

![html-checkout](/documentation/validator/html-checkout.png)
</details>

<details>
<summary>Click to View Checkout Success</summary>

![html-checkout-success](/documentation/validator/html-checkout-success.png)
</details>

<details>
<summary>Click to View Privacy Policy</summary>

![html-privacy-policy](/documentation/validator/html-privacy-policy.png)
</details>

### CSS

The official [World Wide Web Consortium (W3C) validator for CSS](https://jigsaw.w3.org/css-validator/validator) was used to validate the CSS style sheet code. The code passed through the validator with no issues.

<details>
<summary>Click for CSS Validator Results</summary>

![CSS-validator](/documentation/validator/css-validator.png)
</details>

## Performance Testing

Website performance was evaluated using the tool Google Lighthouse. This section presents the performance metrics, including load times, optimization opportunities, and the steps taken to enhance the site's speed and efficiency.

Lighthouse performance evaluation was performed on the deployed website using [Chrome Developer Tools Lighthouse Report](https://developer.chrome.com/docs/lighthouse/overview).

### General issues

- Stripe: Stripe is causing issues with the Lighthouse performance test.

| Issue                        | Screenshot                                                                                                                                                       |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Third party cookies (stripe) | <details> <summary>**Click to View**</summary> ![lighthouse-stripe-cookie](documentation/validator/lighthouse-stripe-cookie.png)</details>                       |
| Unused JavaScript            | <details> <summary>**Click to View**</summary> ![lighthouse-stripe-javascript](documentation/validator/lighthouse-stripe-javascript.png)</details>               |
| JavaScript                   | <details> <summary>**Click to View**</summary> ![lighthouse-unused-stripe-javascript](documentation/validator/lighthouse-unused-stripe-javascript.png)</details> |


### Mobile 

| App              | File                                      | Screenshot                                                                                                                                                                   |
|------------------|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| about            | lighthouse-mobile-about-faq               | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-about-faq](documentation/validator/lighthouse-mobile-about-faq.png)</details>                             |
| about            | lighthouse-mobile-about-resources         | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-about-resources](documentation/validator/lighthouse-mobile-about-resources.png)</details>                 |
| about            | lighthouse-mobile-about-surfboards        | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-about-surfboards](documentation/validator/lighthouse-mobile-about-surfboards.png)</details>               |
| about            | lighthouse-mobile-about-surfboards-detail | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-about-surfboards-detail](documentation/validator/lighthouse-mobile-about-surfboards-detail.png)</details> |
| about            | lighthouse-mobile-about-us                | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-about-usl](documentation/validator/lighthouse-mobile-about-us.png)</details>                              |
|                  |                                           |                                                                                                                                                                              |
| cart             | lighthouse-mobile-cart-empty              | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-cart-empty](documentation/validator/lighthouse-mobile-cart-empty.png)</details>                           |
| cart             | lighthouse-mobile-cart-full               | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-cart-full](documentation/validator/lighthouse-mobile-cart-full.png)</details>                             |
|                  |                                           |                                                                                                                                                                              |
| checkout         | lighthouse-mobile-checkout                | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-checkout](documentation/validator/lighthouse-mobile-checkout.png)</details>                               |
| checkout         | lighthouse-mobile-checkout-success        | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-checkout-success](documentation/validator/lighthouse-mobile-checkout-success.png)</details>               |
|                  |                                           |                                                                                                                                                                              |
| contact          | lighthouse-mobile-contact                 | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-contact](documentation/validator/lighthouse-mobile-contact.png)</details>                                 |
| contact          | lighthouse-mobile-contact-success         | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-contact-success](documentation/validator/lighthouse-mobile-contact-success.png)</details>                 |
|                  |                                           |                                                                                                                                                                              |
| home             | lighthouse-mobile-home                    | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-home](documentation/validator/lighthouse-mobile-home.png)</details>                                       |
|                  |                                           |                                                                                                                                                                              |
| newsletter       | lighthouse-mobile-newsletter              | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-newsletter](documentation/validator/lighthouse-mobile-newsletter.png)</details>                           |
|                  |                                           |                                                                                                                                                                              |
| private policy   | lighthouse-mobile-privacy-policy          | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-privacy-policy](documentation/validator/lighthouse-mobile-privacy-policy.png)</details>                   |
|                  |                                           |                                                                                                                                                                              |
| profile          | lighthouse-mobile-profile                 | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-profile](documentation/validator/lighthouse-mobile-profile.png)</details>                                 |
| profile update   | lighthouse-mobile-profile-update          | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-profile-update](documentation/validator/lighthouse-mobile-profile-update.png)</details>                   |
|                  |                                           |                                                                                                                                                                              |
| products        | lighthouse-mobile-tutorials               | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-tutorials](documentation/validator/lighthouse-mobile-tutorials.png)</details>                             |
| products-detail | lighthouse-mobile-tutorials-detail        | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-tutorials-detail](documentation/validator/lighthouse-mobile-tutorials-detail.png)</details>               |
|                  |                                           |                                                                                                                                                                              |
| allauth signin   | lighthouse-mobile-signin                  | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-signin](documentation/validator/lighthouse-mobile-signin.png)</details>                                   |
| allauth signout  | lighthouse-mobile-signout                 | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-signout](documentation/validator/lighthouse-mobile-signout.png)</details>                                 |
| allauth signup   | lighthouse-mobile-signup                  | <details> <summary>**Click to View**</summary> ![lighthouse-mobile-signup](documentation/validator/lighthouse-mobile-signup.png)</details>                                   |

### Desktop

| App              | Page                                       | Screenshot                                                                                                                                                                     |
|------------------|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| about            | lighthouse-desktop-about-faq               | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-about-faq](documentation/validator/lighthouse-desktop-about-faq.png)</details>                             |
| about            | lighthouse-desktop-about-resources         | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-about-resources](documentation/validator/lighthouse-desktop-about-resources.png)</details>                 |
| about            | lighthouse-desktop-about-surfboards        | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-about-surfboards](documentation/validator/lighthouse-desktop-about-surfboards.png)</details>               |
| about            | lighthouse-desktop-about-surfboards-detail | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-about-surfboards-detail](documentation/validator/lighthouse-desktop-about-surfboards-detail.png)</details> |
| about            | lighthouse-desktop-about-us                | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-about-us](documentation/validator/lighthouse-desktop-about-us.png)</details>                               |
|                  |                                            |                                                                                                                                                                                |
| cart             | lighthouse-desktop-cart-empty              | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-cart-empty](documentation/validator/lighthouse-desktop-cart-empty.png)</details>                           |
| cart             | lighthouse-desktop-cart-full               | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-cart-full](documentation/validator/lighthouse-desktop-cart-full.png)</details>                             |
|                  |                                            |                                                                                                                                                                                |
| checkout         | lighthouse-desktop-checkout                | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-checkout](documentation/validator/lighthouse-desktop-checkout.png)</details>                               |
| checkout         | lighthouse-desktop-checkout-success        | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-checkout-success](documentation/validator/lighthouse-desktop-checkout-success.png)</details>               |
|                  |                                            |                                                                                                                                                                                |
| contact          | lighthouse-desktop-contact                 | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-contact](documentation/validator/lighthouse-desktop-contact.png)</details>                                 |
| contact          | lighthouse-desktop-contact-success         | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-contact-success](documentation/validator/lighthouse-desktop-contact-success.png)</details>                 |
|                  |                                            |                                                                                                                                                                                |
| home             | lighthouse-desktop-home                    | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-home](documentation/validator/lighthouse-desktop-home.png)</details>                                       |
|                  |                                            |                                                                                                                                                                                |
| newsletter       | lighthouse-desktop-newsletter              | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-newsletter](documentation/validator/lighthouse-desktop-newsletter.png)</details>                           |
|                  |                                            |                                                                                                                                                                                |
| private policy   | lighthouse-desktop-privacy-policy          | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-privacy-policy](documentation/validator/lighthouse-desktop-privacy-policy.png)</details>                   |
|                  |                                            |                                                                                                                                                                                |
| profile          | lighthouse-desktop-profile                 | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-profile](documentation/validator/lighthouse-desktop-profile.png)</details>                                 |
| profile update   | lighthouse-desktop-profile-update          | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-profile-update](documentation/validator/lighthouse-desktop-profile-update.png)</details>                   |
|                  |                                            |                                                                                                                                                                                |
| products        | lighthouse-desktop-tutorials               | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-tutorials](documentation/validator/lighthouse-desktop-tutorials.png)</details>                             |
| products-detail | lighthouse-desktop-tutorials-detail        | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-tutorials-detail](documentation/validator/lighthouse-desktop-tutorials-detail.png)</details>               |
|                  |                                            |                                                                                                                                                                                |
| allauth signin   | lighthouse-desktop-signin                  | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-signin](documentation/validator/lighthouse-desktop-signin.png)</details>                                   |
| allauth signout  | lighthouse-desktop-signout                 | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-signout](documentation/validator/lighthouse-desktop-signout.png)</details>                                 |
| allauth signup   | lighthouse-desktop-signup                  | <details> <summary>**Click to View**</summary> ![lighthouse-desktop-signup](documentation/validator/lighthouse-desktop-signup.png)</details>                                   |

## Accessibility Testing

Accessibility testing was conducted to ensure the website is usable by people with various disabilities. This section covers the tools used for testing, such as screen readers and accessibility validators, and the improvements made based on the results.

**Focusable Elements**
After manual testing, the html element anchor was changed to semantically correct button for scroll-to-top button to make it focusable. The button, just like other focusable elements on the website, has visual feedback as well as `aria-label` and `sr-only` explanation for its purpose when using a screen reader.

![test-accessibility-button](/documentation/testing/test-accessibility-button.png)

**Screen Readers**
For improved UX when using a screen reader, `aria-hidden="true"` was added to all fontawesome icons.

Skip links were added to all pages for easy navigation while using a screen reader. If there is a form present, the user has the option to skip to the main content or skip to the form.

```html	
{% block skip_link %}
<a href="#sr-main-content" class="sr-only sr-only-focusable">Skip to main content</a>
<a href="#subscriber-form" class="sr-only sr-only-focusable">Skip to newsletter subscription form</a>
{% endblock %}
```

As recommended by the [W3C, Web Accessibility Initiative (WAI)](https://www.w3.org/WAI/tutorials/images/decorative/), alternative text was removed from purely decorative images for links to scientific resources in the about app, to avoid audible clutter.

### WAVE Web Accessibility Evaluation Tool

The [Wave WebAIM Validator](https://wave.webaim.org/) was used to validate web accessibility on the deployed website.

The WAVE tool was used to test the accessibility of the website. The results of the test are successful and the website is fully accessible. 

One warning of redundant links is displayed. The navigation item 'homepage' has the same url as the adjacent logo, which is a common practice for good UX. The warning will therefore not be heeded.

![wave-home](/documentation/validator/wave-home.png)

<details>
<summary>Click to View Products: Tutorials</summary>

![wave-tutorials](/documentation/validator/wave-tutorials.png)
</details>

<details>
<summary>Click to View Click to View Products: Tutorials Detail</summary>

![wave-tutorials-detail](/documentation/validator/wave-tutorials-details.png)
</details>

<details>
<summary>Click to View About Us</summary>

![wave-about-us](/documentation/validator/wave-about-us.png)
</details>

<details>
<summary>Click to View About: Surfboards</summary>

![wave-surfboards](/documentation/validator/wave-surfboards.png)
</details>

<details>
<summary>Click to View Click to View About: Surfboards Detail</summary>

![wave-surfboards-detail](/documentation/validator/wave-surfboards-detail.png)
</details>

<details>
<summary>Click to View Click to View About: FAQ</summary>

![wave-about-faq](/documentation/validator/wave-faq.png)
</details>

<details>
<summary>Click to View Click to View About: Resources</summary>

![wave-resources](/documentation/validator/wave-resources.png)
</details>

<details>
<summary>Click to View Click to View Newsletter</summary>

![wave-newsletter](/documentation/validator/wave-newsletter.png)
</details>

<details>
<summary>Click to View Contact</summary>

![wave-contact](/documentation/validator/wave-contact.png)
</details>

<details>
<summary>Click to View Allauth Account</summary>

![wave-allauth](/documentation/validator/wave-allauth.png)
</details>

<details>
<summary>Click to View Cart</summary>

![wave-cart](/documentation/validator/wave-cart.png)
</details>

<details>
<summary>Click to View Checkout</summary>

![wave-checkout](/documentation/validator/wave-checkout.png)
</details>

<details>
<summary>Click to View Privacy Policy</summary>

![wave-privacy-policy](/documentation/validator/wave-privacy-policy.png)
</details>

### Coolors Contrast Checker

[Coolors Color Contrast Checker](https://coolors.co/contrast-checker/333333-ffffff) was used to validate color contrast for web accessibility in terms of readability.

![Color contrast test](/documentation/color-contrast.png)

For the **link color**, the color #0000FF was chosen on recommendation from the [WebAIM community blog](https://webaim.org/blog/wcag-2-0-and-link-colors/) and the [WebAIM Color Contrast Checker](https://webaim.org/resources/contrastchecker/), since the default link color does not meet the minimum contrast of accessibility guidelines. 

![color-contrast-links](/documentation/color-contrast-links.png)

## Manual Testing

Manual testing was conducted to verify the functionality, usability, and user experience of the website. This section details the test cases executed, the steps followed, and the results observed for each feature and user interaction.

### Test Cases

### Custom Error pages

To conveniently test the styling on the custom error pages during development, the following code was temporarily added to the app profile views and urls:

#### 404 Not Found

In `views.py`:

```python
def custom_404(request, exception):
    return render(request, '404.html', status=404)
```
In `urls.py`:

```python
handler404 = 'profiles.views.custom_404'
```

To test: Navigate to any non-existent URL, e.g., /profile/test-404/

 <details>
<summary>Click for image 404 during development</summary>

![test-dev-404](/documentation/testing/test-dev-404.png)
</details>

#### 403 Forbidden

In `views.py`:
```python
from django.core.exceptions import PermissionDenied

def test_403(request):
    raise PermissionDenied
```
In `urls.py`:
```python
path('test-403/', views.test_403, name='test_403'),
```

To test: Navigate to /profile/test-403/

 <details>
<summary>Click for image 403 during development</summary>

![test-dev-403](/documentation/testing/test-dev-403.png)
</details>

## Security Testing

This section focuses on security measures and testing.

### Security Considerations

As this is an educational project not intended for real-world deployment or to process actual payments, advanced security measures are beyond the current scope but would be essential in a production environment. 

**Stripe Integration**: 
- The project uses Stripe's test mode for simulating payments.
- All communications with Stripe API are done over HTTPS.

**Environment Variables**: Sensitive information like API keys are stored as environment variables to prevent exposure in the codebase. As precaution and to eliminate human error of deploying the project with DEBUG setting true, the switching between on and off is handled by environmental variable in env.py setting. If the variable is found, the code is in development environment and debug is set to true. If variable is not found, the code is in production environment and debug is set to false.

**Error Handling**: Verified that error messages do not expose sensitive information.

**CSRF Protection**: Tested CSRF token implementation on all forms handling.

**Database Security**: The project utilizes Django's ORM for database operations, which provides built-in protection against SQL injection attacks.

**Authentication**: Authentication system, including password policies and session management, is handled by Django Allauth.

**Authorization**: Ensured proper access controls are in place, especially for product management, personal information, and payment-related functionalities.

![webhooks-successful](/documentation/testing/webhooks-successful.png)

![webhooks-successful-charge](/documentation/testing/webhooks-successful-charge.png)

![webhooks-successful-intent](/documentation/testing/webhooks-successful-intent.png)

![test-webhook-last](/documentation/testing/test-webhook-last.png)

![testing-email](/documentation/testing/test-email.png)

## User Story Testing

Each user story defined in the project requirements was tested to ensure that the implemented features meet the needs and expectations of our target users. This section maps user stories to specific functionalities and describes how they were validated.<br>

The following Epics (Feature Area) & User Stories all passed testing without issues.

| Feature Area | User Story | Expected Result | Result |
|-------------|------------|-----------------|--------|
| Website Content | Homepage First Impression | As a USER, I can view a welcoming homepage and easily identify the website's purpose so that I feel welcome and understand what the website offers. | A welcome message and brief description of the websites offerings are displayed. |
| Navigation and Orientation | As a USER, I can easily understand the structure of the website and identify navigation features/elements so that I can navigate the website to find what I am looking for. | The website has a clean layout with clear visual hierarchy and prominently placed navigation elements. | Passed |
| Web Accessibility | As a USER with disabilities or using assistive technologies, I can easily navigate the website so that I can find what I am looking for and make a purchase. | The website complies with Web Content Accessibility Guidelines (WCAG). | Passed |
| Product Exploration | View a List of Products | As a USER, I can view a list of products so that I can choose products I want to purchase. | Product images, names, brief descriptions, and prices are displayed. |
| Product Exploration | View Individual Product | As a USER, I can click on an individual product so that I can view the price, full product description, product rating, and a larger product image. | Clicking on a product reveals full product details. |
| Product Exploration | Filter Products by Category | As a USER, I can filter the products by category so that I can easily find what I am looking for. | A dropdown menu allows users to filter by category, and the product list updates accordingly. |
| Product Exploration | Search Feature | As a USER, I can search the products by keywords so that I can quickly find what I am looking for. | A search bar is prominently displayed and returns relevant results. |
| Shopping Cart | Add items to shopping cart | As a USER, I can add items to the shopping cart so that I can make a purchase. | Items are added to the shopping cart when the Add to cart button is clicked. |
| Shopping Cart | View items in shopping cart | As a USER, I can view the items in my shopping cart so that I can identify what I purchase. | The items in the shopping cart are displayed. |
| Shopping Cart | Update items in shopping cart | As a USER, I can adjust the items in my shopping cart so that I can easily make changes before I checkout and purchase. | Buttons to delete or modify items in the cart are clearly displayed. |
| Payment Process | Payment Information | As a USER, I can easily enter my payment information so that I can complete the purchase easily. | A clear, easy-to-understand payment form is provided. |
| Payment Process | Secure Payment | As a USER, I can feel confident that my personal details and the payment process are secure so that I can confidently enter the necessary information to make the purchase. | The payment process is secure and uses Stripe. |
| Communication | Contact Store owner | As a USER, I can find a 'Contact' page with ways to reach the store owner so that I can provide feedback, ask questions, or send an enquiry to order a custom-made surfboard. | A Contact page is accessible from the navigation with clear instructions. |
| Communication | Newsletter | As a USER, I can sign up for a newsletter so that I can get notifications on new tutorials and Q&A Sessions. | A newsletter sign-up field is clearly displayed. |
| User Account | Sign Up for User Account | As a USER, I can sign up for a new user account so that I can create a user profile and have an overview of my purchases and save my personal information. | A Sign Up link is prominently displayed and leads to a user-friendly sign-up form. |
| User Account | Update User Profile | As a USER, I can update my user profile so that I can change or correct my personal details. | Signed-in users can update their personal details. |
| User Account | Delete User Account | As a USER, I can delete my user account so that I can delete all my information. | Signed-in users can delete their account and personal information from the website. |
| Product Management | Add a Product | As a STORE OWNER, I can add a product so that I can expand my product offer. | Superusers or staff can add new products. Products can be published immediately or saved as a draft for a future publishing date. |
| Product Management | Update a Product | As a STORE OWNER, I can update a product so that I can update details with minimum effort. | Superusers or staff can update products. |
| Product Management | Delete a Product | As a STORE OWNER, I can delete a product from my product offer. | Superusers or staff can delete products. |
| User Experience | Custom Error page | As a USER, I want to see a user-friendly custom error page when I encounter an error based on forbidden access or object not found so that I can understand why the error occurred and feel safe. | Custom 403, 404, and 500 error pages are displayed when appropriate. |

## Responsiveness Testing

The website's responsiveness across various devices and screen sizes was thoroughly tested. This project utilizes Bootstrap's powerful grid system for creating a responsive layout that adapts to various screen sizes. Dividing the viewport into up to 12 columns ensure that the UI scales seamlessly from mobile devices to large desktop screens.
Only a few media queries were necessery to obtain the best results.

## Browser Compatibility

Testing was performed across multiple browsers to ensure cross-browser compatibility. Friends and family assisted in testing the deployed website on different browsers: Chrome, Firefox, Safari, and Edge. The deployed website works seamlessly across all browsers.

## Bugs

### Known Bugs

There are no known bugs in the deployed project.

### Resolved Bugs
This section lists significant bugs that were encountered during development and testing, along with the solutions implemented. 


| Bug                                                                 | Description                                                                                                                                                                                           | Solution Applied                                                                                                                                                                                 | Result |
|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| AttributeError: 'BlankChoiceIterator' object has no attribute 'len' | Error occurred when adding an order in the admin panel due to incompatibility with the CountryField choices processing.                                                                               | Upgrade Django CountryField package to the latest version.                                                                                                                                       | Solved |
| Unrecognized request URL                                            | Error encountered during order completion process.                                                                                                                                                    | Generated new Stripe API keys and properly set them in environment variables.                                                                                                                    | Solved |
| TypeError: Field 'id' expected a number but got ('2', 1)            | Checkout view raised an error due to incorrect data type for product ID.                                                                                                                              | change to item_id product = Product.objects.get(id=item_id) instead of product_id                                                                                                                | Solved |
| AttributeError: 'Order' object has no attribute 'update_total'      | Signal handlers in signals.py attempted to call a non-existent method on the Order model.                                                                                                             | Add update_total method to the Order model and call it explicitly in the checkout view.                                                                                                          | Solved |
| Order_total not displayed on checkout_success.html                  | Update_total method on Order model was calculating grand_total                                                                                                                                        | Add order_total to calculate grand_total.                                                                                                                                                        | Solved |
| Discount_amount not displayed on checkout_success.html              | Discount calculated in cart contexts.py is for temporary session-based calculations to display in shopping cart while the order model method is for permanent database-stored calculations.           | Add calculation for discount_code to update_total method on Order model.                                                                                                                         | Solved |
| Error in stripe webhook: full_name is not provided                 | Print statements show the full_name in terminal but stripe webhooks do not receive the information.                                                                                                   | Add order to OrderItem when creating an order in webhook_handler to correctly pass order details to stripe payment intent.                                                                       | Solved |
|                                                                     |                                                                                                                                                                                                       | <details> <summary>Click to View webhook error</summary> ![error-webhook](/documentation/validator/error-webhook.png)</details>                                                                   |        |
| checkout  views.py                                                  | All orders created in webhook.                                                                                                                                                                        | Fix indentation error in checkout view which prevented order to be created after validating the order form.                                                                                      | Solved |
| ContactForm                                                         | KeyError: user_profile not found in placeholders.                                                                                                                                                     | Add a placeholder for the user_profile field.                                                                                                                                                    | Solved |
| djrichtextfield and ckeditor                                        | Security issues due to djrichtextfield reported in admin panel with suggestion to swicth to ckeditor but After switching to ckeditor a new warning in the terminal that ckeditor has security issues. | Install Summernote to use SummernoteModelAdmin in admin interface and as suggested by Code Institute tutor support reinstall djrichtextfield since otherwise inconsistency with migration files. | Solved |
| Art model                                                           | Typo: self.get_art_display()                                                                                                                                                                          | self.get_type_display()                                                                                                                                                                          | Solved |
| wh_secret                                                           | wh_secret was set to development endpoint                                                                                                                                                             | create new endpoint for deployed website                                                                                                                                                         | Solved |
| Emails                                                              | Sending emails not working                                                                                                                                                                            | After changing the condition of debug settings in settings.py, the condition in email settings was not updated. Adjusted condition to same condition as debug condition.                         | Solved |
| Database                                                            | Issue in connecting to datase.                                                                                                                                                                        | Change database to Code Institute Database                                                                                                                                                       | Solved |
| Summernote                                                          | Error in rendered hmtl validation.                                                                                                                                                                    | Type content manually instead of copy paste.                                                                                                                                                     | Solved |
| paragraph tags                                                      | Extra paragraph tags caused error in html validation.                                                                                                                                                 | Remove paragraph around content since summernote adds the html tags.                                                                                                                             | Solved |
| Invalid Stripe webhook signature: No signatures found matching the expected signature for payload | webhook secret not found.                                                                                                                                                                             | Fix conditional statement in settings.py for DEV variable and email settings (reverse it)                                                                                                                       | Solved |
| 404 Error for unsubscribe_url | Unsubscribe_url not working in production environment due to a double slash between BASE_URL and unsubscribe_token. | reverse() function in the generate_unsubscribe_url view adds a slash at the beginning of the relative URL. Remove trailing slash from BASE_URL set in settings.py. | Solved |
| profile-update-form           | Form submission failed due to undefined validation of email field. | Add return statement true to valid email field condition.                                       | Solved |
| Footer not sticking to bottom | Footer not sticking to bottom on index.html with little content.   | Add flex-grow-1 to main section in base.html and flex-box property to wrapper div on index.html | Solved |
| Duplicate orders | Duplicate orders with the same stripe payment id were created for each checkout process. | Change check in webhook_handler.py of existing orders from `Order.objects.filter()` by database queryset to `Order.objects.get()` by single object retrieveal. | Solved |
| Reappeared: Duplicate orders | idem. Clear site data (dev tools > application > storage > clear site data) between orders worked temporarily. | Delete postal_code from save info to user profile and disable webhook endpoint for local development environment. | Solved |
| Webhook 500 error            | Code from walkthrough – deprecated since 2022: Retrieve data from the intent object directly in `billing_details = intent.charges.data[0].billing_details` and `grand_total = round(intent.charges.data[0].amount / 100, 2)`= 500 error in stripe webhooks. | Change back to additional stripe API call for stripe_charge object: `stripe_charge = stripe.Charge.retrieve(intent.latest_charge)` | Solved |
| Checkout / HTML attribute error | Attribute placeholder not allowed on element `<select>`: CountryField | Move placeholder assignment logic into conditional statement: `if field != country` in checkout / forms.py | Solved |

## Programs Used

A comprehensive list of all tools, validators, and programs used throughout the testing process and for this testing documentation. This section provides links and brief descriptions of each tool, helping readers understand the testing methodology and potentially replicate the tests.

-	[Python Linter Validator](https://pep8ci.herokuapp.com/) provided by the Code Institute according for Python code.
-	[World Wide Web Consortium's Validation Service for Markup](https://validator.w3.org/) for HTML code.
-	[World Wide Web Consortium (W3C) validator for CSS](https://validator.w3.org/) validator for the CSS stylesheet.
-	[JSHint Validator]( https://jshint.com/) for JavaScript scripts.
-	[Google Chrome Developer Tools Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) for performance report.
-	[Wave WebAIM Validator](https://wave.webaim.org/) to validate web accessibility.
-	[Coolors Color Contract Checker]( https://coolors.co/contrast-checker/112a46-acc8e5) to assess contrast for accessibility.
-	[Table-magic](https://stevecat.net/table-magic/) to create markdown tables for this TESTING.md.
