# DozerGPT

DozerGPT is a fun side project created for the BCR discord server. It is a Discord bot built with an LLM  using **Llama 3.2:1b** with **Ollama**. The bot is specifically trained with knowledge about **FIRST Robotics** and our team. It interacts with **The Blue Alliance (TBA)** API to retrieve live **rankings** for the current event your team is participating in.

### Key Features:
- **Live Event Rankings**: The bot fetches **real-time rankings** for the current event your team is attending from The Blue Alliance API. It does **not** provide any other event data.
- **FIRST Robotics & Team Knowledge**: The bot is trained with knowledge about FIRST Robotics and your team, answering general questions related to the competition.
- **Slash Command Interactions**: Users can interact with the bot through a simple slash command in Discord to get relevant FIRST Robotics information, particularly focused on your team and event rankings.

## Getting Started

### Prerequisites
- **Python** installed on your machine.
- **Ollama** (Install from [Ollama website](https://ollama.com)).
- Some Python packages installed via **pip**:
  - `ollama`
  - `tbapy`
  - `discord`
  - `python-dotenv`

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/DozerGPT.git
   cd DozerGPT
   ```

2. Install dependencies: Use pip to install the required packages:
   ```bash
   pip install ollama tbapy discord python-dotenv
   ```

3. Create a .env file: In the root of the project directory, create a .env file and add the following environment variables:
   - `TBA_KEY='your_tba_key_here'`
   - `DISCORD_TOKEN='your_discord_token_here'`
   - `SERVER_ID='your_server_id_here'`

   - **TBA_KEY**: Get your TBA key by creating an account on The Blue Alliance.
   - **DISCORD_TOKEN**: This is the token for your Discord bot. You can get this from the Discord Developer Portal.
   - **SERVER_ID**: Right-click on your server in Discord (with Developer Mode enabled) to copy the server ID.

   Make sure each variable is on a separate line.

4. Run the bot:
   - First, run the `DozerCreator.py` file to initialize the bot:
   ```bash
   python DozerCreator.py
   ```

   - Then, run the `main.py` file to start the Discord bot:
   ```bash
   python main.py
   ```

5. Interact with the bot: After running the bot, you can interact with it on your Discord server using slash commands.

### Using `CallFromJS.py`

The `CallFromJS.py` file is used by a separate Discord bot called `dozer-discord-bot`, which is written in JavaScript. This file performs essentially the same function as `main.py`, but integrates with the JavaScript framework of the other bot.

To use `CallFromJS.py`:

1. Ensure the environment variables are set up as described above.
2. The `dozer-discord-bot` will call this file as needed to process commands and retrieve responses from DozerGPT.
3. The responses are written to a file (`response.txt`) which the JavaScript bot reads and sends back to the user.

This setup allows for seamless integration between the Python-based DozerGPT and the JavaScript-based `dozer-discord-bot`.