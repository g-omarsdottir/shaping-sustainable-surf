# ![logo](/documentation/logo_wave.png) Shaping Sustainable Surf

![mockup](/documentation/mockup.png)

![Static Badge](https://img.shields.io/badge/last_commit-september_2024-Ffcad4)
![Static Badge](https://img.shields.io/badge/contributors-1-B0d0d3)
![Static Badge](https://img.shields.io/badge/languages-4-C08497)
![Static Badge](https://img.shields.io/badge/javascript-46.2%25-F7af9d)
![Static Badge](https://img.shields.io/badge/css-21.2%25-fbcac1)
![Static Badge](https://img.shields.io/badge/html-18.8%25-ffdfc6)
![Static Badge](https://img.shields.io/badge/python-13.4%25-fffbd5)
![Static Badge](https://img.shields.io/badge/framework-django-a5e1cd)
![Static Badge](https://img.shields.io/badge/payments-stripe-fff)
![Static Badge](https://img.shields.io/badge/wave_a11y-validated-e1f7cb)
![Static Badge](https://img.shields.io/badge/w3c-validated-caafdf)


**View the live project [here](https://shaping-sustainable-surf-8794b08a1b3a.herokuapp.com/).**<br>
*(To open in a new window, press "ctrl" (or ⌘ for Mac) + click on the link)*

Welcome to Shaping Sustainable Surf, a fully functional Django ecommerce web application that offers access to online video tutorials.

## Table of contents

- [Project Goals](#project-goal)
  - [User Experience](#user-experience)
  - [Target Group](#target-group)
  - [Visitors Goals](#visitors-goals)
- [Design](#design)
  - [Layout](#layout)
  - [Wireframes](#wireframes)
  - [Colors](#colors)
  - [Typography](#typography)
- [Project planning](#project-planning)
  - [Database Schema](#database-schema)
  - [Agile Development Methods (Epics, User Stories, MoSCoW Prioritization, Kanban board)](#agile-development-methods-epics-user-stories-moscow-prioritization-kanban-board)
- [Features](#features)
  - [Main Features](#main-features)
  - [Responsiveness](#responsiveness)
  - [Security](#security)
  - [Future Features](#future-features)
-	[Web Marketing](#web-marketing)
    -	[Ecommerce Business Model](#ecommerce-business-model)
    -	[Marketing Strategies](#marketing-strategies)
    -	[Search Engine Optimization (SEO)](#search-engine-optimization-seo)
    -	[Privacy Policy](#privacy-policy)
-	[Technology Used](#technology-used)
    -	[Languages Used](#languages-used)
    -	[Libraries and Frameworks Used](#libraries-and-frameworks-used)
    -	[Programs Used](#programs-used)
- [Deployment and Local Development](#deployment-and-local-development)
  - [Local Clone](#local-clone)
  - [Fork](#fork)
  - [Database](#database)
  -	[Cloudinary](#cloudinary)
  -	[Stripe](#stripe)
  - [Google Mail (Gmail) API](#google-mail-gmail-api)
  - [Deployment](#deployment-using-heroku)
- [Credits](#credits)
  - [Content & Imagery](#content)
  -  [Acknowledgements](#acknowledgements)

**Testing and Bugs** are documented in the separate file [TESTING.md](TESTING.md).

## Project Goal

The website offers access to online video tutorials for surfers and shapers, who want to acquire or progress their surfboard shaping skills while minimizing their environmental impact. The name itself draws a parallel to the process of crafting a surfboard, which is called shaping. 

The name implies that the goal is not only shaping physical surfboards but shaping the future of surfing itself by promoting eco-friendly practices and education.

## User Experience

### Target Group

Eco-conscious surfers, shapers and people in general who
-	Are passionate about surfing, the environment, the ocean, and seek to minimize their environmental impact and prioritize environmental responsibility while pursuing the sport they love.
-	Want to learn how to shape a surfboard using sustainable materials.
-	Are concerned about the environmental impact of traditional surfboard construction and may feel disconnected from the sport due to the mass-produced nature of surfboards.
-	Enjoy hands-on DIY projects and take pride in building their own equipment.
-	Want to learn or further define their skills and techniques needed to shape their own surfboards.

### Visitors Goals

#### First-Time Visitor Goals

As a first-time visitor, I can

-	Enjoy the visually appealing homepage featuring beautiful images showcasing the beauty of the ocean, surfing and sustainable surfboard shaping.
-	Quickly grasp the website's core offering
-	Easily navigate the website to find relevant information.
-	Learn about the different types of tutorials offered.
-	Explore the video tutorial library.
-	Purchase a tutorial that interests me.
-	Learn about sustainable surfboard shaping and the benefits of eco-friendly materials.
-	Understand the benefits of using eco-friendly materials.
-	Browse through images of sustainable surfboards that the store owner shaped
-	Sign up for a newsletter so that I can stay updated.
-	Contact the store owner if I have questions about the tutorials or want to receive an offer for a custom-made surfboard.

#### Returning Visitors Goals

As a returning visitor, I want to

-	Search for new tutorials based on my interests.
-	Purchase additional tutorials that interest me.
-	Seek inspiration for my own project by browsing through images of custom-made sustainable surfboards.
-	Sign up for a newsletter because so that I can participate in the Q&A sessions announced in the newsletter.
-	Contact the store owner if I need advice.

#### Frequent Visitors Goals

As a frequent visitor, I want to

-	See if new tutorials or information on new eco-friendly materials have been added.
-	Purchase additional tutorials that interest me.
-	See if there are new images of custom-made sustainable surfboards.
-	Contact the store owner if I have questions in the course of shaping my own surfboard by following the tutorials.

## Design

### Layout

The layout of the website is devided into an area accessible to all and area exclusively for logged-in users, as dipicted in the flowchart below.

![layout-flowchart](/documentation/layout-flowchart.png)

### Wireframes

Wireframes were designed mobile-first, since the majority of ecommerce purchases are done with mobile devices or tablets.

Screen sizes smaller than 320 were not considered in the design.

#### Wireframes Mobile Version

![mobile-home-products](/documentation/mobile-home-products.png)

![mobile-user-related](/documentation/mobile-user-related.png)

![mobile-about-surfboards](/documentation/mobile-about-surfboards.png)

![mobile-about-faq](/documentation/mobile-about-faq.png)

![mobile-checkout](/documentation/mobile-checkout.png)

#### Wireframes Desktop Version

![desktop wireframe home](/documentation/wf-home.png)
![desktop wireframe products-tutorials](/documentation/wf-products-tutorials.png)
![desktop wireframe wf-product-tutorial-detail](/documentation/wf-products-tutorial-detail.png)
![desktop wireframe wf-about-us](/documentation/wf-about-us.png)
![desktop wireframe wf-about-surfboards](/documentation/wf-about-surfboards.png)
![desktop wireframe wf-about-surfboard-detail](/documentation/wf-about-surfboard-detail.png)
![desktop wireframe wf-about-faq](/documentation/wf-about-faq.png)
![desktop wireframe wf-about-resources](/documentation/wf-about-resources.png)
![desktop wireframe wf-contact](/documentation/wf-contact.png)
![desktop wireframes wf-profile](/documentation/wf-profile.png)
![desktop wireframe wf-allauth](/documentation/wf-allauth.png)
![desktop wireframe wf-checkout-cart](/documentation/wf-checkout-cart.png)
![desktop wireframe wf-checkout](/documentation/wf-checkout.png)
![desktop wireframe wf-checkout-confirmation](/documentation/wf-checkout-confirmation.png)

### Colors

The website's colors are inspired by the ocean and the beach. The main color of the website is the blue #57a7b3 used in the website logo.

![colors](/documentation/colors.png)

A complimenting colorpalette with the website logo's color was created by [Muzli Colors](https://colors.muz.li/palette/57a7b3/3d757d/b35794/7d3d67/b3a357). To keep the overall layout sleek and avoiding visual clutter, the complementing colors were mainly used as accents in box-shadows and for pseudo-class hover effect.

The font color is a warm tone of black and background color is white, which make a very good match for accessability, readability and contrast while being easy on the eye.

[Coolors Color Contrast Checker](https://coolors.co/contrast-checker/333333-ffffff) score:

![contrast checker](/documentation/color-contrast.png)

### Typography

Font types were chosen to create a clean and modern look with a focus on readability.

[Roboto flex](https://fonts.google.com/specimen/Roboto+Flex) was chosen as the primary font for the website, used for all elements except for headings. The font is variable and offers a range of weights, making it suitable for various design elements.

[Roboto slab](https://fonts.google.com/specimen/Roboto+Slab?query=roboto+slab) was chosen as the secondary font. This font is used for headings, ensuring a clear hierarchy and visual appeal. This font is a serif font with subtle decorative details at the ends of strokes. While serif fonts can be used for body text, they may be less readable than sans-serif fonts at smaller sizes due to the increased complexity of the characters. Serif fonts are generally more readable at larger sizes, making them well-suited for headings.

## Project planning

### Database Schema

This project leverages a serverless PostgreSQL database for efficient data management. A well-defined Entity Relationship Diagram (ERD) (see below) was created upfront to guide development. This approach minimizes database complexity and streamlines the development process, reducing the need for future modifications and debugging. Each model within the project directly corresponds to a table in the ERD, ensuring a clear and consistent data structure.

#### Technical Architecture

**Technical Design:** Separation of concern was implemented by dividing key components into individual Django Models (see ERD). This allows for simple and reliable queries based on the primary key, as well as easy management and scalability.

Relationships between the model fields are indicated with relationship lines on the ERD.

Each ERD represents an individual Django app. Relationships between models in different apps are indicated on the ERD if applicable.

**Model-Based Design:** The principles of separation of concerns are adhered to by employing distinct Django models for each key system component (see ERD). This promotes code clarity, maintainability, and scalability.

**Relational Data Modeling:** The ERD effectively visualizes the relationships between models and model fields, fostering the construction of streamlined and efficient database queries utilizing primary keys.

#### Key Features

**Product Management:** The custom models facilitate the storage and management of individual product entities in the products app.

Products are stored in one model. Categories and Subcategories are stored in separate models, which allows for scalability and streamlines further technical design. 

Choices for the Category and Subcategory models are defined as constants within the models. This guarantees consistent terminology throughout the application, enhancing user experience and simplifying search queries.

This approach simplifies the models for the shopping and purchase process, as well as allows for code consistency in code, by referring to products in all html template by the name product, while assuring a separation of concerns and explicitness.

Superusers (store owners) are granted comprehensive permissions within the application, allowing them to efficiently manage content across the platform. These permissions encompass creation, update, and deletion of product data, and pricing adjustments.

![ERD Product model](/documentation/erd-product.png)

![ERD Product model constants](/documentation/erd-product-constants.png)

**Ecommerce Functionality**

**Discount Codes:** The custom model facilitates the storage and management of individual discount codes in the cart app. The model is used to validate the code and apply the discount to the shopping cart. To ensure the code is valid, the model checks if the code is in the database, and if the code is in the database, if the code is currently active. As precaution, the model and the form are placed in the shopping cart app to allow the form to be submitted to check for validation without interfering with the order form in the checkout app.<br>

Superusers (store owners) are granted permission to create, update, and delete discount codes, as well as manage settings to activate or disable discount codes temporarily.

**Relationship with Order model:** The Order model includes a foreign key to the DiscountCode model, allowing for easy access to the discount code applied to the order.<br>

![ERD DiscountCode model](/documentation/erd-discount-code.png)
![ERD DiscountCode model constants](/documentation/erd-discount-code-constants.png)

**Order Management:** The model Order stores all necessary information for a store order. The model OrderItem associates the products with orders. The models are placed in the checkout app<br>  

Superusers (store owners) are granted permission to view and add new orders, as well as editing essential order details post-purchase, including contact information, delivery addresses, and discounts applied. This flexibility is particularly useful for correcting errors or accommodating changes requested by customers.<br>

Non-Editable Order Items: For security and integrity, the individual items within each order are presented inline but are marked as read-only. This prevents accidental modifications to the items ordered.<br>

These extensive permissions empower superusers to maintain and optimize the application's functionality, ensuring smooth operations and customer satisfaction.

The model OrderItem associates the purchased products with orders. Furthermore, it stores the product name and price at the time of order in case of changes in product name, price or if a product is deleted to maintain data integrity of the order history. These values are passed to the model in the checkout view.

**Integrated Payment Processing:** The system facilitates secure online transactions for product purchases by integrating with Stripe, a payment gateway provider. This ensures a seamless and secure user experience during checkout.

**Relationship with Product, DiscountCode and UserProfile models:** The Order model establishes relationships with the models Product in app products, DiscountCode in app cart, and UserProfile in app profiles (see ERD). This facilitates data retrieval and management of purchase history for both users and store administrators.

![ERD checkout](/documentation/erd-checkout.png)

**Payment Security**

**Stripe Integration:** By leveraging Stripe's secure payment infrastructure, the application safeguards sensitive financial information during transactions. This ensures user trust and adheres to industry-standard security protocols.

**Data security Measures** 

**CSRF Protection:** To safeguard against Cross-Site Request Forgery (CSRF) attacks, the application enforces the use of CSRF tokens in all forms using the POST method. This bolsters data integrity and prevents unauthorized actions.

**User Management**

**Django Allauth Integration for User Management:** User authentication and authorization are implemented by leveraging the Django Allauth, a third-party library that upholds robust security practices. This provides a robust and secure foundation for user access control.

**UserProfile model:** The UserProfile model is used to store user data. This includes user name, email, and password. The model is placed in the profiles app. To differentiate the information stored in the UserProfile model from the similar information stored in the Order model, the fields have the prefix default. Users can place an order without signing up for an account.<br>

The custom model field video_unlocked is a boolean field, used to detect if a registered user has purchased a video tutorial and has access the video's url in their user profile page on the website. The boolean field is triggered in the webhook handler in the checkout app.

**Relationship with Order and Contact models:** The UserProfile model establishes relationships with the models Order and Contact in app checkout and contact, respectively. This facilitates data retrieval and management of user contact information and purchase history.<br>

![ERD UserProfile](/documentation/erd-userprofile.png)

**Communication**

**Contact Form:** Users can contect the store owner using a contact form on the website. The form is placed in the contact app, and the model is used to store the form data. The contact form guides user through all necessary details for the store owner to make a detailled offer on a customized surfboard.<br> 

The form can just as easily be used to send a simple enquiry, feedback or a question to the store owner. <br>

The user receives a copy of the message by email and the store owner is notified by email of the new message. <br>

**Relationship with UserProfile model:** The Contact model establishes relationships with the UserProfile model in the app profiles (see ERD). This facilitates data retrieval of contact information to conveniently prefill the user's contact information in the form.

![ERD Contact Model](/documentation/erd-contact.png)

![ERD Contact Model CONSTANTS and ForeignKey](/documentation/erd-contact-constants-fk.png)

<span id="anchor-newsletter"></span>
**Newsletter:** This custom model provides a way to draft, finalize, and send newsletters to subscribers. The STATUS choices for the Newsletter model provide a workflow for managing the creation and sending of newsletters. After a newsletter is sent, the data and time of the sending is applied, and the status is set to “Done and Sent”. This can also be manually applied in case the newsletter was sent directly from the email account as opposed to via the admin interface. Setting the newsletter status to “Save and Send Newsletter Now” saves and sends the newsletter to all subscribers.

**Subscriber:** This custom model represents a user subscribed to the newsletter. The model collects only email address and no other personal data, such as name or phone number, which is not strictly necessary for the purpose of signing up for a newsletter. This adheres to  the EU General Data Protection Regulation’s (GDPR) principle of data minimization and to respect the data privacy of users, who are reluctant to give their personal information and might not sign up. The unique email address ensures that each subscriber can only sign up once.

The user must explicitly agree to receiving the newsletter and the boolean field defaults to “False” for an unchecked checkbox in accordance with the EU GDPR.

For each subscriber, an **unsubscribe token** is generated and allows for the secure handling of unsubscribe. This token is created using Python’s secrets function with 48 characters, ensuring a unique and secure token for each subscriber. This is to avoid malicious unsubscribing of subscribers using loops. The token is not regenerated to avoid conflicting tokens that may negatively affect UX when trying to subscribe using an expired token. Regenerating unsubscribe tokens at certain time points does have security benefits and would be considered for a larger scale project. Activating the unsubscription token deletes the subscriber’s email address permanently from the database, since there is no need to keep records and delete the data at a later time point as is permitted by the GDPR.

A confirmation email is sent to the subscriber containing the unsubscribe token and a discount code as a small token of appreciation for subscribing. The personalized unsubscribe token is sent to each subscriber as well as in every newsletter. There is no confirmation of subscription necessary since that is beyond the scope of this project. The user is informed and equipped with the necessary means to object and unsubscribe immediately in case of a change of hearts or unintentional subscription.

![erd-newsletter](/documentation/erd-newsletter.png)

**About Us**

**About Us Page:** The About Us page contains information about the store owner and the website goal. The page is placed in the about app, and the model is used to store the page content.

**Custom Surfboard:** The Custom Surfboard page contains a collection of custom surfboards created by the store owner. The page is placed in the about app, and the model is used to store the page content. Although there is no entity relation between the models, the CustomSurfboard model enhances the Contact model, which aims to collect information from customers for a customized surfboard.

**FAQs:** The FAQs page contains frequently asked questions and answers. The page is placed in the about app, and the model is used to store the page content. Websites that include a FAQs page can enhance the credibility and authority of the website content, which search engines like Google value and thereby beneficial for SEO.

**Resources:** The Resources page contains links to reliable sources on environmental and ocean conservation. The page is placed in the about app, and the model is used to store the page content. Websites that include external links to reputable sources can enhance the credibility and authority of the website content, which search engines like Google value and thereby beneficial for SEO.

![ERD About Us](/documentation/erd-about.png)

### Agile Development Methods (Epics, User Stories, MoSCoW Prioritization, Kanban board)

This project utilizes Agile Development Methods to manage development and ensure efficient delivery.

#### Epics 

These represent the high-level objectives and functionalities of the project. Each one can be further decomposed into smaller, more manageable tasks described in the user stories. The user stories can be viewed on [this project’s Kanban board](https://github.com/users/g-omarsdottir/projects/5).

#### User Stories

These detailed descriptions outline functionalities from the user's perspective. They follow the format "As a [role], I can [capability] so that [received benefit]". Each user story has well-defined acceptance criteria outlining the specific requirements for successful implementation. The user stories can be viewed on [this project’s Kanban board](https://github.com/users/g-omarsdottir/projects/5).

#### The MoSCoW Prioritization Method

To effectively manage resources and development flow, based on urgency and necessity, the prioritization method MoSCoW was employed. The acronym stands for Must Have, Should Have, Could Have, and Won't Have. 

**Must Have:** Features absolutely essential for the current iteration's functionality and guaranteed to be delivered.<br>
**Should Have:** Desirable features that add significant value to the current iteration but can be reconsidered if needed.<br>
**Could Have:** Features that would be nice to have but can be deferred for later iterations without impacting core functionality.<br>
**Won't Have:** Features that are not a priority for the current iteration and are excluded from the current scope, possibly not implemented at all.<br>

This method is a structural approach to determine which features are essential for the current stage (Must Have), which can be incorporated if time allows (Should Have), which might be deferred for later iterations (Could Have), and which are excluded from this iteration or unlikely to be implemented (Won’t Have). The priorities are reflected with **labels** on each user story on [this project’s Kanban board](https://github.com/users/g-omarsdottir/projects/5).

#### Kanban Board for Visual Workflow Management

The Kanban board is a handy tool in agile project management to provide a clear visual representation of the project planning and development workflow. This board displays the various stages each work item progresses through, along with the current status of individual tasks. This project’s Kanban board can be viewed [here](https://github.com/users/g-omarsdottir/projects/5).

## Features

### Main Features

### Custom Error Pages

The project a custom HTML error page for status codes 403 (Forbidden), 404 (Not Found) and 500 (Internal Server Error) for improved user experience. The error page maintains a consistent design with the rest of the website. The error pages clearly explains the meaning of the error code in a user-friendly way avoiding technical jargon and uses clear, concise language. The error pages display a friendly image in line with the website theme to make the error page more visually appealing.<br>

To style the error pages during development, the error pages were rendered using temporary views and urls placed in the profile app for easy testing. The approach is documented in [TESTING.md](TESTING.md).

![custom error pages](/documentation/feature-error-pages.png)

### Discount Code

The discount code can be obtained by subscribing to the newsletter and for future features in advertising campaigns. The discount code and the amount is displayed to the user in the shopping cart. The user can remove the discount code, e.g. to enter a different discount code, if they wish to.

![discount code](/documentation/discount-code.png)

If a different discount code is entered without removing the previous discount code, the new discount is applied and the previous discount is automatically removed.

![discount code replace](/documentation/discount-code-replace.png)

The discount code is stored in the order as well for better overview for customer and store owner.

![discount code](/documentation/discount-order-history.png)

### Tutorials

Users can browse tutorials and purchase with the integrated purchase system by stripe. The button on the side brings users to the top of the page.

![feature tutorials](/documentation/feature-tutorials.png)

Clicking anywhere on the card opens up the tutorial detail. The user can put the tutorial in the shopping cart or return to overview using the buttons.

![feature tutorials detail](/documentation/feature-tutorials-detail.png)

### About Us

The user can read about the store owner and gain trust in the product. Links to other pages are anchored in the description and invitation to sign up for the newsletter.

![feature about us](/documentation/feature-about-us.png)

![feature about us links](/documentation/feature-about-us-links.png)

![feature about us links 2](/documentation/feature-about-us-links-2.png)

### Collection of Surfboards

The user can view a collection of previous work made by the store owner. Clicking anywhere on the card opens up a detailed view of the surfboard. Since these custom surfboards are **not included in the ecommerce purchasing system**, the page is placed in the about us app to distinguish between the two types of products.

A scroll-to-top button is placed at the bottom of the list view to return to the top of the page when clicked.

![feature surfboards](/documentation/feature-surfboards.png)

In the detailed view of a surfboard, the user can send an enquiry about the surfboard by clicking the link. The user is then forwarded to the contact page. Or to return to the overview, the user can click the button.

![feature surfboard detail](/documentation/feature-surfboard-detail.png)

### Frequently asked questions (FAQ)

The user can view frequently asked questions. Including a FAQ page is a common practice to improve SEO results.

![feature faq](/documentation/feature-faq.png)

### Newsletter

The user can **subscribe** to the newsletter by entering an email address into the input field. The input field is autofocused for conveniency. Only the email address is collected, adhering to the EU GDPR's data minimization principle.

![feature-newsletter-signup](/documentation/feature-newsletter.png)

The input field has basic backend **email validation** for correctness and database comparison with existing subscribers. The user is notified and errors in the form are cleared using JavaScript for improved UX.

The user must **accept the terms** to subscribe.  

![feature-newsletter-validation](/documentation/feature-newsletter-validation.png)

The terms for subscription are described in the **disclaimer** and **privacy policy**, which open in a **modal** without refreshing the page to not to disrupt the UX.

The content of the privacy policy is filled into the modal from the source document using JavaScript, ensuring best practices that in case of changes, the content is only edited in one place and always up to date on all pages.

![feature-newsletter-modals](/documentation/feature-newsletter-modals.png)

The user receives a confirmation displaying the **discount code**. The confirmation, discount code as well as a **personalized link to unsubscribe** is **sent by email** to the subscribed email address.

![feature-newsletter-success page](/documentation/feature-newsletter-success.png)

If there is currently no discount code active or the discount code cannot be retrieved for other reasons, the user is notified by a message in the browser and by email of technical issues. The user is encouraged to contact the store owner for a functional discount code.

![feature-newsletter-discount-error](/documentation/feature-newsletter-discount-error.png)

**Secure unsubscribe process** is implemented using unique tokens for each subscriber. One-click unsubscription permanently removes subscriber data, ensuring GDPR compliance.

![feature-newletter-unsubscribe](/documentation/feature-newsletter-unsubscribe.png)

Please see a detailed description of data privacy in accordance with the GDPR, security measures for subscribing and unsubscribing, as well as the procedure and options to send the [newsletter in the communication section of the data base schema section](#anchor-newsletter).

**Newsletters can be drafted, finalized, and sent** with status tracking directly from the admin interface using gmail API.

#### Promoting the Newsletter on the website: 

The newsletter subscription page is prominently linked and can be accessed at any time with one click, without invasively blocking the users screen at any point for imporoved UX. 

- **As a link in the footer**:

  ![feature-newsletter-footer](/documentation/feature-newsletter-footer.png)

- As a **banner** on the tutorials page: 

  - **Subtle animation:** slow slide down with a gradient glow that fades.

    ![feature-newsletter-banner](/documentation/feature-newsletter-banner.png)

  - **Conditional display:** 
    - If a registered user has already subscribed to the newsletter, the banner is not displayed to avoid visual clutter (products / views.py). 
    - Banner text: Subheading only displayed on medium screens and up.

    ![feature-newsletter-subheading](/documentation/feature-newsletter-subheading.png)

  - **Accessibility:** The whole surface of the banner is clickable to navigate to the newsletter subscription page for improved UX, especially people with motor disabilities.

- As an item on the **navigation bar** under the section about us:

  ![feature-newsletter-navbar](/documentation/feature-newsletter-navbar.png)

- As a **link** in the website's content where fitting:

  ![feature-newsletter-prom](/documentation/feature-newsletter-prom.png)

### Resources

The user can view an overview with reliable resources related to the store content with a short description, which can improve SEO results. Clicking anywhere on the card opens up the link in a new window.

![feature resources](/documentation/feature-resources.png)

### Shopping Cart

The user can place tutorials in the shopping cart and is notified of the action. The successmessage disappears after a while, since this took up a lot of the screen realestate on mobile screens, but the cart preview stays open for a convenient checkout.

![feature userfeedback cart](/documentation/feature-userfeedback-cart.png)

The user can remove the item from the cart, apply a discount code before continuing on to secure checkout, or return to overview using the buttons.

![feature cart](/documentation/feature-cart.png)

The user cannot place more than one amount of the same tutorial in the shopping cart to avoid mistakes since it is a digital product. Mistakes can negatively impact UX and mean time consuming corrections of invoices for the store owner.

![feature cart](/documentation/feature-cart-double.png)

### Contact Form

If the user is logged in, the contact form is prefilled for their convenience with the data from their profile. The user can also enter a different email address or name if they wish to.

![feature contact prefill](/documentation/feature-contact-prefill.png)

The contact form is designed to obtain necessary information from users interested in buying a surfboard. The user can fill out the form and send it to the store owner, and choose to only fill out the required fields, name and email address. 

Displaying the whole contact form at once, instead of toggling parts of it as needed, may spark interest in ordering or building a surfboard. Skilled surfers, who are are primary target group for selling custom made surfboards, will recognize the attention to detail and others may appreciate the guidance through the complicated process of calculating a surfboard’s parameters based on the surfer and its intended use. This can help build trust in the website and in the products.

![feature contact form](/documentation/feature-contact-form.png)

### User Profile

**CRUD functionality: Create** <br>
The user can **create** an account by signing up. For convenience, the user can save the personal information to their profile, which they entered during the checkout process when purchasing a tutorial.

![Feature userprofile save info](/documentation/feature-userprofile-save.png)

**CRUD functionality: Read** <br>
The user can view their order history and click on the link to view the original full order confirmation. 

![feature profile orderhistory](/documentation/feature-profile-orderhistory.png)

**CRUD functionality: Update** <br>
The user can manage their profile information by clicking the button. Here they can **update personal information**. 

If the email address associated with the user account is updated, the system implements a security measure:
- Notification emails are sent to both the previous and new email addresses.
- This serves as a precautionary step to alert the user of the change.
- Users are advised to contact the store owner if they didn't initiate this change themselves.

Security and User Experience Considerations: 
- If the email sending process fails, the user is not notified of this failure. 
- This design choice prevents disruption to the user experience and avoids potential confusion. 
- Django allauth's password and authentication settings are configured to safeguard against brute force attacks.

The notification system demonstrates respect for user data protection, enhances trust in the website's security measures, and provides an additional layer of account security.

![feature profile manage](/documentation/feature-profile-manage.png)

**CRUD functionality: Delete** <br>
The user can **delete the user profile** permanently from the database. If they wish to delete the profile, they must confirm the deletion before proceeding.

![feature profile delete](/documentation/feature-profile-delete.png)

Of course, the user can **cancel** and return to their user profile without taking any action.

The user can access the links to the **purchased tutorials in the userprofile**.

![feature user profile](/documentation/feature-profile.png)

### Order confirmation

The user receives an order confirmation with all details and a link to the purchased tutorial.

![feature order confirmation](/documentation/feature-order-confirmation.png)

### Purchased Tutorial

The user can click on the link in the order confirmation and view the tutorial hosted on youtube (not listed for public view). The title of each tutorial is displayed in the beginning and fades out while the video plays. The video itself is a similation for the tutorial.

![feature watch purchased tutorial introduction](/documentation/feature-vid-building.png)

![feature watch purchased tutorial shortboard](/documentation/feature-vid-shortboard.png)

![feature watch purchased tutorial boyancy](/documentation/feature-vid-boyancy.png)

### Search Bar

Users can enter a search query for the tutorials into the search field in the header, with the placeholder "search tutorials". The search displays all tutorials with the query in the titel or description.

![feature search](/documentation/feature-search.png)

If the search query does not match any of the tutorials, the user is notified and redirected to the the tutorials overview pagae.

![feature search no result](/documentation/feature-search-noresult.png)

### Responsiveness

Full responsiveness was achieved using Bootstrap's grid system. The website is designed to be viewed on a desktop, laptop, tablet or mobile device.

### Security

#### User Authentication and Authorization

The application ensures secure user authentication and authorization through the integration of Django Allauth. This powerful tool simplifies the process of managing user accounts, including registration, login, password reset, and email verification. By utilizing Django Allauth, the project adheres to best practices for web application security, providing our users with a safe and reliable environment.

#### Access Control

To safeguard user data and privacy, stringent access controls were implemented . These measures are designed to restrict unauthorized access to sensitive information, ensuring that each user can only view or interact with their own content. 

#### Secure Payment Processing

For handling financial transactions, the project utilizes Stripe, a leading payment processing service. Stripe is renowned for its commitment to security, providing a seamless and secure way for users to make payments online. By integrating Stripe, all financial operations are ensured to be conducted in compliance with industry-standard security protocols, protecting both users and the store owner from potential threats.

In summary, the application prioritizes security at every level, from user account management to data protection and financial transactions simulation.

### Future Features

**Review & Rate Management:** As a future feature, the project envisions expansion to include a user-driven review and rating system for products. This enhancement aims to empower store owners with insights into customer preferences, identifying popular and less favored tutorials. Such information will facilitate strategic decisions regarding content expansion or refinement, ultimately guiding users towards making informed purchasing choices. <br>

While reviews and ratings are prevalent in ecommerce platforms, prioritizing this feature is beyond the current scope due to time limitations. The project's primary goal remains focused on raising awareness for ocean conservation efforts and showcasing the unique, custom-shaped surfboards crafted by the store owner. Given the distinct pricing challenges associated with custom-made products, these are not made available for purchase on the website. A review and rating system to enhance the platform incrementally is at the top list of future considerations.

## Web Marketing

### Ecommerce Business Model

The business model for this ecommerce website is a Business to Customer (B2C) model, currently only selling digital content for single one-time payments. <br>

This section elaborates on the ecommerce marketing value and SEO benefits of the project’s custom models.

The focus and main goal of this project is to create an ecommerce website with integrated purchase process and features that increase the marketing value and SEO benefits. The design of the technical architecture of the individual Django models was created to enhance web marketing efforts beyond the organic growth with social media marketing and reducing costs related to traditional advertising.

#### Products Models

The Product model and related Category and Subcategory models ensure a coherent and consistent use of terminology regarding the surfboard parameters throughout the website. 

**Marketing Value:** Consistent use of terminology makes a trustworthy and serious impression. This avoids misspelling in the product description, thus avoiding concerns about the store owner’s expertise, which could potentially reduce the market value.

**SEO Benefits:** Using predefined parameters reduces the risk of misspelling while creating the entry for the product, potentially leading to failed searches in search engines or on the website’s integrated search field.

#### Discount Code Model

**Marketing Value:** Discount codes incentivize users to subscribe to the newsletter, increasing brand awareness and potentially leading to repeat customers.

**SEO Benefits:** Discount codes can be promoted through social media and email marketing campaigns, driving traffic to the website.

#### Video Unlocked Field of the Profile model

**Marketing Value:** The video_unlocked field unlocks the access to a tutorial in the user's profile page, which is triggered during the purchase process of the tutorial (by the webhook handler at successful payment). This feature invites users a conveniently keep an overview of and access to their purchased tutorials on their profile page on the website. Repeated visits to the website and the thoughtful placement of buttons to browse through the collection of tutorials increases the likelihood to purchase further videos.

#### Contact Form Model

**Marketing Value:** The contact form facilitates communication with potential customers, allowing them to inquire about custom products or ask questions. Even if users did not visit the website to place an order for a custom-made surfboard by the store owner, they are likely to take interest in the  various details necessary to shape a custom-made surfboard and enticed to make an enquiry, which may lead to a sale.<br>

Connoisseurs will recognize the attention to detail and amateurs will appreciate the guidance through the complicated process of calculating a surfboard’s parameters with regard to the surfer and intended use, potentially enhancing the marketing value and increasing website traffic.

**SEO Benefits:** A well-designed contact form can improve user experience, which is a positive SEO ranking factor.

#### About Us Model

**Marketing Value:** The About Us page tells the brand story and builds trust with potential customers.

**SEO Benefits:** High-quality content on the About Us page can improve website authority and ranking for relevant keywords. The date of entry increases the seriousness of the website.

#### Custom Surfboard Model

**Marketing Value:** The Custom Surfboard page provides a collection of custom-made surfboards with elegant images for potential customers showcasing the store owner’s expertise. The detail view of a custom surfboard invites the user to visit the contact page to enquire about the surfboard, potentially leading to a sale of a custom surfboard or a tutorial for creative DIY users.

#### FAQ Model

**Marketing Value:** The frequently asked questions page provides valuable information to potential customers addressing their concerns and demonstrates the commitment to customer service and expertise in the field of environmental-friendly materials and reducing the carbon footprint of the surfboard industry. 

**SEO Benefits:** These pages target long-tail keywords related to custom surfboards, environmental conservation, and climate change mitigation, which are not only vital and utmost import, but also vouge and widely used search terms. Websites with a section for  frequently asked questions enhance the authority and seriousness of the website by search engines like google, thus improving organic search traffic.

#### Resources Model

**Marketing Value:** The Resources page demonstrate the commitment to environmental and ocean conservation causes, potentially resonating with environmentally conscious customers. 

**SEO Benefits:** Including external links to reputable and high-quality sources like the United Nations and the Intergovernmental Panel on Climate Change can enhance the credibility and authority of the website content, which search engines like Google value and thereby beneficial for SEO. The store owner can manually change the order of the resources on the website according to current popularity of search terms or environmental occurrences.

Overall, the project has the potential to expand to selling further products and physical goods, as the product category and subcategory models can be expanded by the store owner in the admin panel. The content displayed on the website can be updated according to current market trends and popular search terms.

### Marketing Strategies

### Social Media & Newsletter Marketing

Users are invited on a banner on the website to subscribe to the newsletter and obtain a discount code for a discount off their next purchase. The store owner can send a newsletter to the subscribers to increase the likelihood of the subscribers to purchase the products.<br>

The social media marketing strategy relies on organic growth. The facebook page is set up to promote the products through postings of new tutorials, images of new custom-made surfboards, and for discount code campaigns.<br>

Furthermore, it aims to be a source of information for the users, raise general aweareness regarding sustainable materials, environmental and ocean conservation causes, climate change mitigation and the environmental impact of the surfboard industry, life cycle analysis (LCA) and minimizing the carbon footprint through re-posting of posts by relevant reliable sources.<br>

The facebook page provides a link to the website, which can be used to promote the products and increase the likelihood of the users to purchase the products by users that land on the facebook page through posts related to environmental related topics.

![facebook-mockup](/documentation/facebook-mockup.png)

### Search Engine Optimization (SEO)

The website design was planned with SEO in mind. This is described in detail in the relevant ERD models.

#### Keywords

The metadata for this project has been carefully crafted to enhance search engine optimization (SEO) and improve discoverability. The overall approach to keyword selection and implementation is as follows:

**Keyword Development Process**

1. **Initial Brainstorming with fellow surfers and my sister, Geographer and Specialist in Geothermal Energies **: We began with a comprehensive brainstorming session to identify relevant terms and concepts related to our surfboard tutorials and eco-friendly surfing products. This ensured targeting the most effective terms for the niche.

2. **Google Search Analysis**: Related searches and suggestions provided by Google for initial terms, which helped uncover additional relevant keywords and phrases.

3. **Professional Consultation**: We consulted with SEO professionals to refine our keyword list and 

4. **Long-Tail Keyword Focus**: Emphasizes is on long-tail keywords to target specific user intents and capture more qualified traffic. These longer, more specific phrases often have less competition and higher conversion rates.

5. **Keyword Diversity**: A mix of both short-tail and long-tail keywords to create a balanced and comprehensive SEO strategy.

**Keyword Implementation**

- Keywords are strategically placed in meta descriptions, page titles, and content headers.
- A natural integration of keywords within the website content to maintain readability and user experience. Keywords were used in headings and in semantic and html `<strong>` tags.
- The metadata is structured to be both search engine friendly and informative to potential visitors.

#### Sitemap

[XML-Sitemaps.com](https://www.xml-sitemaps.com/) was used to generate the sitemap for the deployed project. The generator crawls the entire website and generates a sitemap.xml file that was downloaded and placed in the rootdirectory of this project. The sitemap is an XML file that contains a list of all the pages on the website. The sitemap is used by search engines to crawl the website and index the pages.

#### Robots.txt

The robots.txt file is a text file that tells search engines how to crawl the website. The robots.txt file is located in the root directory of the website. The robots.txt file is used to disallow certain pages from crawling by search engines and are not indexed by search engines.

The [Sitemap for this project](https://www.xml-sitemaps.com/details-shaping-sustainable-surf-8794b08a1b3a.herokuapp.com-da3dd3a88.html) is included in the robots.txt file.

In this project, the disallowed pages are the account pages and the shopping cart page.

The ownership of the robots.txt file is tested and verified by Google by adding a sitespecific metatag in the head of the base template. Google then veryfies if the robots.txt file is working correctly and provides a performance report after a short waiting time.

![ownership-verfied-html-tag](/documentation/testing/test-robots.txt.png)

### Privacy Policy

[Privacypolicygenerator](https://www.privacypolicygenerator.info/) was used to create the privacy policy for this project.

The privacy policy is rendered on the websites template to make it visually more appealing and make trustworthy impression on users. The privacy policy is located in the home app and is anchored in the footer of the website.

**GDPR Compliance:** If a website collects personal data from European Union residents, compliance with the General Data Protection Regulation (GDPR) is mandatory. A privacy policy is a key component of GDPR compliance, outlining how personal data is collected, processed, stored, and protected.
Trust Building: It builds trust with users by being transparent about what data is collected, how it's used, and for what purposes. 

**Riskmanagement:** In a real-life ecommerce project, having a clear privacy policy in place helps identify potential risks associated with data handling and processing. Addressing these risks proactively can prevent legal issues and reputational damage.

## Technology Used

### Languages Used

- Python
- HTML
- CSS
- JavaScript
- Markdown for this README.md and TESTING.md

### Libraries and Frameworks Used

In addition to libraries and frameworks already installed in the Code Institute template:

- [Django v3.2.25](https://docs.djangoproject.com/en/5.0/releases/3.2.25/) - Python web framework
- [django-allauth v0.63.3](https://docs.allauth.org/en/latest/installation/index.html) - User account authentication
- [black v24.4.2](https://black.readthedocs.io/en/stable/) - Formats code compliant to pep8
- [django-extensions v3.2.3](https://pypi.org/project/django-extensions/) - Show urls and location of installed packages
- [django-crispy-forms v2.2](https://django-crispy-forms.readthedocs.io/en/1.14.0/) - Simplifies the creation of forms
- [crispy-bootstrap v4](https://pypi.org/project/crispy-bootstrap4/) - Bootstrap-specific classes to style forms
- [django-resized v1.0.2](https://pypi.org/project/django-resized/) - Handles resizing and format converting of images uploaded by store owners
- [pillow v10.3.0](https://pillow.readthedocs.io/en/stable/) - A Python imaging library, handles images in combination with the Django Resized Image Field
- [django-summernote v0.8.20.0](https://github.com/summernote/django-summernote) - A a simple WYSIWYG editor to use SummernoteModelAdmin in the admin panel interface
- [django-richtextfield v1.6.2](https://pypi.org/project/django-richtextfield/) - Not actively used but unable to uninstall due to dependies of previous migrations of richtextfields (as suggested by CI tutor support)
- [cloudinary v1.40.0](https://cloudinary.com/documentation/django_integration) - Allows to upload product images
- [django-cloudinary-storage v0.3.0](https://cloudinary.com/documentation/rails_activestorage) - Provides storage of uploaded product images 
- [django-countries v7.6.1](https://pypi.org/project/django-countries/) -  Provides country choices for use with forms and a country field for models
- [stripe v10.1.0](https://docs.stripe.com/) - Provides secure payment processing
- [whitenoise v5.3.0](https://pypi.org/project/whitenoise/) - Python package to simplify static file serving for web apps
- [psycopg2 v2.9.9](https://pypi.org/project/psycopg2/) - PostgreSQL database adapter for the Python programming language
- [gunicorn v20.1.0](https://docs.gunicorn.org/en/20.1.0/) - Gunicorn serves as a Python WSGI HTTP server for UNIX, designed to interface with WSGI-compliant web applications to serve applications efficiently and reliably, handling multiple concurrent connections and requests optimisation (equivalent to manage.py runserver used in development for the deployed app)
- [django-autoslug==1.9.9](https://pypi.org/project/django-autoslug/) - Automatically generates slug field

### Programs Used
- [Canva](https://www.canva.com/) to create the website logo
- [Photoroom](https://www.photoroom.com/tools/background-remover) to remove background from images and website logo
- [Pixelied](https://pixelied.com/convert) to convert images to webp format
- [TinyPNG](https://tinypng.com/) to compress images
- [favicon.io](https://favicon.io/favicon-converter/) to create favicon from website logo
- [Leonardo AI](https://leonardoai.com/) to create the custom error pages images
- [Shields.io](https://shields.io/badges/) to create static badges for this README
- [YouTube](https://www.youtube.com/) for hosting the tutorial videos
- [Techsini.com](https://techsini.com/multi-mockup/index.php) to create the mockup for this README
- [Chrome Extension Ignor X-Frame headers](https://chromewebstore.google.com/detail/ignore-x-frame-headers/gleekbfjekiniecknbkamfmkohkpodhe) to be able to create a mockup on Techsini from a django project
- [Google Fonts](https://fonts.google.com/) for the website fonts
- [Google Gemini AI](https://gemini.ai/) for expanding the content of product descriptions
- [Coolors Contrast Checker](https://coolors.co/contrast-checker) for the color contrast check
- [Fontawesome](https://fontawesome.com/) for icons
- [Muzli Colors](https://colors.muz.li/palette/57a7b3/3d757d/b35794/7d3d67/b3a357) for color palette
- [Balsamiq](https://balsamiq.com/wireframes/) for wireframes
- [Privacypolicy Generator](https://www.privacypolicygenerator.info/) for the privacy policy
- [XML-Sitemaps.com](https://www.xml-sitemaps.com/details-shaping-sustainable-surf-8794b08a1b3a.herokuapp.com-da3dd3a88.html) for the Sitemap for this project
- [Code Institute Database Maker](https://dbs.ci-dbs.net/) for the database
- [Google Gmail](https://www.google.com/intl/de/gmail/about/) for website confirmation emails
- [Heroku](https://www.heroku.com/) for deployment
- [GitHub](https://github.com/) for storing repository
- [Gitpod](https://www.gitpod.io/) for development environment

## Deployment and Local Development

### Local Clone

To clone the repository:
- Log in to GitHub and navigate to the repository of this project.
- Click on the green button "Code" to open the dropdown menu, select "Clone with HTTPS, SSH or GitHub CLI" and copy the link provided.
- Open "Terminal" (or "Git Bash") in your code editor.
- Change the current working directory to the location where you want the cloned directory to be made.
- Type "git clone" in the terminal and then paste the URL copied on GitHub in step 2, above.
- Press "Enter" and your local clone will be created.
- Install requirements from requirements.txt using the command "pip install -r requirements.txt". If working in a virtual environment, activate the virtual environment before running the command.
- Create e.g. a .env or env.py to store sensitive information such as database URL, secret key, email API, cloudinary URL, stripe secret key and webhook handler secret.

### Fork

To fork the repository:
- Log in to Github and navigate to the repository of this project.
- Click the button "Fork" in the top right corner to open dropdown menu and select "Create a new fork".
- Install requirements from requirements.txt using the command "pip install -r requirements.txt". If working in a virtual environment, activate the virtual environment before running the command.
- Create e.g. a .env or env.py to store sensitive information such as database URL, secret key, email API, cloudinary URL, stripe secret key and webhook handler secret.

### Database

This project utilizes a PostgreSQL relational database from Code Institute for their students.

To connect to the database:
- Go to the [Code Institute Database Maker](https://dbs.ci-dbs.net/)
- Create a database using the email address used to sign up for the Code Institute LMS.
- The Database URL is sent to the email address.
- Add the database URL as a variable to the project and make sure to keep it secret, by e.g. adding it to a .env or env.py file included in .gitignore, and therefore not pushed to your repository or publicly displayed in your code.

### Cloudinary

This project utilizes Cloudinary, a cloud-based storage and Content Delivery Network (CDN) solution, to host and serve static media files such as images. 

Cloudinary storage ensures scalability as it accommodates growth in media volume, ensuring the project can handle future increases in media assets without compromising performance.

To connect to cloudinary:
-	Log into or sign up for a Cloudinary Account.
-	Navigate to "development" to obtain the necessary credentials, the API secret key and cloudinary URL.
-	Install cloudinary and cloudinary-storage packages and integrate to the Django project by configuring these in the settings.py file.
-	Add the cloudinary URL as a variable to the project and make sure to keep it secret, by e.g. adding it to a .env or env.py file included in .gitignore, and therefore not pushed to your repository or publicly displayed in your code. 

### Stripe

This project uses [Stripe](https://docs.stripe.com/) to handle the secure payment process in test mode.

To connect to Stripe API:
- Log into or sign up for a stripe account.
- Navigate to "Developers" on the top page menu.
- In the section "API keys", select "Get your test API keys".
- You will find two keys necessary to connect your project: 
  - STRIPE_PUBLIC_KEY = Publishable Key (starts with pk)
  - STRIPE_SECRET_KEY = Secret Key (starts with sk)
- In case users prematurely close the purchase-order page or internet connection fails during payment processing, it is important include Stripe Webhooks.
- Navigate to "Developers" on the top page menu.
- In the section "Webhooks", select "Add Endpoint".
  - Add the webhook URL.
  - Select "Receive All Events".
  - Click the button "Add Endpoint" to complete the process.
  - You will find one key under signing secret.
    - STRIPE_WH_SECRET = Signing Secret (Wehbook) Key (starts with wh)
- Install the stripe package and integrate to the Django project by configuring it in the settings.py file.
- Add the link to [stripe's JavaScript](https://docs.stripe.com/js) in your base html template to make security features from stripe available throughout the website for maximum security.
- Add core JavaScript from the stripe documentation necessary to [accept a payment](https://docs.stripe.com/payments/accept-a-payment).
- Stripe elements style is customizable to adhere to the ovarall [style of the website](https://docs.stripe.com/elements/appearance-api).
- Add the keys as variables to the project and make sure to keep the secret keys secret, by e.g. adding it to a .env or env.py file included in .gitignore, and therefore not pushed to your repository or publicly displayed in your code.

### Google Mail (Gmail) API

This project uses [Gmail](https://mail.google.com/) to handle email communication with users for account verification and order confirmations.

To connect to Gmail API:
- Create a Gmail (Google) account obtain the API key and connect your project.
- Log into or sign up for a Google Gmail account.
- Navigate to "Account Settings" (cog icon) in the top-right corner of Gmail.
- Select "Accounts and Import".
- Within the section called "Change account settings", click on the link for Other Google Account settings.
- From this new page, select "Security" on the left.
- Select 2-Step Verification to activate and follow the instructions to verify your password and account.
- Once verified, select "Turn On" 2-factor authentication (2FA).
- Navigate back to the "Security" page and select "App passwords".
- This might prompt you once again to confirm your password and account.
- Select "Mail" as "App Type".
- Select "Other (Custom name) " for the "device type".
- Add custom name,  e.g. project’s name.
- You'll be provided with a 16-character password (API key).
  - Tip: store this key safely, as you cannot access this key again!
  - EMAIL_HOST_PASS = user's 16-character API key.
  - EMAIL_HOST_USER = user's own personal Gmail email address.
- Add the pass and the host as variables to the project and make sure to keep them secret, by e.g. adding it to a .env or env.py file included in .gitignore, and therefore not pushed to your repository or publicly displayed in your code. 

### Deployment using Heroku

To deploy the repository:
- Log into or sign up for a Heroku account.
- Navigate to the dashboard.
- Navigate to the button "New" in the top right corner and select "Create New App" from the navigation dropdown menu.
- Enter a name for the app. The name of the app must be unique and cannot be identical to any other app deployed by other users on Heroku.
- Select your region, "United States" or "Europe", from the navigation dropdown menu.
- Click on the button "Create App".
- Navigate to "Deploy" on the top navigation menu, scroll down to "Deploy Method" and connect the repository with GitHub.
- Navigate to "Settings" on the top navigation menu.
- In the section "Config Var", click on the button "Reveal Config Vars".
- Click on "Add a new Config Var" and add the necessary keys and values.
    - SECRET_KEY with the value of the secret key.
    - DATABASE_URL with the value of the database URL.
    - CLOUDINARY_URL with the value of the cloudinary URL.
    - STRIPE_SECRET_KEY with the value of the secret key.
    - STRIPE_PUBLIC_KEY with the value of the public key.
    - STRIPE_WH_SECRET with the value of the webhook handler secret key.
    - EMAIL_HOST_PASS with the value of the API key.
    - EMAIL_HOST_USER with the value of the email address.
- Navigate to section "Deploy" on the top navigation menu.
- Select "GitHub" as the deployment method.
- Search for the repository to be deployed by using the search bar and click "Connect".
- Select the repository branch to be deployed.
- Choose "Manual" deployment.
    - Manual deployment must be manually re-deployed after pushing new changes to the repository.
    - Crucial when working with DEBUG=True during development.
- Click the button "View" to open the link to the deployed project.

## Credits

### Content

All content is written by me, Gudrun Omarsdottir, unless explicitly otherwise stated.

- Stripe Official documentation for code snippets necessary for implementing the Stripe payment process:
  - [Core JavaScript functunalities from stripe](https://stripe.com/docs/payments/accept-a-payment).
  - [Core CSS style from stripe](https://stripe.com/docs/stripe-js).

Inspiration and debugging help from:

- Django framework official documentation, in particular:
  - [Django Docs](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#inlinemodeladmin-objects) for the Django admin site.
  - [Django Docs](https://docs.djangoproject.com/en/2.2/ref/signals/) and [Reddit](https://www.reddit.com/r/django/comments/cerq2k/how_to_editing_the_add_modelsave_button_in_the/) for simple solution to handle calls to trigger sending newsletter from the admin interface and from signal for front-end functionality.

- The Code Institute walkthrough project Boutique Ado for inspiration for the basic website structure.
- Stack Overflow Community 

### Imagery

- [Canva](https://www.canva.com/) - Website logo and favicon
- [Faviocon.io](https://favicon.io/favicon-converter/) to convert logo into favicon
**Pexels.com:**
- [Video for Tutorials](https://www.pexels.com/video/man-painting-a-surfboard-854124/)
- [Photo by Kampus Production](https://www.pexels.com/photo/man-in-wetsuit-pointing-finger-at-camera-5904824/)
- [Photo by Harold Granados](https://www.pexels.com/photo/a-man-in-green-shirt-shaping-a-surfboard-10000115/)
- [Photo by Nataliya Vaitkevich](https://www.pexels.com/photo/happy-woman-holding-a-surfboard-4944641/)
- [Photo by Lachlan Ross](https://www.pexels.com/photo/crop-man-planing-wooden-surface-of-surfboard-5967744/)
- [Photo by Grégory Costa](https://www.pexels.com/photo/a-tattooed-person-holding-a-pencil-7763823/)
- [Photo by Lachlan  Ross](https://www.pexels.com/photo/crop-artisan-shaping-surfboard-in-workshop-5967749/)
- [Photo by Vincent Rivaud](https://www.pexels.com/photo/blue-and-white-surfboard-2876747/)
- [Photo by Yaroslav Shuraev](https://www.pexels.com/photo/view-of-three-people-surfing-1553959/)
- [Photo by Dalila Dalprat](https://www.pexels.com/photo/woman-holding-surfboard-and-posing-outdoor-1852621/)
- [Photo by Vladimir Kudinov](https://www.pexels.com/photo/man-in-white-surfboard-67386/)
- [Photo by alexandre saraiva carniato](https://www.pexels.com/photo/photography-of-man-surfing-2103783/)
- [Photo by Lucas Meneses](https://www.pexels.com/photo/person-surfing-on-green-water-6144077/)
- [Photo by Jess Loiterton](https://www.pexels.com/photo/a-woman-wearing-swimsuit-doing-surfing-5231936/)
- [Photo by Jess Loiterton](https://www.pexels.com/photo/woman-in-pink-bikini-surfing-on-water-4321800/)
- [Photo by Jess Loiterton](https://www.pexels.com/photo/aerial-view-of-people-swimming-on-sea-4327786/)
- [Photo by Jonathan Borba](https://www.pexels.com/photo/young-woman-waxing-a-surfboard-19596861/)
- [Photo by Ging Ang](https://www.pexels.com/photo/close-up-photo-of-person-carrying-surfboard-1753689/)
- [Photo by Ann H](https://www.pexels.com/photo/word-reduce-made-up-of-wooden-letters-20698129/)
- [Photo by Guy Kawasaki](https://www.pexels.com/photo/man-surfing-1654484/)
- [Photo by Jeremy Bishop](https://www.pexels.com/photo/sea-nature-water-wave-2397652/)
- [Photo by Jess Loiterton](https://www.pexels.com/photo/woman-in-black-bikini-sitting-on-white-surfboard-on-blue-sea-5006582/)
- [Photo by Jess Loiterton](https://www.pexels.com/photo/person-in-red-and-white-kayak-on-blue-body-of-water-4321465/)
- [Photo by Pixabay](https://www.pexels.com/photo/person-surfing-416676/)
- [Photo by Mudassir Ali](https://www.pexels.com/photo/aerial-photography-of-person-surfing-1556796/)
- [Photo by Kammeran Gonzalez-Keola](https://www.pexels.com/photo/turtle-swimming-in-the-sea-17822918/)
- [Photo by Emiliano Arano](https://www.pexels.com/photo/photography-of-barrel-wave-1298684/)
- [Photo by Kammeran Gonzalez-Keola](https://www.pexels.com/photo/inside-of-a-turquoise-wave-13317495/)
- [Photo by Kammeran Gonzalez-Keola](https://www.pexels.com/photo/man-riding-surfboard-in-wavy-ocean-7925859/)
- [Photo by Yabi Oregi](https://www.pexels.com/photo/flags-of-countries-in-front-of-the-united-nations-office-at-geneva-16459372/)

### Acknowledgements

- My mentor, Mitko Bachvarov, for his guidance and encouragement.
- My sister, Malfridur Omarsdottir, Geographer and Specialist in Geothermal Energies, for brainstorming for keywords, proofreading content and fact checking on eco-friendly sustainable materials and links to relaiable resources.
- My friend Stephan Reich, Software Developer, for his support and advice.
- My fellow student at Code Institute [Amir Schkolnik](https://github.com/AmirShkolnik) for his valuable support with proofreading.
- My Code Institute class facilitator, Kristyna Wach, for her cheerful motivation and encouragement.
- Slack community for support and advice.
- Stackoverflow community for information.