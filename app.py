from flask import Flask, render_template, request, redirect, session
import requests
from threading import Thread
from config import *

app = Flask(__name__)
app.secret_key = 'super secret key'

class User():
    def __init__(self, username=None, discriminator=None, _id=None, avatar_hash=None):
        self.username = username
        self.discriminator = discriminator
        self.id = _id
        self.avatar_hash = avatar_hash
        self.avatar_url = f"https://cdn.discordapp.com/avatars/{_id}/{avatar_hash}.png?size=1024"
        

@app.route("/")
def home():
    access_token = session.get("access_token")

    if not access_token:
        return render_template("index.html")

    try:
      user_json  = requests.get("https://discord.com/api/users/@me", headers={"Authorization": f"Bearer {access_token}"})
      user_json = user_json.json()
  
      user = User(
          user_json["username"],
          user_json["discriminator"],
          user_json["id"],
          user_json["avatar"]
      )
  
      return render_template("index.html", user=user)
    except:
      return render_template("index.html")

@app.route("/logout")
def logout():
    session.pop("access_token")
    return redirect("/")

@app.route("/joinserver/<userid>/")
def joinserver(userid : int):
    access_token = session.get("access_token")

    data = {
        "access_token" : access_token
    }
    headers = {
        "Authorization": f"Bot {BOT_TOKEN}",
        "content-type": "application/json"
    }

    response_json  = requests.put(f"https://discordapp.com/api/guilds/763348615233667082/members/{userid}", json=data, headers=headers)
    print(response_json.status_code)

    return redirect("/")

@app.route("/login")
def login():
    return redirect(OAUTH_URL)
    
@app.route("/oauth/callback", methods=["GET", "POST"])
def oauth_callback():
    code = request.args["code"]

    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'Authorization' : f"Bot {BOT_TOKEN}"
    }
    get_access_token = requests.post('https://discord.com/api/oauth2/token', data=data, headers=headers).json()

    session["access_token"] = get_access_token["access_token"]

    return redirect("/")

app.run(host="0.0.0.0", port=PORT)