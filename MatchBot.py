import discord
import os
from discord import client


class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            pass
        else:
            print(f"User:  {message.author} Content: ,{message.content}")
            text = message.content
            lowered = text.lower()
            if ("valorant" in lowered):
                await message.channel.send("Valorant to gówno💩")

    async def on_presence_update(self,before,after):
        if before.activity != after.activity:

            print('---------------------------------------')
            print(after.name)
            print(before.activity)
            print(after.activity)
            print('---------------------------------------')
            if(after.activity is not None and after.activity.type == discord.ActivityType.playing):
                if 'VALORANT' in after.activity.name:
                    channel = client.get_channel(743808007665745963)
                    if channel is not None:
                        await channel.send(f'@{after.name} has entered Valorant')



intents = discord.Intents.default()
intents.message_content = True
intents.presences = True
intents.members = True
client = Client(intents=intents)
token = os.getenv('TOKEN')
print(token)

