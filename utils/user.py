import requests

class User():
    def __init__(self, username=None, discriminator=None, _id=None, avatar_hash=None):
        self.username = username
        self.discriminator = discriminator
        self.id = _id
        self.avatar_hash = avatar_hash
        self.avatar_url = f"https://cdn.discordapp.com/avatars/{_id}/{avatar_hash}.png?size=1024"


def get_user(access_token, BOT_TOKEN):
    user_json  = requests.get("https://discord.com/api/users/@me", headers={"Authorization": f"Bearer {access_token}"})
    user_json = user_json.json()

    user = User(
        user_json["username"],
        user_json["discriminator"],
        user_json["id"],
        user_json["avatar"]
    )
    
    user_guilds  = requests.get("https://discord.com/api/users/@me/guilds", headers={"Authorization": f"Bearer {access_token}"}).json()

    bot_guilds = requests.get("https://discord.com/api/users/@me/guilds", headers={"Authorization": f"Bot {BOT_TOKEN}"}).json()
    bot_guild_ids = [x["id"] for x in bot_guilds]

    mutual_guilds = []

    for i in user_guilds:
        if i["id"] in bot_guild_ids:
            mutual_guilds.append(i)


    return [user, mutual_guilds]