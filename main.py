# Imports
import datetime
import discord
import os
from dotenv import load_dotenv, dotenv_values
from discord.ext import commands
import ollama
import tbapy
import re

# Tba key
load_dotenv()
tba = tbapy.TBA(os.getenv("TBA_KEY"))

# Get the event depending on the time of year
theDate = datetime.datetime.now()

if (theDate.month < 3):
   theEventIWant = None

elif ((theDate.day < 7) & (theDate.month == 3)):
   theEventIWant = None

elif ((theDate.day < 29) & (theDate.day >= 7) & (theDate.month == 3)):
   theEventIWant = '2025onwel'

elif ((theDate.day in [29, 30]) & (theDate.month == 3)):  
   theEventIWant = '2025onham'

elif ((theDate.day in [1, 2]) & (theDate.month == 4)):
    theEventIWant = '2025onham'

else:
    theEventIWant = '2025oncmp'


# Get data (rankings for an event)
# If there is no data, convey there is no data to the bot by setting data to be "No data", instead of nothing

if(theEventIWant != None):
    rawData = tba.event_rankings(theEventIWant)
    data = str(rawData)
else:
    data = "No data"

# Prints to the local console that the bot is logged in
class Client(commands.Bot):
    async def on_ready(self):
        print(f"Logged in as {self.user}!")
    
        try: #Syncs the slash commands to the server
            guild = discord.Object(id=1338342223749578875) #Dozertest
            synced = await self.tree.sync(guild=guild)
            print(f"Synced {len(synced)} commands to guild {guild.id}")
        except Exception as e: # Prints the error if it doesn't work
            print(f"Error syncing commands: {e}")

# Things to make the bot work with discord
intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

# Specifies which servers the slash command works on
load_dotenv() #loads the .env file
GUILD_ID = discord.Object(id=os.getenv("ServerID"))

# This is the slash command
@client.tree.command(name="dozergpt", description="Talk to DozerGPT", guild=GUILD_ID) #Name must be all lowercase # Change which guild id in .env to change which server it serves
async def DozerGPT(interaction: discord.Interaction, prompt: str):

    try:

        # Send an immediate acknowledgment response to avoid timeout
        await interaction.response.send_message(content=f"Q: {prompt}\n\n ""Processing your request...")

        # Get the response from dozer
        combinedPrompt = 'Here is the data set:' + data + ' \nHere is the prompt from the user:\n' + prompt
        rawResponse = ollama.chat(model='DozerGPT', messages=[{'role': 'user', 'content': combinedPrompt}])
        weirdresponse = str(rawResponse)
        print(weirdresponse)

        #Keep only what's inside the double quotes
        def extract_content(weirdresponse):
            # This regex matches content inside double quotes
            content_regex = r"content=['\"](.*?)(?=['\"][,])"
            only_text = re.findall(content_regex, weirdresponse)
            matchesfinal = "".join(only_text)
            matchesfinal = matchesfinal.replace(r'\n', '\n')  # This will make sure \n is interpreted as a newline
            return matchesfinal

        #Get the output of the regex
        response = extract_content(weirdresponse)

        # Edit the response with the real response
        print(response)
        await interaction.edit_original_response(content=f"Q: {prompt}\n\nA: {response}")

    except discord.errors.NotFound as e:
    # Handle interaction not found errors gracefully
        print(f"Error: Interaction not found - {e}")
        await interaction.followup.send("Sorry, something went wrong. Please try again later.")

    except Exception as e:
        # General error handling
        print(f"Unexpected error: {e}")
        await interaction.followup.send("An unexpected error occurred.")



# Makes it work and log in as the right bot
load_dotenv() #loads the .env file
client.run(os.getenv("DISCORD_TOKEN"))

