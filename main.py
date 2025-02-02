import discord
from discord import Intents, Client, Message, app_commands
from discord.ext import commands
from responses import get_response
from language_learning import russian_a1, russian_a2, russian_b1, french_a1, french_a2, french_b1, spanish_a1, spanish_a2, spanish_b1, chinese_a1, chinese_a2, chinese_b1
from script1 import ttsActivated
from typing import Final
import os
from dotenv import load_dotenv
from random import randint, choice

TOKEN = "Insert your token here"

intents: Intents = Intents.default()
intents.message_content = True #NOQA
client: Client = Client(command_prefix="!", intents=intents)
GUILD_ID = discord.Object(id="Insert your guild id here")
bot = commands.Bot(command_prefix="!", intents = Intents.all())

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

async def send_russian_a1(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = russian_a1(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

async def send_russian_a2(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = russian_a2(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

async def send_russian_b1(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = russian_b1(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

async def send_french_a1(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = french_a1(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

async def send_french_a2(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = french_a2(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

async def send_french_b1(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = french_b1(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

async def send_spanish_a1(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = spanish_a1(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

async def send_spanish_a2(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = spanish_a2(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

async def send_spanish_b1(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = spanish_b1(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

async def send_chinese_a1(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = chinese_a1(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

async def send_chinese_a2(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = chinese_a2(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

async def send_chinese_b1(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return
    
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = chinese_b1(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print('Logged in as {0.user}' .format(client))
    
@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print("synced {len(synced)} command(s)" )
    except Exception as e:
        print(e)

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    if channel == 'public-chat':
      await send_message(message, user_message)  
    elif channel == 'russian_a1':
        await send_russian_a1(message, user_message)
    elif channel == 'russian_a2':
        await send_russian_a2(message, user_message)
    elif channel == 'russian_b1':
        await send_russian_b1(message, user_message)
    elif channel == 'french_a1':
        await send_french_a1(message, user_message)
    elif channel == 'french_a2':
        await send_french_a2(message, user_message)
    elif channel == 'french_b1':
        await send_french_b1(message, user_message)
    elif channel == 'spanish_a1':
        await send_spanish_a1(message, user_message)
    elif channel == 'spanish_a2':
        await send_spanish_a2(message, user_message)
    elif channel == 'spanish_b1':
        await send_spanish_b1(message, user_message)
    elif channel == 'chinese_a1':
        await send_chinese_a1(message, user_message)
    elif channel == 'chinese_a2':
        await send_chinese_a2(message, user_message)
    elif channel == 'chinese_b1':
        await send_chinese_b1(message, user_message)
    
    else: 
        print('no channel found')

    print(f'[{channel}] {username}: "{user_message}"')
    


def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()