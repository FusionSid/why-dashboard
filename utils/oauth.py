import requests

def join_why_server(access_token, BOT_TOKEN, userid):
    data = {
        "access_token": access_token
    }
    headers = {
        "Authorization": f"Bot {BOT_TOKEN}",
        "content-type": "application/json"
    }

    response_json = requests.put(
        f"https://discordapp.com/api/guilds/763348615233667082/members/{userid}", json=data, headers=headers)
    
    return response_json.status_code


def get_access_token(CLIENT_ID, CLIENT_SECRET, code, REDIRECT_URI, BOT_TOKEN):
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
        'Authorization': f"Bot {BOT_TOKEN}"
    }
    response = requests.post('https://discord.com/api/oauth2/token', data=data, headers=headers).json()
    return response