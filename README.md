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

![image](https://github.com/user-attachments/assets/ab220b4b-8ff5-4c46-b1c3-6b61c62cce23)


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

## 📄 Install Dependencies

Create a file named `requirements.txt` with the following content:

```txt
flask>=2.0.3
python-dotenv>=0.19.2
authlib>=1.0
requests>=2.27.1
```

Then, install all dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Configuration

Create a `.env` file in the root directory of your project and add the following variables:

```env
AUTH0_CLIENT_ID=<Your Auth0 Client ID>
AUTH0_CLIENT_SECRET=<Your Auth0 Client Secret>
AUTH0_DOMAIN=<Your Auth0 Domain>
APP_SECRET_KEY=<Your Generated Secret Key>
```

### Generate a secure secret key:
```bash
openssl rand -hex 32
```

---

## 🚀 Running the Application

Start your Flask server by running:

```bash
python3 server.py
```

Then open your browser and go to:

```
http://localhost:3000
```

---

✅ You're now ready to test login, logout, and protected routes with Auth0!
