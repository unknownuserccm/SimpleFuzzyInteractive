# Self-Learning Discord Chatbot

A simple Discord chatbot that learns to respond by interacting with users, without any external AI API.  
It stores learned question-answer pairs in a JSON file and uses fuzzy matching to tolerate typos and variations.

---

## Features

- **Self-learning:** Learns new responses from user input dynamically.
- **Fuzzy matching:** Handles minor typos or variations in user messages.
- **Memory persistence:** Saves learned data in a `memory.json` file.
- Ignores messages from bots and in direct messages.

---

## Requirements

- Python 3.8+
- [discord.py](https://discordpy.readthedocs.io/en/stable/) (`pip install discord.py`)

---

## Setup

1. Clone or download this repository.

2. Create a Discord bot via the [Discord Developer Portal](https://discord.com/developers/applications), get your bot token, and invite the bot to your server.

3. Install dependencies:

   ```bash
   pip install discord.py
