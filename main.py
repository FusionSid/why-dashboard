from flask import Flask, render_template, request, redirect, session
from config import *
from utils import get_user, join_why_server, get_access_token

app = Flask(__name__, template_folder="pages", static_folder="assets")
app.secret_key = 'super secret key'


@app.route("/")
def home():
    access_token = session.get("access_token")

    if not access_token:
        return render_template("index.html")

    return render_template("index.html", user=True)


@app.route("/account")
def account():
    access_token = session.get("access_token")

    if not access_token:
        return redirect("index.html")

    try:
        user = get_user(access_token, BOT_TOKEN)
        return render_template("account.html", user=user[0], mutual=', '.join(i['name'] for i in user[1]))
    except:
        return render_template("account.html")


@app.route("/logout")
def logout():
    session.pop("access_token")
    return redirect("/")


@app.route("/login")
def login():
    return redirect(OAUTH_URL)


@app.route("/joinserver/<userid>/")
def joinserver(userid: int):
    access_token = session.get("access_token")
    
    res = join_why_server(access_token, BOT_TOKEN, userid)

    return redirect("/account")


@app.route("/oauth/callback", methods=["GET", "POST"])
def oauth_callback():
    CODE = request.args["code"]

    response = get_access_token(CLIENT_ID, CLIENT_SECRET, CODE, REDIRECT_URI, BOT_TOKEN)

    session["access_token"] = response["access_token"]

    return redirect("/account")


# Normal Pages:

@app.route("/commands/")
def commands():
    access_token = session.get("access_token")

    if not access_token:
        return render_template("commands.html")

    return render_template("commands.html", user=True)


@app.route("/help/")
def help():
    access_token = session.get("access_token")

    if not access_token:
        return render_template("help.html")

    return render_template("help.html", user=True)


@app.route("/about/")
def about():
    access_token = session.get("access_token")

    if not access_token:
        return render_template("about.html")

    return render_template("about.html", user=True)


app.run(host="0.0.0.0", port=PORT)
