# ![logo](/documentation/logo_wave.png) Shaping Sustainable Surf

![mockup](/documentation/mockup.png)

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

Welcome to Shaping Sustainable Surf.

## Project Goal

This is my final project of the full-stack software development diploma at Code Institute. It is a fully functional Django ecommerce web application that offers access to online video tutorials for surfers and shapers, who want to acquire or progress their surfboard shaping skills while minimizing their environmental impact. 

The name "Shaping Sustainable Surf" draws a parallel to the process of crafting a surfboard, which is called shaping and reflects the dual mission: crafting eco-friendly surfboards and shaping a more sustainable future for the sport by promoting eco-friendly practices and education.

## User Experience

### Target Group

- Eco-conscious surfers and shapers.
- People seeking to learn or improve surfboard shaping skills using eco-friendly materials.
- DIY enthusiasts interested in sustainable surfboard shaping.

### Visitors Goals

#### First-Time Visitor Goals

As a first-time visitor, I can

-	Enjoy the visually appealing homepage.
-	Quickly understand the website's core offering.
-	Navigate easily to find relevant information.
-	Explore and purchase video tutorials.
-	Learn about sustainable surfboard shaping and eco-friendly materials.
- View examples of sustainable surfboards.
- Sign up for the newsletter.
- Contact the store owner for custom surfboard enquiries using the contact form.

#### Returning Visitors Goals

As a returning visitor, I want to

-	Access new tutorials and content.
-	Seek inspiration from custom-made sustainable surfboard gallery.
-	Sign up for a newsletter because so that I can participate in the Q&A sessions announced in the newsletter.
-	Contact the store owner for advice on ongoing projects.

#### Frequent Visitors Goals

As a frequent visitor, I want to

-	Check for new tutorials and information on eco-friendly materials.
-	Check for updates to the custom-made surfboard gallery.
-	Contact the store owner for advice and give feedback.

## Design

### Layout

The layout of the website is divided into two areas: one for all visitors and another for logged-in users, as dipicted in the flowchart below.

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

The website's colors are inspired by the blue ocean waves and whitewater, centered around the blue #57a7b3 used in the website logo.

