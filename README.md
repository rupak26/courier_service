# Courier Service API

This is a Django-based API for a courier service, handling packages, users, and authentication.

## Features
- User authentication (registration, login)
- Package management (create, update, delete, track)
- RESTful API with Django Rest Framework (DRF)

## Installation
### Prerequisites
- Python 3.13+
- Django 5.1+
- SQLite (default) or PostgreSQL

### Steps
1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd courier_service-main
   ```
2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
4. **Apply migrations:**
   ```
   python manage.py migrate
   ```
5. **Create a superuser (optional):**
   ```
   python manage.py createsuperuser
   ```
6. **Run the development server:**
   ```
   python manage.py runserver
   ```

## API Endpoints
    BASE-URL ----  http://127.0.0.1:8000/
### Authentication
```
SELECT METHOD ON POSTMAN FIRST AND THEN TRY OUT THIS API ENDPOINTS
```
```
- "POST"  '/user/register/'                - Register a new user
- "POST"  '/user/login/'                   - Authenticate and receive a token
```
### Package Management
```
- "GET"   'package/create/'                - List all packages
- "POST"  'package/create/'                - Create a package
- "GET"   'package/create/{id}/'           - Retrieve a package
- "PUT"   'package/create/{id}/'           - Update a package
- "DELETE"  'package/create/{id}/'         - Remove a package
```
## Technologies Used
- **Django** (backend framework)
- **Django Rest Framework (DRF)** (API implementation)
- **SQLite** (database)

## Contributing
Feel free to fork the repository and submit pull requests.


## Made with Love ❤ --(Rupak Biswas)

