# Api Key
fileopen = open("C:\\Users\\NEW\\OneDrive\\Documents\\Ai\\Template for AI\\Jarvis\\Data\\Api.txt","r")
API = fileopen.read()
fileopen.close()


# Importing
import openai
from dotenv import load_dotenv #pip install python-dotenv

#Coding

openai.api_key = API
load_dotenv()
completion = openai.Completion()

def ReplyBrain(question, chat_log=None):
    # Read chat log template from a file
    FileLog = open("C:\\Users\\NEW\\OneDrive\\Documents\\Ai\\Template for AI\\Jarvis\\\DataBase\\chat_log.txt", "r")
    chat_log_template = FileLog.read()
    FileLog.close()

    # If no specific chat log is provided, use the template
    if chat_log is None:
        chat_log = chat_log_template

    # Create prompt by appending question to the chat log
    prompt = f'{chat_log}You : {question}\nCubic : '

    # Generate AI response using OpenAI GPT-3
    response = completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=0.3,
        frequency_penalty=0.5,
        presence_penalty=0
    )

    # Extract the generated answer from the response
    answer = response.choices[0].text.strip()

    # Update the chat log with the question and answer
    chat_log_template_update = chat_log_template + f"\nYou : {question} \nCubic : {answer}"

    # Write the updated chat log back to the file
    FileLog = open("C:\\Users\\NEW\\OneDrive\\Documents\\Ai\\Template for AI\\Jarvis\\\DataBase\\chat_log.txt", "w")
    FileLog.write(chat_log_template_update)
    FileLog.close()

    return answer
