# API Documentation

## Base URL

https://personal-expenses-api-movz.onrender.com

---

## Authentication

Authentication is handled using JWT tokens with Djoser and Simple JWT.

---

### Register

Create new user account.

**POST** /auth/users/

**Body**
{
"username": "testuser",
"email": "test@email.com",
"password": "12345678"
}

---

### Login (Get Tokens)

**POST** /jwt/create/

**Body**:
{
"email": "test@email.com",
"password": "12345678"
}

Response:
{
"access": "jwt_access_token",
"refresh": "jwt_refresh_token"
}

---

### Change Password

Change the current user's password.

**POST** /auth/users/set_password/

**Body**:
{
"current_password": "oldpassword123",
"new_password": "newpassword123"
}

---

### Refresh Token

**POST** /jwt/refresh/

**Body**:
{
"refresh": "jwt_refresh_token"
}

---

### Authorization Header (Important)

For protected endpoints, include this header:

Authorization: Bearer <access_token>

---

## Transactions
### List Transactions

GET /api/transactions/

Auth: Bearer Token

Description:
Returns all transactions for the authenticated user.

---

### Create Transaction

**POST** /api/transactions/

Auth: Bearer Token
**Body**:
{
"type": "expense",
"amount": 10.50,
"description": "Lunch",
"date": "2026-02-03",
"category": 1
}

---

### Retrieve Transaction by ID

**GET** /api/transactions/{id}

Auth: Bearer Token
Description: Returns details of a specific transaction by ID.

---

### Delete Transaction by ID

**DELETE** /api/transactions/{id}

Auth: Bearer Token

---

### Update Transaction (Partial)

**PATCH** /api/transactions/{id}
Updates specific fields of a transaction.
Auth: Bearer Token
**Body**: (Only fields to update)
{
"description": "Lunch",
"date": "2026-02-03",
"category": 1
}

---

## Categories
### List Categories

**GET** /api/transactions/category

Auth: Bearer Token
Description:
Returns all categories for the authenticated user.

---

### Create Category

**POST** /api/transactions/category

Auth: Bearer Token
Body:

{
"name": "Food"
}

Description:
Creates a new category for the authenticated user.

---

### Retrieve Category by ID

**GET** /api/transactions/category/{id}

Auth: Bearer Token
Description:
Returns details of a specific category by ID.

---

### Delete Category by ID

**DELETE** /api/transactions/category/{id}

Auth: Bearer Token

---

### Update Category 

**PATCH** /api/transactions/category/{id}

Auth: Bearer Token
**Body**:

{
"name": "Groceries"
}

---
