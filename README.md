# Django Book Management API

This Django project provides a simple API for book management along with user authentication features. It allows users to sign up, log in, and manage a list of books including creating, updating, and deleting book entries.

**Features**
- User Authentication: Users can sign up and log in using their email and password. User authentication is managed using Django's built-in authentication system.
- Book Management: Allows users to create, view, update, and delete books. Each book has attributes such as name, description, and an image URL.

## How to Set Up and Run the Project

**Prerequisites**
- Python 3.8 or above
- Django 3.2 or above
- Basic knowledge of Django and RESTful APIs

**Installation**
1. Clone the Repository:
```
git clone https://github.com/Leera-Consulting/bookmanagement.git
cd bookmanagement
```
2. Setup a Virtual Environment (Optional but recommended):
```
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
```
3. Install Dependencies:
```
pip install django
pip install djangorestframework-simplejwt
pip install Pillow
```
4. Run Migrations:
```
python manage.py makemigrations
python manage.py migrate
```
5. Start the Development Server:
```
python manage.py runserver
```

The server will start on `http://127.0.0.1:8000/`.

**Usage**
The API endpoints include:
- User Signup: `POST /signup/`
- Registers a new user.
- Payload: `{ "email": "<email>", "password": "<password>" }`
- User Login: `POST /login/`
- Authenticates a user.
- Payload: `{ "email": "<email>", "password": "<password>" }`
- List Books: `GET /books/`
- Retrieves a list of all books.
- Create Book: `POST /book/create/`
- Creates a new book entry.
- Payload: `{ "name": "<name>", "description": "<description>", "image": "<image_url>" }`
- Update Book: `PUT /book/update/<book_id>/`
- Updates an existing book.
- Payload: `{ "name": "<name>", "description": "<description>", "image": "<image_url>" }`
- Delete Book: `DELETE /book/delete/<book_id>/`
- Deletes a specific book.

**Testing**
For testing the API, you can use tools like Postman or curl to make requests to the endpoints.

**License**
This project is licensed under the MIT License.

**Contributing**
Contributions to the project are private.