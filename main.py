import discord
import os
from os.path import join, dirname
from dotenv import load_dotenv
client = discord.Client()

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BOT_TOKEN = os.environ.get("vc_log_token")

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')


@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == 762884002591801344: # server id
        text_ch = client.get_channel(882893372908503040) # channnel id 
        if before.channel is None:
            msg = f'{member.name} が {after.channel.name} に参加しました。'
            await text_ch.send(msg)

'''
botのトークン
'''
client.run(BOT_TOKEN)