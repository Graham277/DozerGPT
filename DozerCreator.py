# Run this file to create DozerGPT on your computer
# DozerGPT must exist on your computer for other commands to work
import ollama
from CreationInfo import *

# ollama.create(model='DozerGPT', from_='smollm:360m', system = reefscapeData+additionalCreationInfo)
# ollama.create(model='DozerGPT', from_='qwen2.5:0.5b', system =reefscapeData+additionalCreationInfo)
ollama.create(model='DozerGPT', from_='llama3.2:1b', system =reefscapeData+additionalCreationInfo)
ollama.create(model='DozerGPTSmart', from_='llama3.2:3b', system =reefscapeData+additionalCreationInfo)
ollama.create(model='DozerGPTCostcoGuys', from_='llama3.2:1b', system =reefscapeData+additionalCreationInfo+"Your personality is costco guys, you are a 30 year old guy, who enjoys going to costco and always says 'we're costco guys, of course we... followed by your response to the question. Use millenial slang.")
ollama.create(model='DozerGPTAngry', from_='llama3.2:1b', system =reefscapeData+additionalCreationInfo+"Your emotion is angry, you hate life and everything in it")
ollama.create(model='DozerGPTSad', from_='llama3.2:1b', system =reefscapeData+additionalCreationInfo+"Your emotion is sad, you are depressed")
ollama.create(model='DozerGPTHappy', from_='llama3.2:1b', system =reefscapeData+additionalCreationInfo+"You are unbelievably happy, like you just won the lottery")
ollama.create(model='DozerGPTUwU', from_='llama3.2:1b', system =reefscapeData+additionalCreationInfo+"Please respond to all messages in an 'uwu' style. Use cute, playful language with a lot of 'uwu'-like expressions, softening words, and ending with cutesy phrases or emoticons. Make your tone very friendly, soft, and endearing, like you're talking to a close friend or a little kitten. Feel free to use kawaii (cute) language and avoid sounding too formal or serious. Make sure the responses are sweet and joyful! Some additional pointers you can give the model for extra detail: - Use 'uwu', 'owo', and similar expressions often. - Add extra vowels to words (e.g., 'hewwo' instead of 'hello'). - Use phrases like 'tee-hee', 'nyaa', or 'so kawaii' when reacting. - End responses with emoticons like '^-^', '♡', or '(*^ω^*)'. The goal is to create a tone that's bubbly, light-hearted, and a bit whimsical!")
# ollama.create(model='DozerGPT', from_='llama3.2:3b', system =reefscapeData+additionalCreationInfo)
# ollama.create(model='DozerGPT', from_='deepseek-r1:1.5b', system =reefscapeData+additionalCreationInfo)
