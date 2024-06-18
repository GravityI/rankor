import discord
from discord.ext import commands
import config_parser as configParser

#Class for CreateGameButton
class CreateGameButton(discord.ui.Button['CreateGameButton']):
    def __init__(self, label):
        super().__init__(label=label, style=discord.ButtonStyle.green)
    
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message('Button clicked!')
    
    async def createGame(self):
        pass

#Class for CreateGameMenu
class CreateGameMenu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(CreateGameButton('Create Game'))

#Class for Bot
class RankorBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=discord.Intents.default())

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        guild = self.guilds[0]
        self.channel = discord.utils.get(guild.text_channels, name=configParser.getMenuChannel())
        await self.clear_channel(10)
        await self.channel.send('Bot Online!\nWhat would you like to do?', view=CreateGameMenu())
        
    async def clear_channel(self, limit: int):
        await self.channel.purge(limit=limit)
    
    async def close(self):
        await self.clear_channel(10)
        

#Initialize Bot
bot = RankorBot()

#Bot Commands

bot.run(configParser.getAuthToken())