# personal-expenses-API

## Description
A RESTful API for managing personal expenses, allowing users to track income, expenses, and categories with secure JWT authentication.

## Live Demo
Base URL:
https://personal-expenses-api-movz.onrender.com

## Features
- JWT Authentication using Djoser
- User registration and login
- Manage income and expenses (CRUD operations)
- Category management
- User-specific data isolation (each user can only access their own data)
- Partial updates using PATCH
- Automatic calculation of total income, total expenses, and balance
- Filtering transactions by type, category, and date
- Search functionality for categories
- Ordering transactions by amount, date, and creation time
- Pagination with additional financial summary (income, expenses, balance)
- Prevent deleting a category if it is linked to existing transactions
- Code reusability using a Base View (DRY principle)

## Tech Stack
- Python
- Django
- Django REST Framework
- PostgreSQL (Neon)
- JWT Authentication
- Djoser

## Setup & Installation
1. Clone the repository
```bash
git clone https://github.com/your-username/personal-expenses-api.git
cd personal-expenses-api
```
2. Create and activate a virtual environment
```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Run migrations
```
python manage.py migrate
```
5. Start the development server
```
python manage.py runserver
```

## Environment Variables
Create a `.env` file and add:

```env
SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
DEBUG=True
```

## API Documentation
Full API documentation is available in [API.md](API.md)

## Continuous Integration
This project uses GitHub Actions for basic CI checks.

## Testing
The API can be tested using Postman, Insomnia, or Hoppscotch.