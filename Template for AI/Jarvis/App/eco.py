import tkinter as tk
from tkinter import messagebox
import openai

# Set up OpenAI API credentials
openai.api_key = 

# Create the main application window
window = tk.Tk()
window.title("Green Travel Guide")

# Function to plan the trip
def plan_trip():
    destination = destination_entry.get()
    if destination:
        # Use AI to plan the trip
        prompt = f"Plan a beautiful trip to {destination} at a low cost."
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.7
        )

        if response and response.choices:
            trip_details = response.choices[0].text.strip()
            result_label.config(text=trip_details)  # Update the result label
        else:
            messagebox.showinfo("No Results", "No trip details found for the given destination.")
    else:
        messagebox.showerror("Error", "Please enter a destination.")

# Create a label for the title
title_label = tk.Label(window, text="Green Travel Guide", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Create a frame for destination input
input_frame = tk.Frame(window)
input_frame.pack(pady=20)

# Create a label and entry field for destination input
destination_label = tk.Label(input_frame, text="Enter Destination:", font=("Arial", 12))
destination_label.pack(side="left")

destination_entry = tk.Entry(input_frame, font=("Arial", 12), width=30)
destination_entry.pack(side="left")

# Create a button to submit the destination and plan the trip
submit_button = tk.Button(window, text="Plan Trip", font=("Arial", 12), command=plan_trip)
submit_button.pack(pady=10)

# Create a label to display the trip details
result_label = tk.Label(window, text="", font=("Arial", 12), wraplength=400)
result_label.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
