# API Documentation

## Base URL

https://personal-expenses-api-movz.onrender.com

---

## Register

Create new user account.

POST /api/accounts/register

Body:
{
"username": "testuser",
"email": "test@email.com",
"password": "12345678"
}

---

## Login (Get Tokens)

POST /api/token/

Body:
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

## Refresh Token

POST /api/token/refresh/

Body:
{
"refresh": "jwt_refresh_token"
}

---

## Authorization Header (Important)

For protected endpoints, include this header:

Authorization: Bearer <access_token>

---

### List Transactions

GET /api/transactions/

Auth: Bearer Token

Description:
Returns all transactions for the authenticated user.

---

### Create Transaction

POST /api/transactions/

Auth: Bearer Token

---

### Retrieve Transaction by ID

GET /api/transactions/{id}

Auth: Bearer Token

---

### Delete Transaction by ID

DELETE /api/transactions/{id}

---

### Update Transaction (Full)

PUT /api/transactions/{id}

Auth: Bearer

---

### Update Transaction (Partial)

PATCH /api/transactions/{id}

Auth: Bearer Token

---
