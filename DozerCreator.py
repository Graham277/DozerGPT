# Run this file to create DozerGPT on your computer
# DozerGPT must exist on your computer for other commands to work
import ollama
from CreationInfo import *

ollama.create(model='DozerGPT', from_='llama3.2:1b', system =reefscapeData+additionalCreationInfo)
# ollama.create(model='DozerGPT', from_='llama3.2:3b', system =reefscapeData+additionalCreationInfo)
# ollama.create(model='DozerGPT', from_='deepseek-r1:1.5b', system =reefscapeData+additionalCreationInfo)
