# Auto Ria Api

This is the backend API for the Auto Ria Project. It providers various endpoints for handling user, cars, analytics,
payments, and more.

## Technologies

- **Django** - web framework for Python used to build the backend.
- **Django Rest Framework** - For building RESTful APIs.

- **MySQL** - A relational database for storing data about users, cars, and other resources.
- **Celery** - For handling asynchronous tasks like processing emails or long-running operations.
- **Redis** - For caching and storing task queues.
- **drf-yasg** - For automatically generating API documentation.
- **Pillow** - For image processing.

## Installation

### Requirements:

- Python 3.12+
- Poetry for dependency management.
- Docker

### Setup Steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/grigoriy1209/cars_control.git
   cd cars_project
2. Install dependencies:
   poetry install
3. Build and start the Docker containers:
  docker compose up --build
4. Set up environment variables(create a .env file):
     **DEBUG=True**
     **SECRET_KEY=**
     **MYSQL_DATABASE=**
     **MYSQL_USER=**
     **MYSQL_PASSWORD=**
     **MYSQL_HOST=**
     **MYSQL_PORT=**
5. Apply database migrations:
   poetry run python manage.py migrate
6. Run the development server:
   poetry run manage.py runserver

API Documentation 
The API documentation is available through Swagger UI:
 API Documentation: http://localhost:8000/api/doc

Dependencies:
# Main dependencies:
-django
-djangorestframework
-mysqlclient
-celery
-redis
-chanel-redis
-daphne

# Development dependencies:
-isort
-pytest

API Endpoints
# Users
- all_users: /api/all_users/users
- admins: /api/all_users/admins
- authentication: /api/all_users/auth
- accounts: /api/all_users/accounts
# Cars
- car listing: /api/all_cars/listings
- dropout cars: /api/all_cars/dropout_cars/
# Analytics
- Analytics: /api/analytics
# Payments
- payments:/api/payments
# Partners
- Dealerships: /api/partners/dealerships/
- Dealer Admin: /api/partners/dealerships/dealer/
- Dealer Manager: /api/partners/dealerships/dealer/
- Dealer Mechanic: /api/partners/dealerships/dealer/
- Dealer Seller: /api/partners/dealerships/dealer/

