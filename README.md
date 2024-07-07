# ![logo](/documentation/logo_wave.png) Shaping Sustainable Surf

Mockup
You can view the live project here # <br>
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
- [Project planning](#project-planning)
  - [Database Schema](#database-schema)
  - [Agile Development Methods (Epics, User Stories, MoSCoW Prioritization, Kanban board)](#agile-development-methods)
-	[Technology Used](#technology-used)
    -	[Languages Used](#languages-used)
    -	[Libraries and Frameworks Used](#libraries-and-frameworks-used)
    -	[Programs Used](#programs-used)
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
- [Deployment and Local Development](#deployment-and-local-development)
  - [Local Clone](#local-clone)
  - [Fork](#fork)
  - [Database](#neon-database)
  -	[Cloudinary](#cloudinary)
  -	[Stripe](#stripe)
  - [Google Mail (Gmail) API](#gmail)
  - [Deployment](#deployement-using-heroku)
- [Credits](#credits)

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

### Wireframes

Wireframes were designed mobile-first, since the majority of ecommerce purchases are done with mobile devices or tablets.

Screen sizes smaller than 320 were not considered in the design.

#### Wireframes Mobile Version

![mobile wireframes browsing website](/documentation/mobile-browse.png)

![mobile wireframes actions](/documentation/mobile-actions.png)

#### Wireframes Desktop Version

![desktop wireframes home](/documentation/desktop-home.png)
![desktop wireframes tutorials](/documentation/desktop-tutorials.png)
![desktop wireframes communication](/documentation/desktop-communication.png)
![desktop wireframes user account](/documentation/desktop-user-account.png)
![desktop wireframes purchase](/documentation/desktop-purchase.png)


### Colors

The website's colors are inspired by the ocean and the beach. The main color of the website is the blue #57a7b3 used in the website logo.

![colors](/documentation/colors.png)

A complimenting colorpalette with the website logo's color was created by [Muzli Colors](https://colors.muz.li/palette/57a7b3/3d757d/b35794/7d3d67/b3a357). To keep the overall layout sleek and avoiding visual clutter, the complementing colors were mainly used as accents in box-shadows and for pseudo-class hover effect.

The font color is a warm tone of black and background color is a lighter shade of the main color, which make a very good match for accessability, readability and contrast while being easy on the eye.

[Coolors Color Contrast Checker](https://coolors.co/contrast-checker/333333-eef6f7) score:

![contrast checker](/documentation/color-contrast.png)

## Project planning

### Database Schema

This project leverages a serverless PostgreSQL database for efficient data management. A well-defined Entity Relationship Diagram (ERD) (see below) was created upfront to guide development. This approach minimizes database complexity and streamlines the development process, reducing the need for future modifications and debugging. Each model within the project directly corresponds to a table in the ERD, ensuring a clear and consistent data structure.

#### Technical Architecture

**Technical Design:** Separation of concern was implemented by dividing key components into individual Django Models (see ERD). This allows for simple and reliable queries based on the primary key, as well as easy management and scalability.

Relationships between the model fields are indicated with relationship lines on the ERD.

**Model-Based Design:** The principles of separation of concerns are adhered to by employing distinct Django models for each key system component (see ERD). This promotes code clarity, maintainability, and scalability.

**Relational Data Modeling:** The ERD effectively visualizes the relationships between models and model fields, fostering the construction of streamlined and efficient database queries utilizing primary keys.

#### Key Features

**Product Management:** The custom models facilitate the storage and management of individual product entities in the products app.

Products are stored in one model. Categories and Subcategories are stored in separate models, which allows for scalability and streamlines further technical design. 

Choices for the Category and Subcategory models are defined as constants within the models. This guarantees consistent terminology throughout the application, enhancing user experience and simplifying search queries.

This approach simplifies the models for the shopping and purchase process, as well as allows for code consistency in code, by referring to products in all html template by the name product, while assuring a separation of concerns and explicitness.

Superusers (store owners) are granted comprehensive permissions within the application, allowing them to efficiently manage content across the platform. These permissions encompass creation, update, and deletion of product data, and pricing adjustments.

![ERD Product model](/documentation/erd-product.png)

**Ecommerce Functionality**

**Discount Codes:** The custom model facilitates the storage and management of individual discount codes in the cart app. The model is used to validate the code and apply the discount to the shopping cart. To ensure the code is valid, the model checks if the code is in the database, and if the code is in the database, if the code is currently active. As precaution, the model and the form are placed in the shopping cart app to allow the form to be submitted to check for validation without interfering with the order form in the checkout app.<br>

Superusers (store owners) are granted permission to create, update, and delete discount codes, as well as manage settings to activate or disable discount codes temporarily.

**Relationship with Order model:** The Order model includes a foreign key to the DiscountCode model, allowing for easy access to the discount code applied to the order.<br>

![ERD DiscountCode model](/documentation/erd-discount-code.png)

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

## Technology Used
### Languages Used

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

### Programs Used
[Canva](https://www.canva.com/) to create the website logo
[Photoroom](https://www.photoroom.com/tools/background-remover) to remove background from images and website logo
[Pixelied](https://pixelied.com/convert) to convert images to webp format
[TinyPNG](https://tinypng.com/) to compress images
[favicon.io](https://favicon.io/favicon-converter/) to create favicon from website logo
[Fontawesome](https://fontawesome.com/) for icons
[Muzli Colors](https://colors.muz.li/palette/57a7b3/3d757d/b35794/7d3d67/b3a357) for color palette

## Features
### Main Features

#### Custom Error Pages

The project a custom HTML error page for status codes 403 (Forbidden) and 404 (Not Found) for improved user experience. The error page maintains a consistent design with the rest of the website. The error pages clearly explains the meaning of the error code in a user-friendly way avoiding technical jargon and uses clear, concise language. The error pages display a friendly image in line with the website theme to make the error page more visually appealing.<br>

To style the error pages during development, the error pages were rendered using temporary views and urls placed in the profile app for easy testing. The approach is documented in [TESTING.md](TESTING.md).

### Responsiveness
### Security
### Future Features

## Web Marketing

### Ecommerce Business Model

The business model for this ecommerce website is a Business to Customer (B2C) model, currently only selling digital content for single one-time payments. <br>

The project has the potential to expand to selling further products and physical goods, as the product category and subcategory models can be expanded by the store owner in the admin panel.

### Marketing Strategies
### Social Media & Newsletter Marketing
### Search Engine Optimization (SEO)
#### Keywords
#### Sitemap
#### Robots.txt
### Privacy Policy

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

The Code Institute walkthrough project Boutique Ado for inspiration for the basic website structure.
[Django Docs](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#inlinemodeladmin-objects) for the Django admin site.
[Django Docs](https://docs.djangoproject.com/en/dev/topics/email/#sending-alternative-content-types) and [StackOverflow](https://stackoverflow.com/questions/2809547/creating-email-templates-with-django) for sending emails as HTML formatted and plain text.
[Core JavaScript functunalities from stripe](https://stripe.com/docs/payments/accept-a-payment) for stripe payment process.
[Core CSS style from stripe](https://stripe.com/docs/stripe-js) for stripe payment process.

### Imagery

[Canva](https://www.canva.com/) - Website logo and favicon

### Acknowledgements
