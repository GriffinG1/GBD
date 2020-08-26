import pydirectinput
from discord.ext.commands import Bot
from discord import file

TOKEN = open('TOKEN.txt', "r").read()
client = Bot(command_prefix='@') #for now

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.channel.id == 740832220780036118:
        if message.content.startswith('hello'):
            await message.channel.send('Hi there! ' + message.author.mention)
        if message.content.startswith('b'):
            pydirectinput.press('z')
        if message.content.startswith('b2'):
            pydirectinput.press('z')
            pydirectinput.press('z')
        if message.content.startswith('b3'):
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
        if message.content.startswith('b4'):
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
        if message.content.startswith('b5'):
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
        if message.content.startswith('b6'):
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
        if message.content.startswith('b7'):
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
        if message.content.startswith('b8'):
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
        if message.content.startswith('b9'):
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
            pydirectinput.press('z')
        if message.content.startswith('a'):
            pydirectinput.press('x')
        if message.content.startswith('a2'):
            pydirectinput.press('x')
            pydirectinput.press('x')
        if message.content.startswith('a3'):
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
        if message.content.startswith('a4'):
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
        if message.content.startswith('a5'):
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
        if message.content.startswith('a6'):
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
        if message.content.startswith('a7'):
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
        if message.content.startswith('a8'):
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
        if message.content.startswith('a9'):
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
            pydirectinput.press('x')
        if message.content.startswith('x'):
            pydirectinput.press('v')
        if message.content.startswith('y'):
            pydirectinput.press('c')
        if message.content.startswith('L'):
            pydirectinput.press('e')
        if message.content.startswith('R'):
            pydirectinput.press('r')
        if message.content.startswith('up'):
            pydirectinput.press('w')
        if message.content.startswith('up2'):
            pydirectinput.press('w')
            pydirectinput.press('w')
        if message.content.startswith('up3'):
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
        if message.content.startswith('up4'):
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
        if message.content.startswith('up5'):
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
        if message.content.startswith('up6'):
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
        if message.content.startswith('up7'):
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
        if message.content.startswith('up8'):
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
        if message.content.startswith('up9'):
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
            pydirectinput.press('w')
        if message.content.startswith('left'):
            pydirectinput.press('a')
        if message.content.startswith('left2'):
            pydirectinput.press('a')
            pydirectinput.press('a')
        if message.content.startswith('left3'):
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
        if message.content.startswith('left4'):
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
        if message.content.startswith('left5'):
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
        if message.content.startswith('left6'):
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
        if message.content.startswith('left7'):
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
        if message.content.startswith('left8'):
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
        if message.content.startswith('left9'):
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
            pydirectinput.press('a')
        if message.content.startswith('down'):
            pydirectinput.press('s')
        if message.content.startswith('down2'):
            pydirectinput.press('s')
            pydirectinput.press('s')
        if message.content.startswith('down3'):
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
        if message.content.startswith('down4'):
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
        if message.content.startswith('down5'):
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
        if message.content.startswith('down6'):
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
        if message.content.startswith('down7'):
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
        if message.content.startswith('down8'):
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
        if message.content.startswith('down9'):
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
            pydirectinput.press('s')
        if message.content.startswith('right'):
            pydirectinput.press('d')
        if message.content.startswith('right2'):
            pydirectinput.press('d')
            pydirectinput.press('d')
        if message.content.startswith('right3'):
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
        if message.content.startswith('right4'):
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
        if message.content.startswith('right5'):
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
        if message.content.startswith('right6'):
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
        if message.content.startswith('right7'):
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
        if message.content.startswith('right8'):
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
        if message.content.startswith('right9'):
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
            pydirectinput.press('d')
        if message.content.startswith('d-up'):
            pydirectinput.press('8')
        if message.content.startswith('d-left'):
            pydirectinput.press('4')
        if message.content.startswith('d-down'):
            pydirectinput.press('2')
        if message.content.startswith('d-right'):
            pydirectinput.press('6')
        if message.content.startswith('start'):
            pydirectinput.press('enter')
        if message.content.startswith('select'):
            pydirectinput.press('space')
        if message.content.startswith('f'):
            pydirectinput.press('f')
            pydirectinput.press('tab')
            pydirectinput.press('tab')
            pydirectinput.press('tab')
            pydirectinput.press('enter')
            pydirectinput.press('tab')
            pydirectinput.press('enter')
            channel = client.get_channel("740832220780036118")
            await message.channel.send(file=discord.File(r'C:\Users\camer\Desktop\emu_bot\PokemonCrystalVersion.png'))

client.run(TOKEN)