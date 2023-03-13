import discord
import random

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Bot-oPot est connecté !')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!fourchette'):
        secret = random.randint(1, 100)
        await message.channel.send("Tapez '-1' pour quitter le jeu.")
        nbCoups = 0
        while True:
            msg = await client.wait_for('message')
            if msg.author == client.user:
                continue
            n = int(msg.content)
            if n == -1:
                await message.channel.send("Dommage, vous avez quitté le jeu.")
                break
            nbCoups += 1
            if n < secret:
                await message.channel.send("Le nombre est trop petit.")
            elif n > secret:
                await message.channel.send("Le nombre est trop grand.")
            else:
                await message.channel.send(f"Super, vous avez trouvé en {nbCoups} coups !")
                break

client.run('MTA4NDE0ODczMzg4MjY2NzA5OQ.G4IWCp.ayyNGTnmdAhT7QO-XeQGzDwyIbYLp4DSinlyEA')
