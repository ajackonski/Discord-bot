import discord
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author.name == "AlexJ":
            await message.channel.send('Dante please be quiet you\'re scaring the hoes')
