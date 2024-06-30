# ![logo](/documentation/logo_wave.png) Testing Documentation for Shaping Sustainable Surf

This document outlines the testing procedures and results for the ecommerce project Shaping Sustainable Surf.

For development documentation, please refer to the [README.md](README.md).

View the live project [here]().<br>  
*(To open in a new window, press "Ctrl" + click on the link, or "⌘ + click" on Mac)*

## Overview

Thorough and continuous testing was performed throughout the development process to ensure:
- Seamless functionality of the code
- Adherence to official standards and guidelines
- Optimal user experience across various devices and browsers

## Table of Contents

[Automated Testing](#automated-testing)
[Manual Testing](#manual-testing)
[Security Testing](#security-testing)
[User Story Testing](#user-story-testing)
[Responsiveness Testing](#responsiveness-testing)
[Browser Compatibility](#browser-compatibility)
[Accessibility Testing](#accessibility-testing)
[Performance Testing](#performance-testing)
[Known Bugs](#known-bugs)
[Resolved Bugs](#resolved-bugs)

## Automated Testing

This section covers the automated tests performed on the project's code. It includes validation of Python, JavaScript, HTML, and CSS using industry-standard tools to ensure code quality and adherence to best practices.

### Python

[Python Linter Validator](https://pep8ci.herokuapp.com/) provided by the Code Institute according to the PEP 8 style guide was used for validating the Python code.
[Results to be added]

### JavaScript 

The [JSHint Validator]( https://jshint.com/), a JavaScript Code Quality Tool was used to validate the JavaScript code.
[Results to be added]

### HTML

The [World Wide Web Consortium's Validation Service for Markup](https://validator.w3.org/) was used to check the HTML.

HTML code by URI input as well as loading the source code of each page from the browser by direct input into the validator. The HTML source code of the rendered website is used to validate code with Django template tags.

[Results to be added]

### CSS

The official [World Wide Web Consortium (W3C) validator for CSS](https://validator.w3.org/) was used to validate the CSS style sheet code.
[Results to be added]

## Manual Testing

Manual testing was conducted to verify the functionality, usability, and user experience of the website. This section details the test cases executed, the steps followed, and the results observed for each feature and user interaction.

Test Cases
[Table to be added]

## Security Testing

This section focuses on security measures and testing.

### Security Considerations

As this is an educational project not intended for real-world deployment or to process actual payments, advanced security measures are beyond the current scope but would be essential in a production environment. 

**Stripe Integration**: 
- The project uses Stripe's test mode for simulating payments.
- All communications with Stripe API are done over HTTPS.

**Environment Variables**: Sensitive information like API keys are stored as environment variables to prevent exposure in the codebase.

**Error Handling**: Verified that error messages do not expose sensitive information.

**CSRF Protection**: Tested CSRF token implementation on all forms handling.

**Database Security**: The project utilizes Django's ORM for database operations, which provides built-in protection against SQL injection attacks.

**Authentication**: Authentication system, including password policies and session management, is handled by Django Allauth.

**Authorization**: Ensured proper access controls are in place, especially for product management, personal information, and payment-related functionalities.

## User Story Testing

Each user story defined in the project requirements was tested to ensure that the implemented features meet the needs and expectations of our target users. This section maps user stories to specific functionalities and describes how they were validated.
[Table to be added]

## Responsiveness Testing

The website's responsiveness across various devices and screen sizes was thoroughly tested. This section outlines the devices and screen resolutions used for testing and documents any adjustments made to ensure a consistent user experience across all platforms.
[Table to be added]

## Browser Compatibility

Testing was performed across multiple browsers to ensure cross-browser compatibility. This section lists the browsers tested, versions used, and any browser-specific issues encountered and resolved.
[Table to be added]

## Accessibility Testing

Accessibility testing was conducted to ensure the website is usable by people with various disabilities. This section covers the tools used for testing, such as screen readers and accessibility validators, and the improvements made based on the results.
[Results to be added]

### WAVE Web Accessibility Evaluation Tool
The [Wave WebAIM Validator](https://wave.webaim.org/) was used to validate web accessibility on the deployed website.
[Results to be added]

### Coolors contrast checker
[Coolors Color Contrast Checker]( https://coolors.co/contrast-checker/112a46-acc8e5) was used to validate color contrast for web accessibility in terms of readability.
[Results to be added]

## Performance Testing

Website performance was evaluated using the tool Google Lighthouse. This section presents the performance metrics, including load times, optimization opportunities, and the steps taken to enhance the site's speed and efficiency.

Lighthouse performance evaluation was performed on the deployed website using [Chrome Developer Tools Lighthouse Report](https://developer.chrome.com/docs/lighthouse/overview).
[Results to be added]

### Known Bugs
This section lists any known issues or limitations in the current version of the website. It includes descriptions of the bugs, their impact, and any planned resolutions or workarounds.
[Table to be added]

### Resolved Bugs
Here, we document significant bugs that were encountered during development and testing, along with the solutions implemented. This section demonstrates the problem-solving process and the improvements made to the project over time.
[Table to be added]

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
