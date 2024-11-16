import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="?", intents=intents)

ascii_to_bold = {
    "A": "𝐀", "B": "𝐁", "C": "𝐂", "D": "𝐃", "E": "𝐄",
    "F": "𝐅", "G": "𝐆", "H": "𝐇", "I": "𝐈", "J": "𝐉",
    "K": "𝐊", "L": "𝐋", "M": "𝐌", "N": "𝐍", "O": "𝐎",
    "P": "𝐏", "Q": "𝐐", "R": "𝐑", "S": "𝐒", "T": "𝐓",
    "U": "𝐔", "V": "𝐕", "W": "𝐖", "X": "𝐗", "Y": "𝐘",
    "Z": "𝐙", " ": " "
}

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ploo(ctx, *, user_input: str = None):
    if not user_input:
        await ctx.send("enter something for me to  𝐏  𝐋  𝐎  𝐎")
        return

    words = user_input.upper().split(" ")
    widened_words = [
        "  ".join(ascii_to_bold.get(char, char) for char in word)
        for word in words
    ]
    final_output = "   ".join(widened_words)
    await ctx.send(final_output)


bot.run("token")
