import ollama
import re
import sys

prompt = sys.argv[1]

# Get the response from dozergpt
combinedPrompt = 'Respond in less than 2 sentences. \nHere is the prompt from the user:\n' + prompt
rawResponse = ollama.chat(model='DozerGPT', messages=[{'role': 'user', 'content': combinedPrompt}])
weirdresponse = str(rawResponse)

# Keep only what's inside the double quotes function
def extract_content(weirdresponse):
    content_regex = r"content=['\"](.*?)(?=['\"][,])"
    only_text = re.findall(content_regex, weirdresponse)
    joined_together = "".join(only_text)
    response = joined_together.replace(r'\n', '\n')  # This will make sure \n is interpreted as a newline
    return response
response = extract_content(weirdresponse)

# Put the data into the file 
filePath = '/home/dozer/GPTStuff/response.txt'
with open(filePath, "w") as file:
    file.write(response)
