# 📁 server.py -----

import json
from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for
from functools import wraps

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if "user" not in session:
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return decorated

# 👆 We're continuing from the steps above. Append this to your server.py file.

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# 👆 We're continuing from the steps above. Append this to your server.py file.

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")

# 👆 We're continuing from the steps above. Append this to your server.py file.

oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)
# 👆 We're continuing from the steps above. Append this to your server.py file.

@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )
# 👆 We're continuing from the steps above. Append this to your server.py file.

@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")
# 👆 We're continuing from the steps above. Append this to your server.py file.

@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )
# 👆 We're continuing from the steps above. Append this to your server.py file.

@app.route("/")
def home():
    return render_template("home.html", session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))
@app.route("/protected")
@requires_auth
def protected():
    user = session["user"]["userinfo"]
    return render_template("protected.html", user=user)

# 👆 We're continuing from the steps above. Append this to your server.py file.

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=env.get("PORT", 3000))

