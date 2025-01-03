# Dockerized Flask CRUD Application with PostgreSQL

## Overview
This project is a simple CRUD (Create, Read, Update, Delete) application built using **Flask**, **PostgreSQL**, and containerized using **Docker**. It allows you to perform operations on a `User` entity with fields like `id`, `name`, and `email`. 

### Features
- Create a new user.
- Retrieve all users or a specific user by `id`.
- Update a user's details using `id` or `email`.
- Delete a user by `id` or `email`.

---

## Prerequisites
Ensure you have the following installed:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Project Structure
```plaintext
.
├── backend/
│   ├── app.py                  # Main Flask application
│   ├── Dockerfile              # Docker configuration for Flask
│   ├── requirements.txt        # Python dependencies
│   └── database_setup.sql      # SQL script for setting up the database
├── docker-compose.yml          # Docker Compose configuration
└── README.md                   # Project documentation
```

---

## Installation

### 1. Clone the Repository
```bash
git clone <repository_url>
cd <repository_name>
```

### 2. Build and Run the Application
Run the following command to build and start the containers.Also make sure to start the Docker Desktop for Windows:
```bash
docker-compose up --build
```

---

## API Endpoints

### Base URL
```plaintext
http://localhost:5000
```

### 1. **Get All Users**
- **Endpoint**: `/users`
- **Method**: `GET`
- **Response**:
```json
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com"
    }
]
```

### 2. **Get User by ID**
- **Endpoint**: `/users/<id>`
- **Method**: `GET`
- **Response**:
```json
{
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com"
}
```

### 3. **Add a New User**
- **Endpoint**: `/users`
- **Method**: `POST`
- **Body**:
```json
{
    "name": "Jane Doe",
    "email": "janedoe@example.com"
}
```

### 4. **Update a User**
- **Endpoint**: `/users/<id>`
- **Method**: `PUT`
- **Body**:
```json
{
    "name": "Updated Name"
}
```

### 5. **Delete a User**
- **Endpoint**: `/users/<id>`
- **Method**: `DELETE`

---


## How to Stop the Application
To stop the application, press `CTRL+C` in the terminal where `docker-compose` is running or run:
```bash
docker-compose down
```


## Screenshots
###  API Endpoints Tested via Postman
**Example: Get all users**  
![screenzy-1735902442179](https://github.com/user-attachments/assets/c8b5cc27-783f-412d-bb0e-36eb4d20933d)


**Example: Add user**  
![screenzy-1735902487351](https://github.com/user-attachments/assets/e18d4ec2-b36c-4d56-9d12-ca9c67adc0fe)


**Example: Update user**  
![screenzy-1735902524118](https://github.com/user-attachments/assets/daa7d886-0da4-48e8-aae2-31aa693d1735)


**Example: Delete user**  
![screenzy-1735902554690](https://github.com/user-attachments/assets/05a00e71-e931-4b3d-8d79-6750c3d16833)




