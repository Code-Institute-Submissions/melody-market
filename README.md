# Melody Market

![alt text](https://melody-market.s3-eu-west-1.amazonaws.com/media/Image1.JPG)

A website for all music lovers! It functions as an online market for musical instrument - new and used. 
Shopper will have the possibility to search, view and to purchase the products. As an addition, this website will serve as an online community where registered users could exchange their goods (so to speak) as they would be able to post their short messages for other registered users to see and in that way user can sell or buy music related products or search for collaboration.

# UX
-------------------------------------------------
![alt text](https://melody-market.s3-eu-west-1.amazonaws.com/media/image2.JPG)

As the site has a potential to grow, more user stories will appear in a develompent part of creating a content.


# Features
---------------------------------------------------
## Existing Features
### Fixed Navbar

Users have the ability to quickly and smoothly go between the pages on the site as all the pages are reachable through the navbar.

### Search bar 

Users can quickly search for a product by inputing a keyword or exact name of the product.

### Products Viewing

Products are viewed in two ways - 1. as part of the list with a first description in form of a sale pitch.
                                  2. in a detailed view with a second description of product's features and characteristic

### Categorising

Users can categorise the products in all products section pages. Products can be categorised by name, price and ratings in an ascending or descending order.

### Product Count

Total number of products is shown on each page that has a product listing

### Authentication

Users can registrate and login to the site which gives them additional options such as saving purchase history to their profile page and accessing the bulleting board.

### Payment

Users can proceed with a secure checkout service and purchase the selected products.

### Adverts

Registered users can add text and view other users' short ads.

### Toast

Users are notified with pop-up messages after a successful action.

### Product Management

Users with appropriate level of access can modify store's content.

![alt text](https://melody-market.s3-eu-west-1.amazonaws.com/media/image3.JPG) 

Regular users, regardless of registration don't have that option

![alt text](https://melody-market.s3-eu-west-1.amazonaws.com/media/image4.JPG)


## Features Left to Implement

* Messaging system - to allow user to directly contact Melody Market team
* Purchase of the used products directly from the website after which product won't be available for a view to other users
* Mailing list - to notify users about a new product or a deal
* Rating system handled directly by users - current rating system is only editable by superusers.

### Future of the site

Plan for forseeable future is that users can upload their audio files and sell them which will expand the site even further on the market.

# Technologies Used
In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

## Frontend

HTML - for main structure of the website
CSS - for the styling and general looks of the website
JavaScript - for different functionalities of the specific parts of the website such as showing random images of the items on sale
jQuery - used in combination with JavaScript to make DOM manipulation easier
Bootstrap - for a main layout of the website and for quick editing the style of the site.
Font Awesome - for navbar icons

## Backend

Python
Django framework
AWS S3 - for storing media files such as images and static files which contain CSS and JavaScript
Stripe - for secure payments in the checkout process after purchasing a product
Heroku - for the deployment of the web site and public access

# Testing

### Browsing:

* Go to the "Home" page
Try to on any of the links in the navbar and verify that an appropriate dropdown menu appears or it redirects you to another page when clicked on a navbar link without a dropdown menu.
Try to click on each of the products and verify that you are redirected to the page with product's details.

### Register / Sign In
* From anywhere on the site
Try to click on register/login icon and verify that it redirects you to the registration or to the login page.
* On a login page
Try to input all the required details and click on login button and verify that you are now logged and the register/login icon has changed the name to your username and a success message appeared.
* On a registration page
*Known bug*
Try to input all the required details and click on the register button and verify that an error message appears. *(User is registered and that can be checked on the admin page. This is possibly due to restrictions from Gmail as when run locally verification email appears in the console.)*

![alt text](https://melody-market.s3-eu-west-1.amazonaws.com/media/image5.JPG)

### Purchasing
Try to add any of the product to the shopping cart and verify that the cart is now populated and a toast message appears.
* Go to the shopping cart page
Try to click on the shopping cart icon and verify that you are redirected to the shopping cart page.
Try to modify number of purchased items and click on update button and verify that the total sum has been updated.
Try to click on remove button and verify that the item is now removed from the cart and total sum has been updated.
* If no items in a shopping cart 
Verify that an image and a message are showing

### Payment
Try to click on **Go to secure payments** button and verify that you are redirected to the payment page.
Try filling in all the required input fields and click on **Complete order** button and verify that you are redirected to the payment summary page and a toast message appeared.
*Known bug* - Confirmation emails are not sent to the purchaser email. This will be addressed in the future.
* Go to the profile page
Verify that the purchase history appears if purchase was ever made.

### Bulleting Board
* Go to the Bulletin Board page
If not logged in verify that you cannot view the content and you are prompted to register or to login
If **logged in** try to click on Add message button and verify that you are redirected to the add message page.
Try to input all the required fields on the add message page and click on add button and verify that a new message is added when navigating back to the Bulletin Board *(Redirecton to the Bulletin board after this action needs fixing)*
Verify that messages appear in each category of advert accordingly.

### Categorising / Searching
* Go to any page with the products
Try to click on a sort bar, select a desired sort parameter and verify that products are rearranged accordingly.
Try to input any logical keyword or a name of the product, click on search button and verify that you are redirected to the page with the correct search results.

### Managing the Products
* Go to the Product Management page (if logged in as a superuser)
Try to input all the required fields and click on add button and verify that a new product now appears on the appropriate page.
* Go to the any page with products listing
Try to click on edit button and verify that you are redirected to the edit product page.
Try to modify any of the input fields, click on update button and verify that the new product is now updated.
Try to click on delete button and verify that a pop-up message appears prompting confirmation for the action.
Try to click on ok and verify that the product is now removed from the database.

# Deployment

## Heroku

Project was deployed to Heroku and these steps were taken:

1. Go to Heroku https://dashboard.heroku.com/apps and create a new app.
2. Click on the Resources tab and start typing Postgress and select that database for your app deployment.
3. In the Gitpod install dj_database_url and psycopg2 with commands in the terminal: pip3 install dj_database_url and pip3 install psycopg2-binary
4. In the setting.py replace the default database with a Postgress database 'default' : dj_database_url.parse('*Postgress database goes here*')
5. Run the migrations to the new database
6. Create a superuser - python3 manage.py createsuperuser
7. Install gunicorn - pip3 install gunicorn
8. Freeze the changes to the requirements.txt file - pip3 freeze > requirements.txt
9. Create a Procfile with this content - web: gunicorn melody_market.wsgi:application
10. Temporarily disable collectstatic - DISABLE_COLLECTSTATIC=1
11. Add hostname of Heroku app in settings.py - ALLOWED_HOSTS
12. Commit changes, push to GitHub and push to Heroku - git push heroku master
13. Create Amazon Web Services S3 account and create a new bucket, appropriate user's groups and security policies.
14. Connect Django to it by installing 2 new packages - pip3 install boto3 and pip3 install django_storages
15. Freeze the changes to requirements.txt
16. Add new setting to setting.py - AWS_STORAGE_BUCKET_NAME and AWS_S3_REGION_NAME
17. In AWS S3 create new folder - media
18. Add API keys to Heroku config variables

# Credits

Main background image was taken from the Shutterstock website (https://www.shutterstock.com/home) as part of the 10 free images that a user can download during the trial period.

Bulleting board image is taken from Amazon site (https://www.amazon.com/Brands-Bulletin-Board-Inches-Light/dp/B00PRYQ9YU) just for the purposes of this project.

# Content

* All the "sale pitch" product descriptions were made by myself.
* Detailed product description were randomly taken from https://www.thomann.de/ie/ website and they do not reflect the exact product features, they were used rather as a mockup.
* All the images are taken from different sources: https://www.thomann.de/ie/, https://www.waltons.ie/, https://musicshop.hr/
* Logo on the instruments has been removed so it would not represent any specific brand but just to be used for this project purposes.

# Acknowledgements

Inspiration for this project came from the Code Institute's final lessons and have undoubtedly widen my horizons in terms of web develompent.