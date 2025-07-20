📚 Bookstore Management System

📝 Project Description

A robust and scalable web application built with Django, designed to manage a digital bookstore. This system provides comprehensive functionalities for both regular users to interact with book data and superusers to administer the entire book catalog, categories, and related information. It features secure user authentication, data validation, and efficient data management.

✨ Key Features

This application offers a wide range of features to ensure a complete bookstore management experience:

User-Facing Features:

Book Management:


Create New Book: Users can add new book entries to the system.

View Specific Book: Display detailed information for a particular book.

Edit/Delete Book: Modify or remove existing book entries (if authorized).

List All Books: View a comprehensive list of all available books.

Book Details: Each book entry includes:


title

description

rate (rating)

views (number of times viewed)

user (the user who created the book)

categories (one or more categories the book belongs to)

ISBN (International Standard Book Number, uniquely linked to the book)

User Authentication & Authorization:


Login & Sign-up: Secure user registration and login functionality.

Required Login: Certain views require users to be logged in to access.

Permission-Based Access: Specific views require particular user permissions.

Admin-Facing Features (Superuser Privileges):

Admin Panel Access: Superusers can access Django's powerful administration panel.

CRUD Operations on Books: Full Create, Read, Update, Delete capabilities for all books directly from the admin interface.

Book Filtering & Display: Enhanced admin panel to easily display and filter books based on various criteria.

Admin Stacked Model Usage: Demonstration of StackedInline for a more organized display of related objects (e.g., ISBN within Book in the admin).

Backend & Data Management:
Book Model: A well-defined Book model to represent book entities.

Relationships:

User Relationship: Each book is linked to an existing user.

Category Relationship: Each book can belong to one or more categories.

ISBN Relationship: A one-to-one relationship with a unique ISBN object.

ISBN Model: Each ISBN object contains:

author_title

book_title

auto-generated ISBN number

Database Integration: Configured to work with either MySQL or PostgreSQL for robust data storage.

CRUD Operations from Database: Core CRUD operations are implemented directly with the database.

Static Files Management: (Bonus) Proper handling and serving of static assets (CSS, JS, images).

Signal Implementation: (Bonus) A Django signal is implemented to automatically create an ISBN object and assign it to a book upon book creation.

Data Validation:

Book Title Length: The title of a book must be between 10 and 50 characters long (applied in both normal views & Admin).

Category Name Length: The minimum length for a category name is 2 characters (applied in both normal views & Admin).

🛠️ Technologies Used

Python 3.x: The core programming language.

Django 4.x: Web framework for rapid development.

PostgreSQL: Relational database management system 

Jinja2, HTML, CSS, JavaScript: For frontend development.

🚀 Installation & Setup

Follow these steps to get the project up and running on your local machine.

1. Clone the Repository:
   
Bash

git clone https://github.com/alyaah95/Book_Store.git
cd Book_Store

2. Create a Virtual Environment (Recommended):

Bash

python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

3. Install Dependencies:
   
Bash

pip install -r requirements.txt

4. Configure Database:
   
For PostgreSQL:


Install PostgreSQL and create a new database (e.g., bookstore_db).

Update DATABASES settings in bookstore_project/settings.py (or your project's settings.py file) with your database credentials:

Python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookstore_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
For MySQL:


Install MySQL and create a new database (e.g., bookstore_db).

Update DATABASES settings in bookstore_project/settings.py (or your project's settings.py file) with your database credentials:

Python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bookstore_db',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
5. Run Migrations:

Bash

python manage.py makemigrations
python manage.py migrate
6. Create a Superuser (for Admin Panel access):
Bash

python manage.py createsuperuser
Follow the prompts to set up username, email, and password.

7. Collect Static Files (if deployed):
   
Bash

python manage.py collectstatic
8. Run the Development Server:

Bash

python manage.py runserver
The application will be accessible at http://127.0.0.1:8000/.
The Admin Panel will be accessible at http://127.0.0.1:8000/admin/.

💡 Usage

Browse Books: Navigate to the home page (http://127.0.0.1:8000/) to view the list of books.

User Registration/Login: Use the /signup and /login URLs to create an account or log in.

Create/Edit Books: Logged-in users can create new books and manage their own books (if permissions allow).

Admin Panel: Log in as a superuser at /admin to access full CRUD operations for books, categories, users, and other data models.

🤝 Contributing

Contributions are welcome! If you have suggestions or want to improve the project, please follow these steps:

Fork the repository.

Create a new branch (git checkout -b feature/YourFeatureName).

Make your changes.

Commit your changes (git commit -m 'Add new feature').

Push to the branch (git push origin feature/YourFeatureName).

Open a Pull Request.


🧑‍💻 Author

Alyaah95

GitHub: https://github.com/alyaah95

