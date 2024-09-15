# Restaurant Booking Website

The Restaurant Booking Website is a restaurant website that enables customers to book a table online.
People who would like to book a table online in a restaurant would benefit from using this website.

![Screenshot demonstrating website responsiveness on all screen sizes](#)


# Overview

The Restaurant Booking Website is a web application built using Django and PostgreSQL, which allows customers to create an account and log in to the website. Customers can select a table, date, time, and number of guests for their reservations, ensuring the guest count does not exceed the table's maximum capacity. Restaurant owners can manage their bookings, view upcoming reservations, and manage customers through an intuitive admin panel.


# User stories

## Admin wants to view all bookings

As an admin, I want to view all bookings so that I can manage the restaurant’s reservations.

## Admin wants to prevent a double bookings

As an admin, I can prevent a double booking so that I can guarantee that a table can't be booked twice for the same date and time.

## User wants to view the restaurant menu

As a user, I want to view the restaurant menu so that I can see what food options are available.

## User wants to book a table for a specific date and time

As a user, I want to book a table for a specific date and time so that I can plan my visit to the restaurant.

## User wants to specify the number of guests for their booking

As a user, I want to specify the number of guests for my booking so that the restaurant can prepare the necessary meals and seating.

## User wants to receive a confirmation message as soon as they book a table

As a user, I want to receive a confirmation message after booking a table so that I know my booking has been successfully recorded.

## User wants to be able to cancel their booking

As a user, I want to be able to cancel my booking so that I can change my plans if necessary.

## User wants to be able to update a booking

As a user, I want to update any of my bookings so that I my updated booking will suit my new needs and circumstances.

## User wants to register on the restaurant website

As a user, I can register on the restaurant website so that I can sign in to my account.

## User wants to sign in to their account on the restaurant website

As a user, I can sign in to my account on the restaurant website so that I can book a table.

## User wants to sign out of their account on the restaurant website

As a user, I can sign out of my account on the restaurant website so that I my account stays safe.


# Features

User Authentication: Sign up, log in, and log out.
Table Reservations: Book tables by selecting the desired time slot and the number of guests.
Booking Management: View, edit, and cancel reservations.
Admin Panel: Manage restaurants, tables, reservations, and customers with full CRUD operations.
RESTful API: Access and manage users, tables, and reservations through a comprehensive API.


## Navigation bar

The fully responsive navigation bar is featured on all pages, includes links to each of the home, gallery, menu, contact pages and register, sign in, my booking, sign out, and book a table forms and is identical on each page to allow for easy navigation.
This section will allow a user to easily navigate from page to page.

![Navigation bar](/assets/readme_image/navigation_bar.jpg)


## Home page

The home page shows a close-up of a part of the restaurant with a blurry background and inscription "Welcome to Restaurant No1"
"Experience the best food and drinks in town".
Buttons
"Our Menu" / "Log In" / "Register Now"
Below are screenshot of the home page.

![Home page](/assets/readme_image/home_page.jpg)


## Gallery page

This gallery page changes the about us section because a picture speaks louder than words. Here there is a possibility to expand the gallery with additional images as needed.
It tells a user about "Restaurant No1" is a family-owned restaurant in Germany that offers its customers various, tasty, healthy meals and drinks.
Additionally, it emphasizes that a customer can easily book a table online as soon as they will have registered on the restaurant website.
Below are screenshot of the "Gallery".

![Gallery page 1](/assets/readme_image/gallery_page_1.jpg)

![Gallery page 2](/assets/readme_image/gallery_page_2.jpg)

![Gallery page 3](/assets/readme_image/gallery_page_3.jpg)


## Menu

The restaurant menu exist on the menu page.
It contains only 3 items, each has an image. The menu is presented with three options and has the possibility to increase the offer if necessary.
All meals and drinks images are fully responsive on all screen sizes.
Below are screenshot of the restaurant menu.

![Menu page](#)


## Contact page

The restaurant contact form exist on the navigation bar.
It contains 3 field and 1 submit button. The contact form is presented with fields: Name, Email, Message through this form, the user can get in touch with the restaurant staff if they have additional questions.
Below are screenshot of the restaurant contact page.

![Contact page empty](/assets/readme_image/contact_page_empty.jpg)

![Contact page full](/assets/readme_image/contact_page_full.jpg)

![Contact page with error](/assets/readme_image/contact_page_with_error.jpg)


## Register

On the register page, there is a register form that enables a customer to register by entering a username, an email, and a password.
A user must confirm their password.
The register form examines the right formula of an email. If its formula was not correct, an error message will appear.
As a user enters their password, and user confirms their password, the two must be identical. If they are not, an error message will become visible.
Below are eight screenshots of the register form.

![Register customer error password not match](/assets/readme_image/register_customer_error_password_not_match.jpg)

![Register customer error email](/assets/readme_image/register_customer_error_email.jpg)


## Login

A Login button exists on the home page.
To login, a registered user must enter their username and password.
A registered user must enter a valid username and password, if either a username or a password is not valid, an error message arises.
As a user successfully signs in, a confirmation message materializes, and the user can go into the booking page to be able to book a restaurant table.
Beneath are screenshots that demonstrate the sign-in form.

![Login customer username or password not valid](/assets/readme_image/login_customer_username_or_password_not_valid.jpg)

![Login customer](/assets/readme_image/login_customer.jpg)


## Book a table

The New Booking, My booking and Logout button appears on the nav bar only after a user will have Login.
A logedin user can book a table in restaurant by means of a booking form that is built in the "New Booking" page.
To book a table, a user should choose a certain table for a specific date and time, the user should also choose a certain number of guests.
If the table, date, and time that a user chooses are already booked, an error message appears and encourages the user to choose another table, date, or time to be able to book a table.
If a user chooses a number of guests that is not compatible with the capacity of the table that the user wants to book, an error message pops up and notifies the user about that.
As a user successfully books a table, a confirmation message informs the user about that.
Underneath are screenshots that illustrate the details of signing in above. 

![Booking new booking customer](/assets/readme_image/new_booking_customer.jpg)

![Booking new booking customer alert already booked](/assets/readme_image/new_booking_customer_alert_already_booked.jpg)

![Booking new booking customer alert number of guests not allowed](/assets/readme_image/new_booking_customer_alert_number_of_guests_not_allowed.jpg)

![Booking new booking customer alert alrady booked for this date](/assets/readme_image/new_booking_customer_alert_alrady_booked_for_this_date.jpg)

![Booking new booking customer alert booked successfully](/assets/readme_image/new_booking_customer_alert_booked_successfully.jpg)


## My Bookings

The My Bookings button appears on the same nav bar as New Booking and Logout button after a user will have signed in.
Clicking on My Bookings will open the My Bookings table on the website.
On My Bookings page, a Logedin user can see their list of bookings, update them, cancel them or logout.
On each booking, there are all the details of that booking, to the right there are two buttons: Edit and Cancel.
If a user clicks inside a certain booking on the Edit button, a form for updating a booking opens up prepopulated with the settings of the booking that the customer wants to update. The user can choose new settings to be applied for that booking if these are available, that booking will be updated and the user can see into their My Bookings table, where they can find their updated booking. If these are not available, however, an error message arises, tells the user that those settings are already booked, and urges the user to choose other settings to be able to update their booking.
If a user clicks inside a certain booking on the Cancel booking button, that booking will be cancelled and a message comes into sight confirming that that booking has successfully been cancelled.
Below are screenshots that depict the "My Bookings" form.

![My Bookings customer](/assets/readme_image/my_bookings_customer.jpg)

![My Bookings customer logout](/assets/readme_image/my_bookings_customer_logout.jpg)

![My Bookings customer update booking green edit button](/assets/readme_image/my_bookings_customer_update_booking_green_edit_button.jpg)

![My Bookings customer update alert successfully](/assets/readme_image/my_bookings_customer_update_alert_successfully.jpg)

![My Bookings - already booked alert????](#)

![My Bookings customer cancel booking successfully](/assets/readme_image/my_bookings_customer_cancel_booking_successfully.jpg)


## Logout

The Logout button appears on the nav bar only after a user will have login.
When a user clicks on the "Logout" button on the nav bar, user will successfully logout and redirect to home page.

![Customer_logout](/assets/readme_image/my_bookings_customer_logout.jpg)


# Technologies Used

Frontend: HTML, CSS, JavaScript
Backend: Django, Django REST framework
Database: PostgreSQL


# Getting Started

Prerequisites
Python 3.6+
PostgreSQL
Virtual environment tool (e.g., venv)
Heroku CLI (for deployment)


# Installation

1. Clone the repository:
   git clone https://github.com/ROCK3879/restaurant_booking_1.git
   cd restaurant_booking
2. Set up a virtual environment:

```bash
   python -m bvenv env
```

source env/bin/activate # On Windows use.

```bash
\env\Scripts\activate`
```

3. Install dependencies:

```bash
   pip install -r requirement.txt
```

4. Configure the database:
   Create a PostgreSQL database and update the DATABASES setting in restaurant_booking/settings.py:

   ```bash

   DATABASES = {
   'default': {
   'ENGINE': 'django.db.backends.postgresql',
   'NAME': 'yourdbname',
   'USER': 'yourdbuser',
   'PASSWORD': 'yourdbpassword',
   'HOST': 'localhost',
   'PORT': '5432',
   }
   }
   ```

5. Apply migrations:

```bash
   python manage.py migrate
```

6. Create a superuser:

```bash
   python manage.py createsuperuser
```

7. Run the development server:

```bash
   python manage.py runserver
```

8. Access the application:
   Open your web browser and go to http://127.0.0.1:8000/

Database Model

```bash

Table admin {
admin_id integer [primary key]
username string
password string
email string
created_at datetime
}

Table tableList {
table_id integer [primary key]
table_name string
admin_id string
number_guests string
created_at datetime
}

Table reservationTable {
reserved_id integer [primary key]
table_id string
table_name string
customer_id integer
date date
time time
number_guests integerss
created_at datetime
}

Table customer {
customer_id integer [primary key]
customer_username string
customer_email string
customer_password password
created_at datetime
}

ref: customer.customer_id < reservationTable.reserved_id
ref: admin.admin_id < tableList.table_id
ref: tableList.table_id < reservationTable.reserved_id

```

Customer Endpoints

```bash
List Customers: GET /api/customers/
Create Customer: POST /ai/customers/create/
Retrieve Customer: GET /api/users/{id}/
Update Customer: PUT /api/customer/update/<int:pk>/
Delete Customer: DELETE /api/customer/<int:pk>/
```

TableList Endpoints

```bash
List Tables: GET /api/tables//
Create Table: POST /api/tables/create/
Retrieve Table: GET /api/table/<int:pk>/
Update Table: PUT /api/tables/update/<int:pk>/
Delete Table: DELETE /api/tables/<int:pk>/
```

Reservation Endpoints

```bash
List Reservations: GET /api/booktables/
Create Reservation: POST /api/booktable/create/
Retrieve Reservation: GET /api/booktable/<int:pk>/
Update Reservation: PUT /api/booktable/update/<int:pk>/
Delete Reservation: DELETE /api/booktable/<int:pk>/
```

Deployment on Heroku

1. Install the Heroku CLI:

2. Log in to Heroku:

3. Create a new Heroku app:
   heroku create your-website-name

4. Add the PostgreSQL add-on:
   heroku addons:create heroku-postgresql:hobby-dev

5. Set up Heroku environment variables:
   heroku config:set DISABLE_COLLECTSTATIC=1

6. Update settings for Heroku:

```bash

Requirements File (requirements.txt)
asgiref==3.8.1
Django==5.0.7
django-cors-headers==4.4.0
djangorestframework==3.15.2
mysqlclient==2.2.4
sqlparse==0.5.1
tzdata==2024.1
psycopg2-binary==2.9.3
```
