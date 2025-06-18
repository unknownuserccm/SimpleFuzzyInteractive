# 🧠 Learning Discord Bot

A simple yet powerful Discord bot that learns responses from users in real-time. When the bot doesn't know how to respond to a message, it asks the user what it should say and remembers it for future conversations!

## ✨ Features

- **🎓 Real-time Learning**: Bot asks users for responses when it doesn't know what to say
- **🔍 Fuzzy Matching**: Handles typos and similar phrases using intelligent text matching
- **💾 Persistent Memory**: Stores all learned responses in a JSON file
- **🔧 Auto-correction**: Normalizes text by removing punctuation and converting to lowercase
- **⚡ Lightweight**: Simple Python script with minimal dependencies
- **🛡️ Error Handling**: Gracefully handles corrupted memory files and timeouts

## 🚀 Quick Start

### Prerequisites

```bash
pip install discord.py
```

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd learning-discord-bot
   ```

2. **Get Discord Bot Token**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create a new application and bot
   - Copy the bot token
   - Add the token to `bot.run("")` at the bottom of the script

3. **Run the bot**
   ```bash
   python bot.py
   ```

4. **Start teaching!**
   - Send a message the bot hasn't seen before
   - When it asks what to respond, reply within 30 seconds
   - The bot will remember your response for future similar messages

## 📁 Project Structure

```
learning-discord-bot/
├── bot.py          # Main bot script
├── memory.json     # Bot's learned responses (auto-generated)
└── README.md       # This file
```

## 🛠️ How It Works

### Learning Process

1. **User sends a message** → Bot normalizes the text (removes punctuation, converts to lowercase)
2. **Bot checks memory** → Looks for exact matches or similar phrases using fuzzy matching
3. **If match found** → Bot responds with the learned response
4. **If no match** → Bot asks "What should I say?" and waits 30 seconds for user input
5. **User responds** → Bot saves the input-response pair to memory.json

### Smart Features

- **Fuzzy Matching**: Uses `difflib` to find similar phrases (handles typos)
- **Text Normalization**: Treats "Hello!" and "hello" as the same input
- **Persistent Storage**: All responses are saved and loaded automatically
- **Timeout Protection**: Learning requests expire after 30 seconds

## 🎮 Usage Examples

### Teaching the Bot

```
User: hello there
Bot: 🤔 I don't know how to respond. What should I say?
User: hi! how are you doing?
Bot: ✅ Got it! I'll remember that.

[Later...]
User: hello there
Bot: hi! how are you doing?
```

### Fuzzy Matching in Action

```
User: hello there
Bot: hi! how are you doing?

User: helo there  (typo)
Bot: hi! how are you doing!  (still matches!)

User: hello ther  (another typo)
Bot: hi! how are you doing!  (matches again!)
```

## ⚙️ Configuration

### Similarity Settings

Adjust the fuzzy matching sensitivity in the script:

```python
SIMILARITY_CUTOFF = 0.6  # Range: 0.0 (very loose) to 1.0 (exact match)
```

- **0.8-1.0**: Very strict matching (fewer typos accepted)
- **0.6-0.8**: Balanced matching (recommended)
- **0.3-0.6**: Loose matching (more typos accepted)
- **0.0-0.3**: Very loose matching (may match unrelated phrases)

### Timeout Duration

Change how long the bot waits for learning responses:

```python
reply = await bot.wait_for("message", timeout=30.0, check=check)  # 30 seconds
```

### Memory File Location

Customize where responses are stored:

```python
MEMORY_FILE = "memory.json"  # Change to your preferred path
```

## 📊 Memory File Format

The bot stores responses in a simple JSON format:

```json
{
    "hello": "hi there how are you",
    "goodbye": "see you later",
    "how are you": "im doing great thanks for asking",
    "what is your name": "im a learning discord bot"
}
```

You can manually edit this file to:
- Add bulk responses
- Fix incorrect responses
- Remove unwanted responses

## 🔧 Advanced Usage

### Bulk Teaching

You can pre-populate the memory.json file with common responses:

```json
{
    "hi": "Hello! How can I help you?",
    "bye": "Goodbye! Have a great day!",
    "thanks": "You're welcome!",
    "good morning": "Good morning! Hope you have a wonderful day!",
    "good night": "Good night! Sweet dreams!"
}
```

### Server-Specific Learning

The bot learns globally across all servers. To make it server-specific, modify the memory structure:

```python
# Example modification for server-specific memory
memory_key = f"{message.guild.id}_{content}"
```

## 🐛 Troubleshooting

### Common Issues

1. **Bot not responding**
   - Check Discord token is correct
   - Ensure bot has "Send Messages" permission
   - Verify bot is online in Discord

2. **Memory not saving**
   - Check file permissions in the bot's directory
   - Ensure the bot has write access to memory.json

3. **Bot responding to other bots**
   - The script already filters out bot messages
   - Check if `intents.message_content = True` is set

4. **Learning timeout issues**
   - Users have 30 seconds to respond to learning prompts
   - Increase timeout value if needed

### Debug Tips

Add logging to see what's happening:

```python
import logging
logging.basicConfig(level=logging.INFO)

# Add to get_response function
print(f"Looking for: '{msg}'")
print(f"Found matches: {matches}")
```

## 🎯 Use Cases

- **Community Servers**: Let members teach the bot server-specific responses
- **Educational**: Learn how basic chatbots work
- **Customer Support**: Pre-train with common questions and answers
- **Fun**: Create personality-driven responses through community input

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 🙏 Acknowledgments

- Built with discord.py
- Uses Python's built-in difflib for fuzzy matching
- Inspired by simple chatbot learning algorithms

## ⚠️ Important Notes

- **Privacy**: All responses are stored in plain text in memory.json
- **Moderation**: Consider adding content filters for public servers
- **Backup**: Regularly backup your memory.json file
- **Rate Limits**: Discord has rate limits - avoid spam learning

---

