import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='?')

bot.lavalink_nodes = [
    {"host": "losingtime.dpaste.org", "port": 2124, "password": "SleepingOnTrains"},
    # Can have multiple nodes here
]

# If you want to use spotify search
bot.spotify_credentials = {
    'client_id': '7e550a51880945e08551cbdba16edf7a ',
    'client_secret': 'c94455bccd3d4fde9fea821dc90eef82'
}

bot.load_extension('dismusic')

bot.run("OTczMjU2MTUwODEwMjMwODU1.G-5AHn.JUUgv2vAC7ZztqftSaiHGG73yK1YFXolzHkKH4")