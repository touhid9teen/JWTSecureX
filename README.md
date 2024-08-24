# Django To-Do API with JWT Authentication

This project is a To-Do application API built using Django REST Framework. It includes user registration, login, and secure endpoints for managing to-do tasks. The API uses JWT (JSON Web Tokens) for user authentication, ensuring that only authenticated users can access and manage their to-do items.

## Features

- **User Registration**: New users can sign up with a username, email, and password.
- **JWT Authentication**: Users can log in to receive an access token, which is required to interact with the to-do endpoints.
- **To-Do Management**: Authenticated users can create, view, update, and delete their personal to-do items.
- **User-Specific Data**: Each user's to-do list is private and only accessible to them.

## Installation

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- Simple JWT

### Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone # Django To-Do API with JWT Authentication

This project is a To-Do application API built using Django REST Framework. It includes user registration, login, and secure endpoints for managing to-do tasks. The API uses JWT (JSON Web Tokens) for user authentication, ensuring that only authenticated users can access and manage their to-do items.

## Features

- **User Registration**: New users can sign up with a username, email, and password.
- **JWT Authentication**: Users can log in to receive an access token, which is required to interact with the to-do endpoints.
- **To-Do Management**: Authenticated users can create, view, update, and delete their personal to-do items.
- **User-Specific Data**: Each user's to-do list is private and only accessible to them.

## Installation

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- Simple JWT

### Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone git@github.com:touhid9teen/To-Do-app-API-developed-with-Django-REST-Framework-and-Simple-JWT-Authentication.git
    ```

2. **Create a Virtual Environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser (Optional):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the Application:**

   Open your web browser and go to `http://127.0.0.1:8000/`.

