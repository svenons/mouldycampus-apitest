
# API Documentation

This document describes the available endpoints for the API, including their usage, required parameters, authorization methods, and example responses.

---

## Table of Contents

1. [Authentication Endpoints](#authentication-endpoints)
2. [Course Endpoints](#course-endpoints)
3. [Professor Endpoints](#professor-endpoints)
4. [Review Endpoints](#review-endpoints)

---

## Authentication Endpoints

### Login

**URL:** `/api/login`  
**Method:** `POST`  
**Authorization:** None  
**Description:** Authenticate a user and issue an API token.

**Parameters:**
- `email` (string, required): User's email.
- `password` (string, required): User's password.

**Response Example:**
```json
{
  "message": "Login successful",
  "user": { "id": 1, "name": "John Doe", "email": "john@example.com" },
  "token": "access-token-string"
}
```

---

### Register

**URL:** `/api/register`  
**Method:** `POST`  
**Authorization:** None  
**Description:** Register a new user and issue an API token.

**Parameters:**
- `name` (string, required): Full name.
- `email` (string, required): Valid email.
- `password` (string, required): Password (minimum 8 characters).
- `password_confirmation` (string, required): Confirm password.
- `major` (integer, required): ID of the user's major.

**Response Example:**
```json
{
  "message": "Registration successful",
  "user": { "id": 2, "name": "Jane Doe", "email": "jane@example.com" },
  "token": "access-token-string"
}
```

---

### Forgot Password

**URL:** `/api/forgot-password`  
**Method:** `POST`  
**Authorization:** None  
**Description:** Request a password reset link.

**Parameters:**
- `email` (string, required): User's email.

**Response Example:**
```json
{
  "message": "Password reset link sent"
}
```

---

### Reset Password

**URL:** `/api/reset-password`  
**Method:** `POST`  
**Authorization:** None  
**Description:** Reset a user's password.

**Parameters:**
- `token` (string, required): Password reset token.
- `email` (string, required): User's email.
- `password` (string, required): New password.
- `password_confirmation` (string, required): Confirm new password.

**Response Example:**
```json
{
  "message": "Password reset successful"
}
```

---

### Logout

**URL:** `/api/logout`  
**Method:** `POST`  
**Authorization:** Bearer Token  
**Description:** Log out the authenticated user.

**Response Example:**
```json
{
  "message": "Logout successful"
}
```

---

## Course Endpoints

### Get All Courses

**URL:** `/api/courses`  
**Method:** `GET`  
**Authorization:** None  
**Description:** Retrieve a list of all courses.

**Response Example:**
```json
[
  { "id": 1, "name": "Math 101", "description": "Introduction to Math" },
  { "id": 2, "name": "Science 101", "description": "Introduction to Science" }
]
```

---

### Get Course Details

**URL:** `/api/course`  
**Method:** `GET`  
**Authorization:** None  
**Description:** Retrieve details of a specific course, including ratings.

**Parameters:**
- `id` (integer, required): Course ID.

**Response Example:**
```json
{
  "course": { "id": 1, "name": "Math 101", "description": "Introduction to Math" },
  "ratings": [
    { "id": 1, "rating": 5, "comment": "Great course!" },
    { "id": 2, "rating": 4, "comment": "Very informative." }
  ]
}
```

---

## Professor Endpoints

### Get All Professors

**URL:** `/api/professors`  
**Method:** `GET`  
**Authorization:** None  
**Description:** Retrieve a list of all professors.

**Response Example:**
```json
[
  { "id": 1, "name": "Dr. Smith", "department": "Mathematics" },
  { "id": 2, "name": "Dr. Johnson", "department": "Science" }
]
```

---

### Get Professor Details

**URL:** `/api/professor`  
**Method:** `GET`  
**Authorization:** None  
**Description:** Retrieve details of a specific professor, including average rating.

**Parameters:**
- `id` (integer, required): Professor ID.

**Response Example:**
```json
{
  "professor": { "id": 1, "name": "Dr. Smith", "department": "Mathematics" },
  "average_rating": 4.5
}
```

---

## Review Endpoints

### Get Reviews for a Course

**URL:** `/api/reviews`  
**Method:** `GET`  
**Authorization:** None  
**Description:** Retrieve reviews for a specific course.

**Parameters:**
- `course_id` (integer, required): Course ID.

**Response Example:**
```json
[
  { "id": 1, "rating": 5, "comment": "Excellent!" },
  { "id": 2, "rating": 4, "comment": "Good course." }
]
```

---

### Create a Review

**URL:** `/api/createAReview`  
**Method:** `POST`  
**Authorization:** Bearer Token  
**Description:** Submit a review for a course.

**Parameters:**
- `course_id` (integer, required): Course ID.
- `rating` (integer, required): Rating between 1 and 5.
- `comment` (string, optional): Review comment.

**Response Example:**
```json
{
  "message": "Review created successfully"
}
```

---

### Delete a Review

**URL:** `/api/deleteAReview`  
**Method:** `DELETE`  
**Authorization:** Bearer Token  
**Description:** Delete a specific review.

**Parameters:**
- `id` (integer, required): Review ID.

**Response Example:**
```json
{
  "message": "Review deleted successfully"
}
```

---

## Authorization

Most endpoints require a valid Bearer Token for access. You can obtain the token via the `login` or `register` endpoints and include it in the `Authorization` header:

```http
Authorization: Bearer your-token-here
```

---

Feel free to ask for further details if needed!
