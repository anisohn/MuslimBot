
# MuslimBot

MuslimBot is a Discord bot designed to help users with prayer notifications, prayer times, and Islamic Q&A.

## Features

- **Prayer Time Notifications**: Sends reminders for each prayer time.
- **Prayer Time Command**: Use `/prayertime` to display today's prayer times.
- **Islamic Q&A**: Use `/question` to ask questions about Islam, and the bot provides answers.

## Setup Instructions

### Prerequisites

- **Python 3.7+**
- **Discord bot token** (from [Discord Developer Portal](https://discord.com/developers/applications))
- **Libraries** (install via `requirements.txt`)

### 1. Clone the Repository
```bash
git clone https://github.com/username/MuslimBot.git
cd MuslimBot
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root:
```
TOKEN=your_discord_bot_token
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Bot

```bash
python main.py
```

### Commands and Usage

- **/prayertime** – Displays today's prayer times.
- **/question <query>** – Ask an Islamic question.

### Code Structure

- **main.py** – Main bot logic and commands.
- **get_prayer_time.py** – Retrieves prayer times.
- **ask_question.py** – Handles Q&A for Islamic questions.

### License

This project is licensed under the MIT License.

