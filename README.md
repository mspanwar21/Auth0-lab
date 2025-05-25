# Flask Auth0 Integration

**Name:** Mohit Singh Panwar  
**Student ID:** 041167761  
**Email:** panw0011@algonquinlive.com  

This project demonstrates how to integrate user authentication into a Python web application using the Flask framework and Authlib OAuth library, with **Auth0** as the authentication provider.

---

## 📋 Prerequisites

Make sure you have the following installed:

- Python 3
- pip (Python package manager)
- An Auth0 account

---

## 🔐 Auth0 Configuration

### 1. Create an Application in Auth0:

- Go to the [Auth0 Dashboard](https://manage.auth0.com/) and navigate to **Applications**.
- Create a new **Regular Web Application** or use an existing one.
- Obtain the following details:
  - **Domain**
  - **Client ID**
  - **Client Secret**

### 2. Configure Callback and Logout URLs:

- **Callback URL:** `http://localhost:3000/callback`
- **Logout URL:** `http://localhost:3000`

➡️ Add these URLs to the **Allowed Callback URLs** and **Allowed Logout URLs** fields in your Application Settings.

---

## ⚙️ Project Setup

### 1. Clone the Repository

```bash
git clone <repository_url>
cd <project_directory>
