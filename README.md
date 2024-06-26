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

**Testing and Bugs** are documented in the separate file TESTING.md

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

## Project planning

### Database Schema

This project leverages a serverless PostgreSQL database for efficient data management. A well-defined Entity Relationship Diagram (ERD) (see below) was created upfront to guide development. This approach minimizes database complexity and streamlines the development process, reducing the need for future modifications and debugging. Each model within the project directly corresponds to a table in the ERD, ensuring a clear and consistent data structure.

#### Technical Architecture

**Technical Design:** Separation of concern was implemented by dividing key components into individual Django Models (see ERD). This allows for simple and reliable queries based on the primary key, as well as easy management and scalability.

Relationships between the model fields are indicated with relationship lines on the ERD.

**Model-Based Design:** The principles of separation of concerns are adhered to by employing distinct Django models for each key system component (see ERD). This promotes code clarity, maintainability, and scalability.

**Relational Data Modeling:** The ERD effectively visualizes the relationships between models and model fields, fostering the construction of streamlined and efficient database queries utilizing primary keys.

#### Key Features

**Product Management:** The custom models facilitate the storage and management of individual product entities.

Products are stored in one model. Categories and Subcategories are stored in separate models, which allows for scalability and streamlines further technical design. 

Choices for the Category and Subcategory models are defined as constants within the models. This guarantees consistent terminology throughout the application, enhancing user experience and simplifying search queries.

This approach simplifies the models for the shopping and purchase process, as well as allows for code consistency in code, by referring to products in all html template by the name product, while assuring a separation of concerns and explicitness.

Store owners and superusers are granted comprehensive permissions to create, update, and delete product data. This enables efficient content management within the application.

![ERD Product model](/documentation/erd-product.png)

**Ecommerce Functionality**

**Integrated Payment Processing:** The system facilitates secure online transactions for product purchases by integrating with Stripe, a payment gateway provider. This ensures a seamless and secure user experience during checkout.

**Purchase Models:** Additional Django models are implemented to manage the intricacies of online purchases. These models capture essential order and payment details, enabling efficient transaction processing and record-keeping.

**Relationship with Product and User models:** The purchase models establish relationships with both product and user models (see ERD). This facilitates data retrieval and management of purchase history for both users and store administrators.

**Payment Security**

**Stripe Integration:** By leveraging Stripe's secure payment infrastructure, the application safeguards sensitive financial information during transactions. This ensures user trust and adheres to industry-standard security protocols.

**Data security Measures** 

**CSRF Protection:** To safeguard against Cross-Site Request Forgery (CSRF) attacks, the application enforces the use of CSRF tokens in all forms using the POST method. This bolsters data integrity and prevents unauthorized actions.

**Django Allauth Integration for User Management:** ser authentication and authorization are implemented by leveraging the Django Allauth, a third-party library that upholds robust security practices. This provides a robust and secure foundation for user access control.

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

[Django v3.2.25](https://docs.djangoproject.com/en/5.0/releases/3.2.25/) - Python web framework
[django-allauth v0.63.3](https://docs.allauth.org/en/latest/installation/index.html) - User account authentication
[black v24.4.2](https://black.readthedocs.io/en/stable/) - Formats code compliant to pep8
[django-extensions v3.2.3](https://pypi.org/project/django-extensions/) - Show urls and location of installed packages
[django-crispy-forms v2.2](https://django-crispy-forms.readthedocs.io/en/1.14.0/) - Simplifies the creation of forms
[crispy-bootstrap v4](https://pypi.org/project/crispy-bootstrap4/) - Bootstrap-specific classes to style forms
[django-resized v1.0.2](https://pypi.org/project/django-resized/) - Handles resizing and format converting of images uploaded by store owners
[pillow v10.3.0](https://pillow.readthedocs.io/en/stable/) - A Python imaging library, handles images in combination with the Django Resized Image Field
[django-richtextfield v1.6.2](https://djangopackages.org/packages/p/django-richtextfield/) - A customizable rich text editor for product description
[cloudinary v1.40.0](https://cloudinary.com/documentation/django_integration) - Allows to upload product images
[django-cloudinary-storage v0.3.0](https://cloudinary.com/documentation/rails_activestorage) - Provides storage of uploaded product images 
[django-countries v7.6.1](https://pypi.org/project/django-countries/) -  Provides country choices for use with forms and a country field for models.

### Programs Used
[Canva](https://www.canva.com/) to create the website logo
[Photoroom](https://www.photoroom.com/tools/background-remover) to remove background from images and website logo
[Pixelied](https://pixelied.com/convert) to convert images to webp format
[TinyPNG](https://tinypng.com/) to compress images
[favicon.io](https://favicon.io/favicon-converter/) to create favicon from website logo

## Features
### Main Features
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

*to-do*

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

[Django Docs](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/#inlinemodeladmin-objects) for the Django admin site

### Imagery

[Canva](https://www.canva.com/) - Website logo and favicon

### Acknowledgements
