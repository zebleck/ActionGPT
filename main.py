# Import requests library for making API calls
import requests

# Define the API endpoint for ChatGPT Plus
api_url = "https://chatgpt.plus/api/v1/generate"

# Define the preheader for GPT-4 to write code
preheader = "Write commands for setting up a project in a folder to host a website using docker-compose.\n\nCommands:"

# Define the parameters for the API request
params = {
    "model": "gpt-4", # Specify GPT-4 as the model
    "preheader": preheader, # Pass the preheader as input
    "temperature": 0.5, # Set the temperature for randomness
    "top_p": 0.9, # Set the top-p for nucleus sampling
    "max_tokens": 100 # Set the maximum number of tokens to generate
}

# Make the API request and get the response as JSON
response = requests.get(api_url, params=params).json()

# Extract the generated commands from the response
commands = response["text"].split("\n")[1:]

# Print the generated commands
print("Generated commands:")
for command in commands:
    print(command)

# Execute each command using os.system and print the output
import os

print("Executing commands:")
for command in commands:
    print(f"> {command}")
    os.system(command)
    


#v2

# Importing GPT-4 library
import gpt4

# Initializing GPT-4 model
model = gpt4.load_model("actiongpt")

# Setting up a loop variable
loop = True

# Setting up an initial prompt variable
prompt = input("Write a first prompt: ")

# Looping until loop is False
while loop:

  # Generating commands using GPT-4 based on prompt
  commands = model.generate_commands(prompt)

  # Printing commands for user selection
  print("Here are some possible commands:")
  for i, command in enumerate(commands):
    print(f"{i+1}. {command}")

  # Asking user which command(s) to execute
  choice = input("Which command(s) do you want to execute? (Enter numbers separated by commas or 'q' to quit): ")

  # Checking if user wants to quit
  if choice.lower() == 'q':
    loop = False

  else:
    # Converting choice string into a list of integers
    choice_list = [int(x) for x in choice.split(',')]

    # Executing selected commands and storing outputs in a list
    outputs = []
    for i in choice_list:
      output = exec(commands[i-1])
      outputs.append(output)

    # Printing outputs for user feedback
    print("Here are the outputs of your selected commands:")
    for i, output in enumerate(outputs):
      print(f"{i+1}. {output}")

    # Asking user if they want to feed back outputs into GPT-4
    feedback = input("Do you want to feed back these outputs into GPT-4? (y/n): ")

    # Checking if user wants feedback
    if feedback.lower() == 'y':
      # Concatenating outputs into a single string and adding it to prompt
      output_string = '\n'.join(outputs)
      prompt += '\n' + output_string

    # Asking user if they want to give additional info for GPT-4 
    info = input("Do you want to give any additional info for GPT-4? (y/n): ")

    # Checking if user wants info 
    if info.lower() == 'y':
      # Asking user for info and adding it to prompt 
      info_string = input("Enter your additional info: ")
      prompt += '\n' + info_string