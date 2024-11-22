import tkinter as tk
from tkinter import messagebox


def calculate_carbon_footprint():
    try:
        electricity_usage = float(electricity_entry.get())
        natural_gas_usage = float(natural_gas_entry.get())
        gasoline_usage = float(gasoline_entry.get())

        electricity_emissions = electricity_usage * 0.5
        natural_gas_emissions = natural_gas_usage * 2.3
        gasoline_emissions = gasoline_usage * 2.31

        total_emissions = electricity_emissions + natural_gas_emissions + gasoline_emissions

        result_text = f"Your carbon footprint for this month:\n"
        result_text += f"Electricity emissions: {electricity_emissions:.2f} kg CO2e\n"
        result_text += f"Natural gas emissions: {natural_gas_emissions:.2f} kg CO2e\n"
        result_text += f"Gasoline emissions: {gasoline_emissions:.2f} kg CO2e\n"
        result_text += f"Total emissions: {total_emissions:.2f} kg CO2e"

        result_label.config(text=result_text)

        suggest_ways_to_reduce(total_emissions)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for electricity, natural gas, and gasoline.")

def suggest_ways_to_reduce(emissions):
    suggestion_text = "Suggestions to reduce your carbon footprint:\n"

    if emissions <= 100:
        suggestion_text += "Your carbon footprint is within an acceptable range."
    else:
        if emissions > 100:
            suggestion_text += "- Reduce energy consumption by using energy-efficient appliances and turning off lights when not in use.\n"
        if emissions > 200:
            suggestion_text += "- Opt for renewable energy sources such as solar panels or wind turbines.\n"
        if emissions > 300:
            suggestion_text += "- Use public transportation, carpooling, or cycling instead of driving alone.\n"
        if emissions > 400:
            suggestion_text += "- Minimize air travel and consider video conferencing for meetings.\n"
        if emissions > 500:
            suggestion_text += "- Practice waste reduction, recycling, and composting.\n"

    suggestion_label.config(text=suggestion_text)

# Create the main window
window = tk.Tk()
window.title("Carbon Footprint Calculator")

# Create input labels and entry fields
electricity_label = tk.Label(window, text="Electricity Usage (kWh):")
electricity_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
electricity_entry = tk.Entry(window)
electricity_entry.grid(row=0, column=1, padx=10, pady=5)

natural_gas_label = tk.Label(window, text="Natural Gas Usage (cubic meters):")
natural_gas_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
natural_gas_entry = tk.Entry(window)
natural_gas_entry.grid(row=1, column=1, padx=10, pady=5)

gasoline_label = tk.Label(window, text="Gasoline Usage (liters):")
gasoline_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
gasoline_entry = tk.Entry(window)
gasoline_entry.grid(row=2, column=1, padx=10, pady=5)

# Create the calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_carbon_footprint)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create the result label
result_label = tk.Label(window, text="", justify="left")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Create the suggestion label
suggestion_label = tk.Label(window, text="", justify="left")
suggestion_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="w")

# Start the Tkinter event loop
window.mainloop()
