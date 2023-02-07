from discord.ext import commands
import discord
import sys

sys.path.append('modules')
from checkers import *

# bot information
BOT_DESC   = 'A simple bot that scans attachments and links for scam, phishing, and malware mitigation.'
CMD_PREFIX = '?'
BOT_TOKEN  = ''

intent = discord.Intents.default()
intent.members = True
intent.messages = True

bot = commands.Bot(command_prefix=CMD_PREFIX, description=BOT_DESC, intents=intent)

################
#  BOT EVENTS  #
################
@bot.event
async def on_ready():
    print('[+] Bot Started')

##################
#  BOT COMMANDS  #
##################
@bot.command()
async def autoScan(ctx):
    print('[+] Auto scan activated')

    @bot.event
    async def on_message(ctx):
        # scans for possible messages
        pass


if (__name__ == '__main__'):
    # no params provided
    if (len(sys.argv) < 2):
        print('Usage: bot.py <bot_token> [command_prefix]')
        print('Example: bot.py afe523b...ef5a ?')
        exit()

    # first case: a token is provided
    if (len(sys.argv) == 2):
        BOT_TOKEN = sys.argv[1]

    # second case: a token and command prefix provided
    if (len(sys.argv) > 2):
        BOT_TOKEN  = sys.argv[1]
        CMD_PREFIX = sys.argv[2]

    bot.run(BOT_TOKEN)