# API Documentation

## Base URL

https://personal-expenses-api-movz.onrender.com

---

## Authentication

Authentication is handled using JWT tokens with Djoser and Simple JWT.

---

## Register

Create new user account.

**POST** /auth/users/

**Body**
{
"username": "testuser",
"email": "test@email.com",
"password": "12345678"
}

---

## Login (Get Tokens)

**POST** /jwt/create/

**Body**:
{
"email": "testuser",
"password": "12345678"
}

Response:
{
"access": "jwt_access_token",
"refresh": "jwt_refresh_token"
}

---

## Change Password

Change the current user's password.

**POST** /auth/users/set_password/

**Body**:
{
"current_password": "oldpassword123",
"new_password": "newpassword123"
}

---

## Refresh Token

**POST** /jwt/refresh/

**Body**:
{
"refresh": "jwt_refresh_token"
}

---

## Authorization Header (Important)

For protected endpoints, include this header:

Authorization: JWT <access_token>

---

### List Transactions

GET /api/transactions/

Auth: JWT Token

Description:
Returns all transactions for the authenticated user.

---

### Create Transaction

**POST** /api/transactions/

Auth: JWT Token
**Body**:
{
"type": "expense",
"amount": 10.50,
"description": "Lunch",
"date": "2026-02-03"
}

---

### Retrieve Transaction by ID

**GET** /api/transactions/{id}

Auth: JWT Token
Description: Returns details of a specific transaction by ID.

---

### Delete Transaction by ID

**DELETE** /api/transactions/{id}

Auth: JWT Token

---

### Update Transaction (Full)

**PUT** /api/transactions/{id}

Auth: JWT Token
**Body**: (All fields required)
{
"type": "income",
"amount": 50.00,
"description": "Salary",
"date": "2026-02-01"
}

---

### Update Transaction (Partial)

**PATCH** /api/transactions/{id}

Auth: JWT Token
**Body**: (Only fields to update)
{
"amount": 55.00
}

---

## List Categories

**GET** /api/transactions/category

Auth: JWT Token
Description:
Returns all categories for the authenticated user.

---

## Create Category

**POST** /api/transactions/category

Auth: JWT Token
Body:

{
"name": "Food"
}

Description:
Creates a new category for the authenticated user.

---

## Retrieve Category by ID

**GET** /api/transactions/category/{id}

Auth: JWT Token
Description:
Returns details of a specific category by ID.

---

## Delete Category by ID

**DELETE** /api/transactions/category/{id}

Auth: JWT Token

---

## Update Category (Full)

**PUT** /api/transactions/category/{id}

Auth: JWT Token
**Body**: (All fields required)

{
"name": "Groceries"
}

---
