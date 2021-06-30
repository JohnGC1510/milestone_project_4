# Testing

## Table of Contents
---
* [Navigation](#navigation)
* [Home Page](#index)
* [User pages](#user-pages)
    + [Profile Page](#profile-pages)
    + [Classes Page](#classes-page)
    + [Membership Page](#membership-page)
    + [Error Pages](#error-pages)
* [Store pages](#store-pages)
    + [All Products](#all-products)
    + [Product Details](#product-details)
    + [Shopping Bag](#shopping-bag)
    + [Checkout](#checkout)
    + [Checkout Success](#checkout-success)
    
* [Validators](#code-validation)
    + [HTML](#html)
    + [CSS](#css)
    + [JavaScript](#javascript)
* [PEP8](#pep8)
* [Compatibility](#compatibility)
    + [Hardware](#hardware)
    + [Browsers](#browsers)
* [User Stories](#user-stories)
    + [Guest User](#guest-user)
    + [Registered User](#registered-user)
    + [Subscribed User](#subscribed-user)
    + [Superuser](#superuser)
* [Known Bugs](#known-bugs)

Testing was performed manually for the full site.
### **Navigation**
---
- All links have been tested for all user types in both the collpased navbar, desktop navbar and the shop navbar and no broken links were discovered.
- If guests users attempt to access pages they do not have access to or perform operations they do not have permissions for they are re-directed to the log in page.
- The navigation item under the user icon change appropriately depending if the user is a guest user or is an authenticated user.
- If an authenticated user attempts to do an admin only task they are informed they do not have the neccesarry permissions and directed to the homepage
### **Index**
---
- The page displays as intended and scales appropriately with screen size. All call to action buttons perform the correct actions.
- The random products have a slight delay when automatically sliding that I was unable to fix
### **User Pages**
---
#### Profile Page
- If the user does not have any favourite items saved an appropiate prompt appears else the favourite items display correctly and react correctly to database changes.
- If the user signs up or removes themself from a class page the table in the profile page updates correspondingly.
- When the user submits the delivery information form with valid inputs the values update and display as intended.
#### Classes Page
- A number of issues were had on the classes page in getting the classes to display in the table appropriately, intially I wanted to leave gaps in the classes timetable to better represent what might be seen in a gym. However my resulting condional logic used a for loop over classes and with multiple classes present this lent to an issue in additonal empty `<td>` elements being created and classes appearing in the wrong place on the table. I was unable to resolve this issue so created enough data items to completely fill the table as a temporary solution. 
- I initially struggled to get the classes to update approiately when clicked as I had every element in the table as a submit button in form and handled the request in a POST request which lead to additonal complications.This was resolved by adding an js AJAX request to take the class_pk and return this to the classes view. 
- When a class is clicked an appropriate message is shown and the table cell clicked will change color to represent the users presence in the class.
- The class table is responsive and will scroll on smaller screens however this is an unideal solution to display the classes timetable, a different UI needs to be developed for smaller screen sizes.
#### Membership Page
- The membership page correctly displays different information for a unauthenticated user, bronze member, silver member and gold member. This prevents users from purchasing a duplicate membership which would not benefit them and allows the user to only see the information they would require. 
- The membership page is responsive on all screen sizes.
#### Error Pages

### **Store Pages**
---
#### All Products
- All the filtering has been tested and returns the correct products.
- Displays well on all screen sizes
- All links in the products navbar are unbroken
#### Product Details
- Quantity of an object is correctly updated when the increment/decrement buttons are pressed.
- When the favourite button the icon changes appropriately and the database is updated correctly
- When initally adding the favourite button had issues with duplicaitng users when trying to add favoruites. Intial logic was to loop through favourites and compare to request.user to check existance of user however the else statement caused multiple issues. Fixed using try except and later refined to object.get_or_create() to refactor the code.
#### Shopping Bag
- All items added from product details correctly display in the shopping bag
- Products with the same id but different sizes display corretly in the shopping bag
- All totals are calculated correctly and if the user has a gold membership then the member discount is correctly applied.
- Responds well on all screen sizes
#### Checkout
- If authenticated user has previosuly saved checkout details the checkout form fields autofill with the correct values
- If the user is not authenticated a prompt is displayed at the bottom of the form to encourage users to sign up rather than the save info box
- When the save-info box is checked the users details are correclty saved
- All totals and discounts are calculated correctly
- Adjust bag button returns you to bag and complete order button submits the payment.
#### Checkout Success
- On completion of order the expected response is seen and a confirmation email is sent to the customer
## **Code Validation**
---
### HTML
- All pages would fail HTML validation using the [HTML W3 validator](https://validator.w3.org/nu/#textarea) due to errors caused by Jinja Templating langauge. No errors or warnings occur other than those caused by use of Jinja Templating were found on any of the template pages.

### CSS

- No errors were found when the style.css page was passed for the [W3 CSS validator](https://jigsaw.w3.org/css-validator/validator)

### JavaScript
- I tested my javascript using [JS hint](https://jshint.com/)
### PEP8
- In webhook_handler there is a flake8 error cause by the long line `profile.default_street_address1 = shipping_details.address.line1` that I was unable to split over multiple lines
- In webhooks.py there is a flake8 error from a long line caused by `payment_intent.payment_failed': handler.handle_payment_intent_payment_failed` that I was unable to split over multiple lines
- In the store app in widgets.py there is a flake8 error from `template_name = 'store/custom_widget_templates/custom_clearable_file_input.html'` that I was unable to split over multiple lines
- The remainder of the python code that is not part of the django boilerplate is fully PEP8 compliant and passed the [PEP8 online](http://pep8online.com/) validation.

## Compatibility
---
### Hardware
I personally tested the website on:
- a windows system with a 4k and HD displays.
- A chromebook with a 1366x768 display
- A google pixel 5, google pixel 2, iphone 11 mobile devices
- An Ipad Pro

My family also tested on a number of different mobile devices and laptops. 

No issues were found on any devices during testing. 

### Browsers
I personally tested the website on:
- Google chrome
- Microsoft Edge
- Firefox

No browser specific issues were found during testing.
## User Stories
---
### Guest User
As a guest user I want...
-	to immediately understand the sites purpose
    - Acheived - upon entry to the site it is clear it is a gym site
-	site navigation to be intuitive.
    - Acheived - font awesome icons and appropriate navigation buttons/bars allow for easy navigation around the site
-	to be able to see the available products
    - Acheived - store shows all products
-	to be able to search the site for specific products
    - Acheived - A search bar functions for all products
-	to be able to view individual product details
    - Acheived - Clicking on a product in the store provides addiotnal details
-	to be able to easily view the shopping bag
    - Acheived - the cart icon clearly indicates the cart link and a preview of the bag is given in a toast
-	to be able to easily to adjust product quantities in the shopping bag
    - Acheived - increment and decrement buttons allow for this
-	to be able to easily remove products form the shopping bag
    - Acheived - text under the product quanity allows you to easily remove a product in your bag or update it's quantity
-	to be given feedback when a bag adjustment is made
    - Acheived - toasts display whenever a bag  adjustment is made
-	to receive order confirmation
    - Acheived - an email is sent to provide order conformation as well as the checkout-success view
-	to be able to easily create an account
    - Partially Acheived - minimal information required from the user to create an account but one click sign up is not enabled as I did not think it applicable to a gym website
-	to understand the benefits of being a registered user
    - Acheived - the membership page clearly explains the benefits of signing up to the site
-	the benefits of subscribing to the gym to be clear
    - Acheived - the membership page clearly explains the benefits of purchasing membership
-	to be able to choose from an option of subscriptions
    - Failed - I did not implement any subscription options this would be a future implementation. A user can however purchase multiple membership types from the store.

### Registered User
As a registered user I want...
-	To be able to log in and out easily
    - Acheived - clear navigation to login and logout links
-	To be able to reset my password if needed
    - Acheived - users can receive an email to reset their password if needed
-	To receive conformation I have registered for the site
    - Acheived
-	To have a personalised profile
    - Acheived - the user profile dispalys the classes the user has signed up too and their favourite items from the store
-	To save/remove favourite products to/from my profile
    - Partially Acheived - users can add and remove favourite products but not directly from their profile page
-	To save my delivery details for faster checkout
    - Acheived - users can save their delivery details on thier profile page or checkout page
-	To be able to update my delivery details
    - Acheived - users can update their delivery details on thier profile page
-	To be able to read the fitness blog
    - Failed - the blog ended being outside of scope for this project
### Subscribed User
As a subscribed user I want...
-	My store discount to be obviously visible
    - Acheived - visible on the membership page and in both the checkout and shopping bag views
-	To be able to sign up to a range of classes at the gym
    - Acheived - able to sign up to a range of classes with the click of a button
-	To easily be able to change the class I am signed up to
    - Acheived - able to remove yourself from class with the click of a button
-	To be reminded by email on the morning of a class
    - Failed - out of scope
### Super User
As a superuser I want…
-	To be easily able to add/edit and delete products
    - Acheived - product management allows users to add products and they can be edited/deleted in the store and product details views
-	To be able to add blog posts
    - Failed - the blog ended being outside of scope for this project
-	To be able to edit and delete all blog posts and comments
    - Failed - the blog ended being outside of scope for this project
-	To be able to view and manage site users
    - Partially acheived - can mange site users through admin
-	To be able to add/edit and remove classes from the timetable
    - Failed - no crud functionallity was implented for classes
## Known Bugs
---
