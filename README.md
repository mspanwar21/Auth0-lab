Name : Mohit Singh Panwar   
Student Id: 041167761
Email: panw0011@algonquinlive.com
Flask Auth0 Integration
This project demonstrates how to integrate user authentication into a Python web application using the Flask framework and Authlib OAuth library, with Auth0 as the authentication provider.

Prerequisites
Before starting, make sure you have the following installed:

Python 3
pip (Python package manager)
An Auth0 account
Auth0 Configuration
Create an Application in Auth0:

Go to the Auth0 Dashboard and navigate to Applications.
Create a new application or use an existing one.
Obtain the following details:
Domain
Client ID
Client Secret
Configure Callback and Logout URLs:

Callback URL: http://localhost:3000/callback
Logout URL: http://localhost:3000
Add these URLs in the Allowed Callback URLs and Allowed Logout URLs fields under Application Settings.
Project Setup
Clone the Repository:

git clone <repository_url>
cd <project_directory>
Create a Virtual Environment (Optional but Recommended):

python3 -m venv venv
source venv/bin/activate  # On MacOS/Linux
.\venv\Scripts\activate  # On Windows
Install Dependencies: Create a requirements.txt file with the following content:

flask>=2.0.3
python-dotenv>=0.19.2
authlib>=1.0
requests>=2.27.1
Then, install the dependencies using:

pip install -r requirements.txt
Environment Configuration
Create a .env file in the root directory with the following variables:

AUTH0_CLIENT_ID=<Your Auth0 Client ID>
AUTH0_CLIENT_SECRET=<Your Auth0 Client Secret>
AUTH0_DOMAIN=<Your Auth0 Domain>
APP_SECRET_KEY=<Your Generated Secret Key>
Generate a suitable APP_SECRET_KEY using the following command:

openssl rand -hex 32
Running the Application
Start the Flask server using:

python3 server.py
Open your browser and visit: http://localhost:3000