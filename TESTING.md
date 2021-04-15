# Testing

## Navigation

-   The navigation link works as expected, each dropdown links to intended page and describes at what section they will end up at clearly.
-   All the account functionalities work as intended e.g Users can Register, Login, logout and view their profile.
-   The shopping bag populates all expected details and updates accordingly
-   The navbar is responsive on mobile devices.
-   The hamburger menu expands and collapse as expected.

### Search Bar

-   The search bar functions efficiently to help users narrow down their search criteria with a particular keyword.

## Homepage

### Hero Image

-   The Hero image and colors will essentially communicate visual aesthetic state of mind to users, first time user would assimilate the front page caption with various options of self explanatory navigation bar.
-   At the left side of the Hero image there is a "SHOP ALL WATCHES " call to action button that will take users directly to product listing section.

## Product Listing

-   The product listing section populates all products accordingly.
-   The selection form for sorting works properly and users can sort products by Category, Name, Price, and Rating in descending or descending order.
-   When users get at the bottom of the long page, they can quickly get back to the top with a "Back to Top" button.
-   Clicking a particular product will expand detailed information as expected.

## Product Details

-   The product detail page populates comprehensive data set about a particular product.
-   The size adjustment selection form functions properly
-   The Add to bag and Keep Shopping buttons links to intended pages.
-   Review details populates at the bottom page as expected.

## Profile

-   The profile page populates users data accordingly and the already saved information can be updated.
-   The correct order history is displayed accordingly.
-   The "update information" button works properly.
-   Upon completion of the form the profile information updates successfully.
-   Clicking on the order number populates a comprehensive summary about the order.
-   The review link take users directly to review form as intended.

## Shopping Bag

-   The shopping bag populates all purchased product details, subtotal for items purchased and a grand total as intended.
-   The functionalities for users to remove items from the shopping bag and update quantities before checkout works properly.
-   Users have the option to keep shopping or secure checkout.
-   The "Keep Shopping" and "Secure Checkout" buttons links to the intended pages.

## Checkout and Payment

-   Webhooks was tested with post feedback success.
-   Stripe payment functionalities work accordingly
-   The checkout form loads properly.
-   The checkout form populates the saved pre-filled profile as expected.
-   The order summary details are properly displayed.
-   Checkout information can be saved to profile when checkbox is selected.
-   Upon payment users will receive a post email confirmation about their orders 
-   Unsuccessful payment returns feedback accordingly.

## Review

-   The review form works as expected.
-   When users must have completed the review form about their purchased product, the feedback displays at the bottom of product details page as intended.
-   Users can view review at the bottom page of product details.

## Contact

-   The form validation prompts user to input value for all required fields as expected.
-   Contact form sends information accordingly.

## Administrative Features

-   Links to product management in the navigation can only be seen if a user is logged in as an administrator.

### Product Management

### Adding a Product

-   Adding a new product works as intended.
-   All required fields must be filled to add a new product.

### Editing/Deleting a Product

-   Deleting a product from a product page works as intended.
-   The "Select Image" and "Add Product" button on the product management page works as intended.
-   The product edit link takes the administator directly to the product management section
-   The modal form pops up as expected.
-   The delete links, has a pre-warning pop up modal to alert administrator of their actions.
-   When editing a product, the information populates the fields of the form accordingly.
-   The form validation prompts user to input value for all required fields as expected.

## Responsiveness

### Further Testing

* All links were tested. Internal links all work. External links all work and open in new window.
* The Website was tested on Google Chrome, Internet Explorer, Firefox, Microsoft Edge and Safari browsers.
* The website was test run on a variety of devices such as Desktop, Laptop, iPhoneXR, Samsung Note3, Samsung Tab2 & Nokia.
* The site was test run by friends and colleagues for possible user experience issues and bugs.
* All the pages are responsive on all screen sizes.
* The buttons links as expected and the modal form pops up in sync.
* The Search bar generates corresponding feedback data.
* All Codes passed through their respective Validators to erase syntax error.

## Flake8 and Code Refactoring

* To see all the problems across all my files, I invoke the linter manually By using the command **python3 - m flake8** which outputs a list of all the issues to the terminal.

* I have gone through the individual links diligently to fixed them.

## Bugs

### Fixed

* Some pages were generating error feedback because I didn't run a postgress migration.

* This was rectified by resetting the migration;
To reset, I had to delete everything (all migration files and pycache folder) inside every app, inside every migrations folder except the **__init__.py** file.
Then I ran makemigrations again.

No known Bugs as at the time of submitting this project.