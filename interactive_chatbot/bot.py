import discord
from discord.ext import commands
import json
import os
import difflib
import string


MEMORY_FILE = "memory.json"
SIMILARITY_CUTOFF = 0.6  # Adjust for typo tolerance

# ====== Normalize text ======
def normalize(text):
    return text.lower().translate(str.maketrans("", "", string.punctuation)).strip()

# ====== Load memory ======
def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    try:
        with open(MEMORY_FILE, "r") as f:
            content = f.read().strip()
            return json.loads(content) if content else {}
    except json.JSONDecodeError:
        print("⚠️ memory.json is invalid. Starting fresh.")
        return {}

# ====== Save memory ======
def save_memory():
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)

# ====== Get fuzzy-matched response ======
def get_response(message):
    msg = normalize(message)
    if msg in memory:
        return memory[msg]
    matches = difflib.get_close_matches(msg, memory.keys(), n=1, cutoff=SIMILARITY_CUTOFF)
    if matches:
        return memory[matches[0]]
    return None

# ====== Init ======
memory = load_memory()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# ====== Message Handling ======
@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return
    if message.guild is None:
        return  # Optional: ignore DMs

    await bot.process_commands(message)  # Handle commands if any

    content = normalize(message.content)
    response = get_response(content)

    if response:
        await message.channel.send(response)
    else:
        await message.channel.send("🤔 I don't know how to respond. What should I say?")

        def check(m):
            return m.author == message.author and m.channel == message.channel

        try:
            reply = await bot.wait_for("message", timeout=30.0, check=check)
            memory[content] = reply.content.strip()
            save_memory()
            await message.channel.send("✅ Got it! I'll remember that.")
        except:
            await message.channel.send("⌛ You didn’t reply in time. Maybe next time!")


bot.run("")
