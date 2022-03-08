import requests

class User():
    def __init__(self, username=None, discriminator=None, _id=None, avatar_hash=None):
        self.username = username
        self.discriminator = discriminator
        self.id = _id
        self.avatar_hash = avatar_hash
        self.avatar_url = f"https://cdn.discordapp.com/avatars/{_id}/{avatar_hash}.png?size=1024"


def get_user(access_token):
    user_json  = requests.get("https://discord.com/api/users/@me", headers={"Authorization": f"Bearer {access_token}"})
    user_json = user_json.json()

    user = User(
        user_json["username"],
        user_json["discriminator"],
        user_json["id"],
        user_json["avatar"]
    )
    
    return user