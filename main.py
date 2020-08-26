import pydirectinput
import discord
import json
import os
import sys
import traceback
from discord.ext import commands


if not os.path.exists("config.json"):
    with open("config.json", "w") as f:
        try:
            with open("config.json.sample") as s:
                data = json.load(s)
                json.dump(data, f, indent=4)
        except FileNotFoundError:
            print("Could not find sample file to create config from. Please download from the repo.")
    print("Created config from sample file.")
    input("Press enter to exit.")
    raise sys.exit()

with open("config.json") as f:
    config = json.load(f)
bot = commands.Bot(command_prefix=config["prefix"])


@bot.check
async def is_allowed(ctx):
    if ctx.author.id not in config["accepted_users"]:
        raise commands.errors.CheckFailure()
        return False
    return True


@bot.check
async def globally_block_dms(ctx):
    if ctx.guild is None:
        raise discord.ext.commands.NoPrivateMessage()
        return False
    return True


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandNotFound):
        return
    elif isinstance(error, commands.errors.CheckFailure):
        return await ctx.send("You don't have permission to use this command!")
    elif isinstance(error, commands.errors.NoPrivateMessage):
        return await ctx.send("This bot does not run in DMs.")
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("You're missing required arguments.")
        return await ctx.send_help(ctx.command)
    elif isinstance(error, commands.errors.BadArgument):
        return await ctx.send("A bad argument was provided, please try again.")
    if ctx.command:
        await ctx.send("An error occurred while processing the `{}` command.".format(ctx.command.name))
    tb = traceback.format_exception(type(error), error, error.__traceback__)
    error_trace = "".join(tb)
    print(error_trace)


@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))


button_dict = {
    "a": "x",
    "b": "z",
    "x": "v",
    "y": "c",
    "l": "e",
    "r": "r",
    "up": "w",
    "down": "s",
    "left": "a",
    "right": "d",
    "d-up": "8",
    "d-down": "2",
    "d-left": "4",
    "d-right": "6",
    "start": "enter",
    "select": "space"
}


def repeat_input_x(inp, x):
    for i in range(0, x):
        pydirectinput.press(inp)


def get_screenshot():
    file = discord.File(config["screenshot_path"], "image.png")
    embed = discord.Embed()
    embed.set_image(url="attachment://image.png")
    return embed, file


@bot.command()
async def press_button(ctx, button, repeat: int = None):
    """Hits the provided button repeat number of times"""
    if button not in button_dict.keys():
        raise commands.errors.BadArgument()
    elif repeat is None:
        repeat = 1
    elif 0 <= repeat >= 10:
        await ctx.send(f"Repeat count of {repeat} is outside the valid limits. Inputted value must be between 1 and 9 inclusive. Changing value to 1.")
        repeat = 1
    pressed_button = button_dict[button.lower()]
    repeat_input_x(pressed_button, repeat)
    embed, file = get_screenshot()
    embed.description = f"Pressed the `{button.lower()}` button {repeat} times."
    await ctx.send(file=file, embed=embed)


@bot.command()
async def hello(ctx):
    """Says hello!"""
    await ctx.send(f"Hi there {ctx.author.mention}!")


@bot.command()
async def shutdown(ctx):
    """Shuts down the bot"""
    await ctx.send("Shutting down...")
    await bot.close()

bot.run(config["token"])