Using a complimenting colorpalette from [Muzli Colors](https://colors.muz.li/palette/57a7b3/3d757d/b35794/7d3d67/b3a357), accent colors are strategically applied to box-shadows and hover effects to keep the overall layout sleek and avoid visual clutter.

![colors](/documentation/colors.png)

The font color is a warm tone of black and background color is white, ensuring excellent contrast for accessability and readability, while being easy on the eye.

[Coolors Color Contrast Checker](https://coolors.co/contrast-checker/333333-ffffff) score:

![contrast checker](/documentation/color-contrast.png)

### Typography

Font types were chosen to create a clean and modern look with a focus on readability.

**Primary Font:** [Roboto Flex](https://fonts.google.com/specimen/Roboto+Flex) a variable font used for body text, offering versatile weight options.

![Primary Font](/documentation/typography-primary.png)

**Heading Font:** [Roboto Slab](https://fonts.google.com/specimen/Roboto+Slab?query=roboto+slab) a serif font with subtle decorative details, establishing clear visual hierarchy.

![Heading Font](/documentation/typography-heading.png)

## Project planning

### Database Schema

This project uses Neon database, a serverless PostgreSQL database for efficient data management. The development was guided by a pre-defined **Entity Relationship Diagram (ERD)** (see below), which streamlined the development process and reduced database complexity. Each model in the project corresponds directly to a table in the ERD, ensuring a clear and consistent data structure.

#### Technical Architecture

**Model-Based Design:** Key components are separated into individual Django Models (see ERD), adhering to separation of concerns principles. This promotes code clarity, maintainability, and scalability.

**Relational Data Modeling:** The ERD visualizes relationships between models and model fields, enabling efficient database queries using primary keys.

**App Structure:** Each ERD represents a Django app, with inter-app model relationships indicated where applicable.

#### Key Features

**Product Management:** 
- Products, Categories and Subcategories are stored in separate models, which allows for scalability and streamlines further technical design. 
- Consistent terminology is guaranteed throughout the application to enhance user experience and simplify search queries by pre-defining constants within the models.
- This approach allows for a streamlined shopping and purchase process.
- Administrators (store owners) have comprehensive permissions to manage content and product data across the platform, including creation, updates, deletion, and pricing adjustments.

![ERD Product model](/documentation/erd-product.png)

![ERD Product model constants](/documentation/erd-product-constants.png)

**Ecommerce Functionality**

**Discount Codes:** 
- DiscountCode model in the Cart app manages and validates discount codes.
- Validation checks include code existence in the database and current active status.
- Placement in the cart app allows for code validation without interfering with the checkout process.
- Adm can create, update, delete, and manage discount codes, including temporary activation/deactivation.

**Relationship with Order model:** 
- Order model in the Checkout app links to the DiscountCode model via a Foreign Key.
- Enables quick reference to applied discounts for each order (see ERD for Order model below). 

![ERD DiscountCode model](/documentation/erd-discount-code.png)
![ERD DiscountCode model constants](/documentation/erd-discount-code-constants.png)

**Order Management:** 
- Models are placed in the Checkout app.
- Order model stores essential order information. 
- OrderItem model links products to orders and stores product details at time of purchase.
  - This feature maintains data integrity of the order history in case of changes in product name, price or deletion. 
- Administrators (store owners) have permission to 
  - View and add new orders
  - Edit post-purchase order details stored in the Order model (contact information, delivery addresses, and discounts applied)
  - View order items stored in the OrderItem model (read-only to maintain order integrity)
- These features ensure data integrity, operational flexibility, and customer satisfaction

**Relationship with Product, DiscountCode and UserProfile models:** 
- Order model links to the models:
  - Product (placed in the Products app)
  - DiscountCode (placed in the Cart app) 
  - UserProfile (placed in Profiles app)
- This structure facilitates data retrieval and management of purchase history for users and store administrators.

![ERD checkout](/documentation/erd-checkout.png)

**Integrated Payment Processing:** 
- The application uses secure online transactions for product purchases by integrating Stripe, a payment gateway provider. 
- Payment processing is placed in the Checkout app.

#### Security

**Payment Security**

- **Stripe Integration:** Leveraging Stripe's secure payment infrastructure, the application safeguards sensitive financial information during transactions, ensuring user trust and compliance with industry security standards.

**Data security Measures** 

- **CSRF Protection:** To safeguard against Cross-Site Request Forgery (CSRF) attacks, the application enforces CSRF tokens in all forms using the POST method, enhancing data integrity and preventing unauthorized actions.

**User Management**

**Django Allauth Integration:** 
- User authentication and authorization are implemented through Django Allauth, a third-party library that ensures robust security for secure user access control.

**UserProfile model:** 
- The UserProfile model is used to store user data (user name, email, password). 
- The model is placed in the Profiles app. 
- To differentiate from similar data stored in the Order model, the fields in the UserProfile mode are prefixed with "default_". 
- Users can place orders without creating a user account.
- The "video_unlocked" boolean field indicates whether a registered user has purchased access to a video tutorial. 
  - The field is updated via the webhook handler in the Checkout app.

**Relationship with Order and Contact models:** 
- The UserProfile model links to the models:
  - Order (placed in the Checkout app)
  - Contact (placed in the Contact app)
- These relationships facilitate data retrieval and management of user contact information and purchase history.

![ERD UserProfile](/documentation/erd-userprofile.png)

**Communication**

**Contact model:** 
- Users can contect the store owner using a contact form. 
- The form data is stored in the Contact model placed in the Contact app.
- This form collects necessary details for the store owner to provide a tailored offer for a customized surfboard.
- The form can be used for general enquiries, feedback, or questions. 
- Users receive a copy of the message to the provided email address. 
- The store owner is notified of new messages by email and can reply by email and/or via the admin interface.

**Relationship with UserProfile and Category models:** 
- The Contact model links to the models: 
  - UserProfile model (placed in the Profiles app)
    - Allows for convenient prefilling of the user's contact information in the form.
  - Category model (placed in the Products app)
    - For a quick and easy overview of messages for the store owner.

![ERD Contact Model](/documentation/erd-contact.png)

![ERD Contact Model CONSTANTS and ForeignKey](/documentation/erd-contact-constants-fk.png)

<span id="anchor-newsletter"></span>
**Newsletter model:** 
- This custom model provides a way to 
  - Draft, finalize, and send newsletters to subscribers. 
  - Provide a status workflow for managing newsletter creation and delivery. 
  - Record the timestamp of dispatch.
  - Automatically update the status to “Done and Sent”
    - This can also be updated manually in case the newsletter was sent from the email account as opposed to via the admin interface. 
  - Keep records of newsletter content.

**Subscriber model:** 
- This custom model represents users subscribed to the newsletter. 
- Collects only email address and no unnecessary personal data (e.g. name or phone number) not strictly necessary to newsletter subscription. 
  - This adheres to  the EU General Data Protection Regulation’s (GDPR) principle of data minimization, promoting user privacy and encouraging subscriptions.
- Ensures that each subscriber can only sign up once through unique email addresses.

- Users must explicitly agree to receiving the newsletter.
  - The boolean field defaults to “False” for an unchecked checkbox to consent, in compliance with the EU GDPR.
- An **unsubscribe token** is generated for each subscriber for handling secure unsubscriptions. 
  - The token is created using Python’s secrets function, ensuring uniqueness and security. 
  - This is to avoid malicious unsubscribing of subscribers using loops. 
  - The token is not regenerated to avoid conflicts with expired tokens that negatively affect user experience. Regenerating unsubscribe tokens at certain time points does have security benefits and would be considered for a larger scale project. 
  - Activating the unsubscription token permanently deletes the subscriber’s email address from the database, aligning with GDPR data retention guidelines.
- A confirmation email is sent to the subscriber, containing:
  - Information about the ability to unsubscribe at any time, ensuring transparency and control over their subscription.
  - Personalized unsubscribe token.
  - Discount code as a small token of appreciation for subscribing. 
- The personalized unsubscribe token is sent to each subscriber in every newsletter. 

![erd-newsletter](/documentation/erd-newsletter.png)

**About Us**

**AboutUs model:** 
- The AboutUs model contains information about the store owner and the website's mission. 
- Placement is in the About app. 

**CustomSurfboard model:** 
- The custom model contains a collection of custom surfboards created by the store owner. 
- Placement is in the About app.
- While there is no direct entity relation between the models, the CustomSurfboard model enhances the Contact model, which collects data from customers for a customized surfboard.

**FAQ model:** 
- The custom model stores frequently asked questions and their answers. 
- Placement is in the About app.
- Including a FAQs page can enhance the credibility and authority of the website content, which search engines like Google value and thereby benefitting search engine optimization (SEO).

**Resource model:** 
- The custom model stores external weblinks to reliable sources on environmental and ocean conservation. 
- Placement is in the About app.
- Including external links to reputable sources can enhance the credibility and authority of the website content, which search engines like Google value and thereby benefitting search engine optimization (SEO).

![ERD About Us](/documentation/erd-about.png)

### Agile Development Methods

This project utilizes Agile Development Methods to manage development and ensure efficient delivery.

#### Epics 

- Epics represent the high-level objectives and functionalities of the project. - Each epic can be further decomposed into smaller, more manageable tasks described in the user stories. 
- The epics can be viewed on [this project’s Kanban board](https://github.com/users/g-omarsdottir/projects/5).

#### User Stories

- User stories are detailed descriptions outlining functionalities from the user's perspective. 
- They follow the format "As a [role], I can [capability] so that [received benefit]". 
- Each user story has well-defined acceptance criteria outlining the specific requirements for successful implementation. 
- The user stories can be viewed on [this project’s Kanban board](https://github.com/users/g-omarsdottir/projects/5).

#### The MoSCoW Prioritization Method

- To effectively manage resources and development flow, based on urgency and necessity, the prioritization method MoSCoW was employed. 
- The acronym MoSCoW stands for **M**ust Have, **S**hould Have, **C**ould Have, and **W**on't Have. *(The o's were added for easier pronounciation.)*

  - **Must Have:** Features absolutely essential for the current iteration's functionality and guaranteed to be delivered.
  - **Should Have:** Desirable features that add significant value to the current iteration if time allows.<br>
  - **Could Have:** Features that would be nice to have but can be deferred for later iterations without impacting core functionality.<br>
  - **Won't Have:** Features that are not a priority for the current iteration and are excluded from the current scope or unlikely to be implemented.<br>
- The priorities are reflected with **labels** on each user story on [this project’s Kanban board](https://github.com/users/g-omarsdottir/projects/5).

#### Kanban Board for Visual Workflow Management

- The Kanban board is a handy tool in agile project management to provide a clear visual representation of the project planning and development workflow. 
- It displays the various stages each work item progresses through and the current status of each individual tasks.
- This project’s Kanban board can be viewed [here](https://github.com/users/g-omarsdottir/projects/5).

## Features

### Main Features

### Custom Error Pages

- The custom HTML error pages 
  - For status codes
    - 403 (Forbidden)
    - 404 (Not Found)
    - 500 (Internal Server Error) 
    - Maintain a consistent design with the rest of the website for improved user experience. 
  - Clearly explain the meaning of the error code in a user-friendly clear, concise language, and avoid technical jargon. 
  - Display a friendly image in line with the website theme to make the error page more visually appealing.
  - The user is invited to return to Homepage by clicking a button.

To style the error pages during development, the error pages were rendered using temporary views and urls placed in the profile app for easy testing. The approach is documented in [TESTING.md](TESTING.md).

![custom error pages](/documentation/feature-error-pages.png)

### Discount Code

The siscount code system is a feature implemented to enhance user experience and support marketing efforts:
- Users can obtain discount codes by subscribing to the newsletter or through promotional campaigns.
- The active discount code and its amount are clearly displayed in the shopping cart.
- Users have the flexibility to remove or replace discount codes as needed.
- When a new discount code is entered, it automatically replaces any existing code, ensuring only one discount is applied at a time.
- For transparency and record-keeping, the applied discount code is stored with the order details (stored in the Order model, placed in the Checkout app), benefitting both customers and store management.

![discount code](/documentation/feature-discount-code.png)

![discount code order details](/documentation/feature-discount-order-history.png)

### Tutorials

The tutorials section offers a user-friendly browsing and purchasing experience:
- Tutorials are displayed as grid of image cards, each containing an image, title, and brief description.
- Users can purchase tutorials using the integrated Stripe payment system and receive immediate access to it.
- A convenient "Back to Top" button is available on the side of the page for easy navigation.

![feature tutorials](/documentation/feature-tutorials.png)

- Clicking an image card reveals a detailed view of the selected tutorial.
- In the detailed view, users can:
  - View more comprehensive information about the tutorial.
  - Add the tutorial to their shopping cart. 
  - Return to the overview using a clearly labeled button.

![feature tutorials detail](/documentation/feature-tutorials-detail.png)

### About Us

The "About Us" section serves critical purposes in building customer trust and engagement:
- Provides transparency by introducing the store owner and business background.
- Humanizes the brand by sharing personal story and motivation.
- Establishes credibility and authenticity for potential customers.
- Creates an emotional connection with visitors.
- Strategically includes calls-to-action like newsletter signup and internal page links.
- Helps potential customers understand the brand's values and mission.

![feature about us](/documentation/feature-about-us.png)

![feature about us links](/documentation/feature-about-us-links.png)

![feature about us links 2](/documentation/feature-about-us-links-2.png)

### Collection of Surfboards

This section showcases the store owner's craftsmanship through a curated collection of previously created custom surfboards:
- Displayed as a grid of image cards, each representing a unique surfboard.
- Located within the "About Us" section to differentiate from purchasable products.
- A convenient "Back to Top" button is available on the side of the page for easy navigation.
- Clicking an image card reveals a detailed view of the selected surfboard.
- In the detailed view, users can:
  - Examine a larger image and specifications of the custom surfboard.
  - Send an enquiry via a link to the contact page.
  - Return to the gallery overview using a clearly labelled button.

![feature surfboards](/documentation/feature-surfboards.png)

![feature surfboard detail](/documentation/feature-surfboard-detail.png)

### Frequently asked questions (FAQ)

- The user can view frequently asked questions. 
- Including a FAQ page is a common practice to improve SEO.

![feature faq](/documentation/feature-faq.png)

### Newsletter

- Key Technical Features:
  - Developed a robust newsletter subscription system demonstrating full-stack development skills.
  - **Newsletters can be drafted, finalized, and sent** with status tracking directly from the admin interface using gmail API.
  - Implemented comprehensive frontend (client-side) and backend (server-side) form validation.
  - Backend email validation with database uniqueness check
  - Dynamic modal content loading without page refresh for optimal version control of privacy policy and terms.
- Security and Data Protection:
    - CSRF protection on subscription form.
    - Secure unsubscription mechanisms using unique tokens against malicious unsubscribing.
    - GDPR-compliant data collection (minimal personal data, permanent deletion at unsubscription, active consent to terms).
- User Experience (UX):
  - Autofocused input field for seamless user interaction.
  - Real-time form validation with clear error messaging.
  - Automated email confirmation including:
    - One-click unsubscribe functionality using a personalized unsubscription token. 
      - Personalized unsubscription token is resent to each subscriber with each newsletter.
    - Welcoming discount code.
      - Error handling is in place in case of invalid discount code.
  - Please see a detailed description of data privacy in accordance with the GDPR, security measures for subscribing and unsubscribing, as well as the procedure and options to send the [newsletter in the communication section of the data base schema section](#anchor-newsletter).

  ![feature-newsletter-validation](/documentation/feature-newsletter-validation.png)

  ![feature-newsletter-modals](/documentation/feature-newsletter-modals.png)

  ![feature-newsletter-success page](/documentation/feature-newsletter-success.png)

- **Error handling** for discount code retrieval: 


  ![feature-newsletter-discount-error](/documentation/feature-newsletter-discount-error.png)

- **Secure unsubscription process:**

  ![feature-newletter-unsubscribe](/documentation/feature-newsletter-unsubscribe.png)


#### Promoting the Newsletter on the website: 

- The newsletter subscription page is prominently linked and can be accessed at any time with one click, without invasively blocking the users screen at any point for imporoved UX. 

- **As a link in the footer**:

  ![feature-newsletter-footer](/documentation/feature-newsletter-footer.png)

- **As a banner** on the tutorials page: 

  - **Subtle animation:** slow slide down with a gradient glow that fades.

    ![feature-newsletter-banner](/documentation/feature-newsletter-banner.png)

  - **Conditional display:** 
    - If a registered user has already subscribed to the newsletter, the banner is not displayed to avoid visual clutter (see code placed in views in the Products app). 
    - Banner text: Subheading only displayed on medium screens and up.

    ![feature-newsletter-subheading](/documentation/feature-newsletter-subheading.png)

  - **Accessibility:** 
    - The whole surface of the banner is clickable to navigate to the newsletter subscription page for improved UX, especially people with motor disabilities.

- As an item on the **navigation bar** under the section about us:

  ![feature-newsletter-navbar](/documentation/feature-newsletter-navbar.png)

- As a **link** in the website's content where fitting:

  ![feature-newsletter-prom](/documentation/feature-newsletter-prom.png)

### Resources

- Including external links to reputable sources can enhance the credibility and authority of the website content, which search engines like Google value and thereby benefitting search engine optimization (SEO).
- Grid-based layout displaying resources as clickable cards for improved accessibility and UX, especially for people with motor disabilities.
- The links open in a new window.

![feature resources](/documentation/feature-resources.png)

### Shopping Cart

- Key Functionality Features:
  -	Add tutorials to cart with instant user notification.
  -	Remove items from cart.
  -	Apply discount codes.
  -	Proceed to secure checkout.
  -	Return to tutorial overview.
- Key Technical Features:
  - Dynamic cart updates without page reload.
  -	Integrated discount code system.
  -	Secure checkout process.
- Error Prevention:
  -	Limit of one unit per tutorial in cart.
  - Safeguards against accidental duplicate purchases.
  -	Reduced risk of invoice errors.
- User Experience (UX):
  -	Temporary success messages to minimize screen clutter.
  -	Persistent cart preview for easy checkout access.
  -	Prevention of duplicate tutorial purchases to avoid errors.
  - Order confirmation by email and in "My Account" for registered users.

- Optimal screen real estate through temporary user feedback:
  ![feature userfeedback cart](/documentation/feature-userfeedback-cart.png)

- **Shopping Cart:**
  ![feature cart](/documentation/feature-cart.png)

- **Error Handling:**
  ![feature cart](/documentation/feature-cart-double.png)

### Contact Form

- Key Functionality Features:
  -	Comprehensive contact form for custom surfboard enquiries.
  -	Showcases expertise and attention to detail.
  -	Educates users on surfboard customization process.
  -	Streamlines communication between customers and administrators (store owner) for the complicated calculating a surfboard’s parameters based on the surfer and its intended use
- Key Technical Features:
  -	Implemented comprehensive frontend (client-side) and backend (server-side) form validation.
  - Comprehensive user feedback and instant display of sent message.
- User Experience (UX):
  -	Auto-fills form for logged-in users with profile data.
    -	Allows easy modification of pre-filled information.
  -	Non-registered users can use the contact form.
  - Balances required fields with optional detailed information.
  -	Users receive an instand display of their message and a copy sent to the provided email address.
- Security:
  -	Integrates with the Allauth user authentication system.
  -	Implements industry security standards (CSRF protection).

![feature contact prefill](/documentation/feature-contact-prefill.png)

![feature contact form](/documentation/feature-contact-form.png)

### User Profile

**CRUD functionality: Create** <br>
- Users can **create** an account by signing up. 
- For convenience, the user can save the personal information to their profile, which they entered during the checkout process when purchasing a tutorial.

  ![Feature userprofile save info](/documentation/feature-userprofile-save.png)

**CRUD functionality: Read** <br>
- The user can view their order history.
- Users can click on the order number link to view the original full order confirmation.

  ![feature profile orderhistory](/documentation/feature-profile-orderhistory.png)

**CRUD functionality: Update** <br>
- Users can manage their profile information by clicking the button "Manage My Profile". 
- Here they can **update personal information**. 
- Security:
  	- Django Allauth's password and authentication settings are configured to safeguard against brute force attacks.
  - If the email address associated with the user account is updated, the system implements a security measure:
    - Notification emails are sent to both the previous and new email addresses.
    - This serves as a precautionary step to alert the user in case of a an unintended or malicious change of email addresses.
    - Users are advised to contact the store owner if they didn't initiate this change themselves.

  ![feature profile manage](/documentation/feature-profile-manage.png)

**CRUD functionality: Delete** <br>
- Users can **delete the user profile** permanently from the database. 
- Deletion must confirmed before proceeding to avoid unintended deletion.
- Of course, users can **cancel** and return to their user profile without taking any action.

  ![feature profile delete](/documentation/feature-profile-delete.png)

- The user can access the links to the **purchased tutorials in the userprofile**.

  ![feature user profile](/documentation/feature-profile.png)

### Order confirmation

- An order confirmation with all details and a link to the purchased tutorial is displayed immediately after successful purchase.
- The order confirmation is sent to the provided email address as well.

  ![feature order confirmation](/documentation/feature-order-confirmation.png)

### Purchased Tutorial

- The tutorials are a similation for the purpose of this ecommerce project.
- The link in the order confirmation links to the tutorial hosted on youtube (not listed for public view).
- In this simulation, the title of each tutorial is displayed in the beginning and fades out while the video plays.

  ![feature watch purchased tutorial introduction](/documentation/feature-vid-building.png)

  ![feature watch purchased tutorial shortboard](/documentation/feature-vid-shortboard.png)

  ![feature watch purchased tutorial boyancy](/documentation/feature-vid-boyancy.png)

### Search Bar

- Users can enter a search query for the tutorials into the search field in the header, with the placeholder "search tutorials". 
- The search results display a list of tutorials containing the search query in the titel or description.
- If the search query does not match any of the tutorial titels or description, the user is notified and redirected to the the tutorials overview page.

  ![feature search](/documentation/feature-search.png)

### Responsiveness

- Full responsiveness was achieved using Bootstrap's grid system. 
- The website is designed to be viewed on a desktop, laptop, tablet or mobile device.

### Security

This application prioritizes security at every level, from user account management to data protection and financial transactions simulation.

#### User Authentication and Authorization

- The application ensures secure user authentication and authorization through the integration of Django Allauth. 
- This powerful tool simplifies the process of managing user accounts, including registration, login, password reset, and email verification. 
- By utilizing Django Allauth, the project adheres to best practices for web application security, providing our users with a safe and reliable environment.

#### Access Control

- To safeguard user data and privacy, stringent access controls were implemented. 
- These measures are designed to restrict unauthorized access to sensitive information, ensuring that each user can only view or interact with their own content. 

#### Secure Payment Processing

- For handling financial transactions, the project utilizes Stripe, a leading payment processing service. 
- Stripe is renowned for its commitment to security, providing a seamless and secure way for users to make payments online. 
- By integrating Stripe, all financial operations are ensured to be conducted in compliance with industry-standard security protocols, protecting both users and the store owner from potential threats.

### Future Features

- **Review and Rate Management:** 
  - User-driven review and rating system for products. 
  - Empowers administrators (store owners) with insights into customer preferences, identifying popular and less favored tutorials to facilitate strategic decisions regarding content expansion or refinement.
  - Guides users towards making informed purchasing choices.

- **Light Mode and Dark Mode**

## Web Marketing

### Ecommerce Business Model

The business model for this ecommerce website is a Business to Customer (B2C) model, selling digital content for single one-time payments.

This section elaborates on the ecommerce marketing value and SEO benefits of the project’s custom models.

The focus and main goal of this project is to create an ecommerce website with integrated purchase process and features that increase the marketing value and SEO benefits. The design of the technical architecture of the individual Django models was created to enhance web marketing efforts beyond the organic growth with social media marketing and reducing costs related to traditional advertising.

#### Products Models

- The Product model and related Category and Subcategory models ensure a coherent and consistent use of terminology regarding the surfboard parameters throughout the website. 

- **Marketing Value:** 
  - Consistent use of terminology makes a trustworthy and serious impression. - Avoids misspelling in the product description, thus avoiding concerns about the store owner’s expertise, potentially leading to reduction of the market value.

- **SEO Benefits:** 
  - Using predefined parameters reduces the risk of misspelling while creating the entry for the product, potentially leading to failed searches in search engines or on the website’s integrated search field.

#### Discount Code Model

- **Marketing Value:** 
  - Discount codes incentivize users to subscribe to the newsletter, increasing brand awareness and potentially leading to repeat customers.

**SEO Benefits:** 
  - Discount codes can be promoted through social media and email marketing campaigns, driving traffic to the website.

#### Video Unlocked Field of the Profile model

- **Marketing Value:** 
  - The video_unlocked field unlocks the access to a tutorial in the user's profile page, which is triggered during the purchase process of the tutorial (by the webhook handler at successful payment). 
  - This feature invites users a conveniently keep an overview of and access to their purchased tutorials on their profile page on the website. 
  - Repeated visits to the website and the thoughtful placement of buttons to browse through the collection of tutorials increases the likelihood to purchase further videos.

#### Contact Form Model

- **Marketing Value:** 
  - The contact form facilitates communication with potential customers, allowing them to inquire about custom products or ask questions. 
  - Even if users did not visit the website to place an order for a custom-made surfboard by the store owner, they are likely to take interest in the  various details necessary to shape a custom-made surfboard and enticed to make an enquiry, possibly leading to a sale.
  - Connoisseurs will recognize the attention to detail and amateurs will appreciate the guidance through the complicated process of calculating a surfboard’s parameters with regard to the surfer and intended use, potentially enhancing the marketing value and increasing website traffic.

- **SEO Benefits:** 
  - A well-designed contact form can improve user experience, which is a positive SEO ranking factor.

#### About Us Model

- **Marketing Value:** 
  - The About Us page tells the brand story and builds trust with potential customers.

- **SEO Benefits:** 
  - High-quality content on the About Us page can improve website authority and ranking for relevant keywords. 
  - The date of entry increases the seriousness of the website.

#### Custom Surfboard Model

- **Marketing Value:** 
  - The Custom Surfboard page provides a collection of custom-made surfboards with elegant images for potential customers showcasing the store owner’s expertise. 
  - The detail view of a custom surfboard invites the user to visit the contact page to enquire about the surfboard, potentially leading to a sale of a custom surfboard or a tutorial for creative DIY users.

#### FAQ Model

- **Marketing Value:** 
  - The frequently asked questions page provides valuable information to potential customers addressing their concerns and demonstrates the commitment to customer service and expertise in the field of environmental-friendly materials and reducing the carbon footprint of the surfboard industry. 

- **SEO Benefits:** 
  - The FAQs target long-tail keywords related to custom surfboards, environmental conservation, and climate change mitigation, which improves SEO. 
  - Websites with a section for  frequently asked questions enhance the authority and seriousness of the website by search engines like google, thus improving organic search traffic.

#### Resources Model

- **Marketing Value:** 
  - The Resources page demonstrate the commitment to environmental and ocean conservation causes, potentially resonating with environmentally conscious customers. 

- **SEO Benefits:** 
  - Including external links to reputable and high-quality sources like the United Nations and the Intergovernmental Panel on Climate Change can enhance the credibility and authority of the website content, which search engines like Google value and thereby beneficial for SEO. 
  - The administrators (store owner) can manually change the order of the resources on the website according to current popularity of search terms or environmental occurrences.

#### Future Project Expansion
- The project is designed with a potential to expand to selling further products and physical goods. 
- The content displayed on the website can be updated according to current market trends and popular search terms.

### Marketing Strategies

### Social Media & Newsletter Marketing

- Marketing Objectives:
  - Newsletter signup with discount incentive.
  - Organic social media growth on Facebook.
  - Promote products and educational content.
- Content Strategy:
  - Showcase new tutorials and custom surfboards.
  - Share discount code campaigns.
  - Highlight sustainability and environmental topics.
- Key Focus Areas:
  - Ocean conservation.
  - Climate change awareness.
  - Surfboard industry environmental impact.
  - Life cycle analysis (LCA) and carbon footprint reduction.
- Business Goals:
  - Increase brand visibility.
  - Drive website traffic.
  - Educate and engage target audience.
  - Encourage product purchases through value-driven content.

- Facebook Page Simulation:
  ![facebook-mockup](/documentation/facebook-mockup.png)

### Search Engine Optimization (SEO)

- The website design was planned with SEO in mind. 
- This is described in detail in section [Web Marketing above](#web-marketing) and the relevant [ERDs for each Django model](#key-features).

#### Keywords

- The metadata for this project has been carefully crafted to enhance search engine optimization (SEO) and improve discoverability. 
- The overall approach to keyword selection and implementation is as follows:

##### Keyword Development Process

- **Initial Brainstorming with fellow surfers and my sister, Geographer and Specialist in Geothermal Energies**: 
    - Identification of relevant terms and concepts related to surfboard tutorials and eco-friendly surfing products to target the most effective terms for the niche.

- **Google Search Analysis**: 
    - Related searches and suggestions provided by Google for initial terms.

- **Professional Consultation**: 
    - Consultation with SEO professionals to refine the keyword list. 

- **Long-Tail Keyword Focus**: 
  - Emphasis is on long-tail keywords to target specific user intents and capture more qualified traffic. 
  - Longer, more specific phrases tend to have less competition and higher conversion rates.

- **Keyword Diversity**: 
    - A mix of both short-tail and long-tail keywords to create a balanced and comprehensive SEO strategy.

##### Keyword Implementation
- Keywords are strategically placed in meta descriptions, page titles, and content headers.
- A natural integration of keywords within the website content to maintain readability and user experience. Keywords were used in headings and in semantic and html `<strong>` tags.
- The metadata is structured to be both search engine friendly and informative to potential visitors.

#### Sitemap

- [XML-Sitemaps.com](https://www.xml-sitemaps.com/) was used to generate the sitemap for the deployed project. 
- The generator crawls the entire website and generates a sitemap.xml file that was downloaded and placed in the rootdirectory of this project. 
- The sitemap is an XML file that contains a list of all the pages on the website. 
- The sitemap is used by search engines to crawl the website and index the pages.

#### Robots.txt

- The robots.txt file is a text file that tells search engines how to crawl the website. 
- The robots.txt file is located in the root directory of the website. 
- The robots.txt file is used to disallow certain pages from crawling by search engines and are not indexed by search engines.
- The [Sitemap for this project](https://www.xml-sitemaps.com/details-shaping-sustainable-surf-8794b08a1b3a.herokuapp.com-da3dd3a88.html) is included in the robots.txt file.

- Disallowed pages are the **user account** and **shopping cart** pages.

- The ownership of the robots.txt file is tested and verified by Google by adding a sitespecific metatag in the head of the base template. 
- Google then veryfies if the robots.txt file is working correctly and provides a performance report after a short waiting time.

  ![ownership-verfied-html-tag](/documentation/testing/test-robots.txt.png)

### Privacy Policy

- Generated using [Privacypolicygenerator](https://www.privacypolicygenerator.info/).
- Outlines data collection, processing, storage, and protection methods, ensuring legal compliance and user trust.
- Rendered on the websites template for visual appeal and trustworthyness. 
- Placement is in the Home app.
- Link is anchored in the footer of the website.
- Key Aspects:
  - GDPR Compliance: Mandatory for collecting EU residents' data.
  - Trust Building: Transparency about data collection and usage.
  - Risk Management: Proactive approach to prevent legal and reputational issues.

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
- [django-resized v1.0.2](https://pypi.org/project/django-resized/) - Handles resizing and format converting of images uploaded by administrators
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
- [Neon.tech](https://neon.tech/) for the database
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

This project utilizes a relational database powered by [Neon.tech](https://neon.tech/), a serverless PostgreSQL solution.

To connect to the database:
- Log into or sign up for a Neon account.
- Create or navigate to your "Tier" (one free tier per user).
- Navigate to the "Dashboard" on the left side menu.
- In the section "Connection Details", you will find the link to the database displayed in the subsection "Connection String".
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
- My sister, Malfridur Omarsdottir, Geographer and Specialist in Geothermal Energies, for brainstorming for keywords, proofreading content and fact checking on eco-friendly sustainable materials and links to reliable resources.
- My friend Stephan Reich, Software Developer, for his support and advice.
- My fellow student at Code Institute [Amir Schkolnik](https://github.com/AmirShkolnik) for his valuable support with proofreading.
- My Code Institute class facilitator, Kristyna Wach, for her cheerful motivation and encouragement.
- Slack community for support and advice.
- Stackoverflow community for information.