# django-online-shop
An online shop built with Django, PostgreSQL, and modern web technologies.
# OnlineShop_Django

A full-stack e-commerce web application built with Django and PostgreSQL.  
The project provides product management, user authentication, shopping cart functionality, likes, comments, and image uploads.

## Features

- User registration and login system
- Secure password hashing
- Product listing and details
- Shopping cart using Django sessions
- Add and remove products from cart
- Product likes system
- User-specific liked products
- Product comments
- Image upload and media management
- PostgreSQL database integration

## Technologies

- Python
- Django
- PostgreSQL
- HTML / CSS
- JavaScript

## Project Structure

```
OnlineShop_Django/
│
├── shop/              # Main Django application
├── templates/         # HTML templates
├── static/            # Static files (CSS, JS, images)
├── media/             # User uploaded files (not included in GitHub)
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/OnlineShop_Django.git
```

Move into the project directory:

```bash
cd OnlineShop_Django
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file in the project root:

```
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

---

### 5. Apply database migrations

```bash
python manage.py migrate
```

---

### 6. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

---

### 7. Run the development server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

## Database

This project uses PostgreSQL as the database backend.

Make sure PostgreSQL is installed and running before starting the application.

## Media Files

Uploaded images are stored in the `media/` directory.

The `media/` folder is excluded from GitHub using `.gitignore`.

## Security

Sensitive information such as:

- Database credentials
- Django secret key
- Environment variables

are stored in `.env` and are not included in the repository.

## Future Improvements

- Online payment integration
- Product categories
- Order management system
- User profile page
- Advanced search and filtering

## Author

Reza Khodadoost Tohidi