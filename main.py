import discord 
from discord.ext import commands
from discord import app_commands

bot = commands.Bot(command_prefix='!d ', intents=discord.Intents.all())

TOKEN = 'YourTOKEN'

# Bot Events
@bot.event
async def on_ready():
    print("Doloris Ready!")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(961159278788505712)
    text = f"Welcome to the server, {member.mention}!"

    emmbed = discord.Embed(title = 'Welcome to the server!',
                          description = text,
                          color = 0x66FFFF)

    await channel.send(text)
    await channel.send(embed = emmbed)
    # await member.send(text)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(961159278788505712)
    text = f"{member.name} has left the server!"
    await channel.send(text)
    # await member.send(text)

@bot.event
async def on_message(message):
    mes = message.content
    await bot.process_commands(message)

    if mes == 'Hello':
        await message.channel.send('Hello It\'s me!')
    
    elif mes == 'Help':
        await message.channel.send('How can I help you ' + str(message.author.name) + '?')

    
# Bot Commands
@bot.command(name='hello')
async def hello(ctx):
    await ctx.send(f"hello {ctx.author.name}!")

@bot.command(name='repeat')
async def repeat(ctx, msg):
    await ctx.send(msg)

# Bot Slash Commands
@bot.tree.command(name='greetingsbot', description='Let\'s bot greeting you')
async def greetingcommand(interaction):
    await interaction.response.send_message('Greetings (from slash command)')

@bot.tree.command(name='name')
#@app_commands.describe(name="What's your name?")
async def namecommand(interaction, name : str):
    await interaction.response.send_message(f"Hi {name}")

@bot.tree.command(name='creator', description='Creator Description')
async def creatorcommand(interaction):
    emmbed = discord.Embed(title='Chonnawee Tungviwatjinda',
                           description='Freelance Developer',
                           color=0x66FFFF,
                           timestamp=discord.utils.utcnow())
    
    emmbed.set_author(name=interaction.user.name, url='https://github.com/VindeciaRJ', icon_url='https://avatars.githubusercontent.com/u/95084608?v=4')
    #emmbed.add_field(name='/hello1', value="Hello Command1", inline=True)
    #emmbed.add_field(name='/hello2', value='Hello Command2', inline=False)
    #emmbed.add_field(name='/hello3', value='Hello Command3', inline=False)
    #emmbed.set_thumbnail(url=interaction.user.avatar)
    #emmbed.set_image(url=interaction.user.avatar)
    emmbed.add_field(name='google', value="[Google](https://www.google.co.th/)", inline=True)
    emmbed.set_footer(text='Footer', icon_url='https://avatars.githubusercontent.com/u/95084608?v=4')
    await interaction.response.send_message(embed=emmbed)

# Start Bot
bot.run(TOKEN)