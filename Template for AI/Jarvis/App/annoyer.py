import tkinter as tk
from tkinter import messagebox
import os
import webbrowser
import random
import pyautogui as pg
import time
import datetime

current_time = datetime.datetime.now()
Time = current_time.strftime('%H:%M:%S')
current_date = datetime.date.today()
Date = current_date.strftime('%Y-%m-%d')

def execute_file(num1, num2):

    def print_message():
        message = entry_message.get()
        Number = num1
        Times = num2
        LinkWeb = f'https://web.whatsapp.com/send?phone={Number}'
        webbrowser.open(LinkWeb)

        y = ('''

         ''')

        FileLog = open("C:\\Users\\NEW\\OneDrive\\Documents\\Ai\\Template for AI\\Jarvis\\\DataBase\\annoy_log.txt", "r")
        annoy_log_template = FileLog.read()
        FileLog.close()
        annoy_log_template_update = annoy_log_template + f"\nTime : {Time} \nDate : {Date} \nPhone Number : +91 {num1} \nNumber of messages : {num2} \nMessage : {message}\n {y}"

        # Write the updated phone log back to the file
        FileLog = open("C:\\Users\\NEW\\OneDrive\\Documents\\Ai\\Template for AI\\Jarvis\\\DataBase\\annoy_log.txt", "w")
        FileLog.write(annoy_log_template_update)
        FileLog.close()

        time.sleep(15)

        for _ in range(int(Times)):
            a = message
            pg.write(a)
            pg.press('Enter')

        

    def start_anime():
        animal = ('Monkey', 'Dog', 'Donkey', 'Rat', 'Cat', 'Chicken' ,'Chimpanzee',
        "Gorilla",
        "Baboon",
        "Lemur",
        "Orangutan",
        "Marmoset",
        "Bonobo",
        "Zeedonk (a hybrid between a zebra and a donkey)",
        "Colobus (a type of monkey)",
        "Mule (a hybrid between a donkey and a horse)",
        "Alpaca",
        'Llama',
        "Platypus",
        'Meerkat',
        "Capuchin (a type of monkey)",
        "Bactrian Camel",
        "Okapi",
        "Wallaby",
        "Lemming",
        "Gibbon")

        Number = num1
        Times = num2
        LinkWeb = f'https://web.whatsapp.com/send?phone={Number}'
        webbrowser.open(LinkWeb)

        y = ('''

         ''')

        FileLog = open("C:\\Users\\NEW\\OneDrive\\Documents\\Ai\\Template for AI\\Jarvis\\\DataBase\\annoy_log.txt", "r")
        annoy_log_template = FileLog.read()
        FileLog.close()
        annoy_log_template_update = annoy_log_template + f"\nTime : {Time} \nDate : {Date} \nPhone Number : +91 {num1} \nNumber of messages : {num2} \nMessage : Used ANIMAL preset.\n {y}"

        # Write the updated phone log back to the file
        FileLog = open("C:\\Users\\NEW\\OneDrive\\Documents\\Ai\\Template for AI\\Jarvis\\\DataBase\\annoy_log.txt", "w")
        FileLog.write(annoy_log_template_update)
        FileLog.close()

        time.sleep(15)
        for _ in range(int(Times)):
            a = random.choice(animal)
            pg.write("You are "+a)
            pg.press('Enter')


        else:
            print("Animal file not found.")

    # Create the main application window
    app = tk.Tk()
    app.title("Message Printer App")

    # Calculate the center position for the app window
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    window_width = 200
    window_height = 200
    x_position = int((screen_width - window_width) / 2)
    y_position = int((screen_height - window_height) / 2)

    # Set the app window's geometry to center it on the screen
    app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Create a label and entry widget for the message input
    label_message = tk.Label(app, text="Enter your message")
    label_message.pack(pady=10)
    entry_message = tk.Entry(app)
    entry_message.pack(pady=5)

    # Create the "Ok" button
    btn_ok = tk.Button(app, text="Ok", command=print_message)
    btn_ok.pack(side=tk.TOP, padx=10, pady=10)

    # Create the "Anime" button
    btn_anime = tk.Button(app, text="Animal", command=start_anime)
    btn_anime.pack(side=tk.TOP, padx=10, pady=10)



    

def validate_phone_number(phone_number):
    return phone_number.isdigit() and len(phone_number) == 10

def on_confirm():
    num1 = entry_num1.get()
    num2 = entry_num2.get()

    if not validate_phone_number(num1):
        messagebox.showerror("Invalid Phone Number", "Please enter a valid 10-digit phone number for Number 1.")
    else:
        result_label.config(text=f"Number 1: {num1}\nNumber of Messages: {num2}")

        # Ask for confirmation before executing the file
        confirm = messagebox.askyesno("Confirmation", f"Are you sure you want to send {num2} messages to {num1}?")
        if confirm:
            execute_file(num1, int(num2))  # Convert num2 to an integer

        entry_num1.delete(0, tk.END)
        entry_num2.delete(0, tk.END)
        entry_num1.focus()

# Create the main application window
app = tk.Tk()
app.title("Number Input App")

# Calculate the center position for the app window
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
window_width = 400
window_height = 200
x_position = int((screen_width - window_width) / 2)
y_position = int((screen_height - window_height) / 2)

# Set the app window's geometry to center it on the screen
app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Create labels and entry widgets for number inputs
label_num1 = tk.Label(app, text="Number to which message should be send")
label_num1.pack(pady=5)
entry_num1 = tk.Entry(app)
entry_num1.pack(pady=5)

label_num2 = tk.Label(app, text="How many masseges should be send")
label_num2.pack(pady=5)
entry_num2 = tk.Entry(app)
entry_num2.pack(pady=5)

# Create the confirm button
btn_confirm = tk.Button(app, text="Confirm", command=on_confirm)
btn_confirm.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(app, text="", wraplength=250, justify="left")
result_label.pack()

# Set the focus to the first input field at startup
entry_num1.focus()

# Start the main event loop
app.mainloop()
