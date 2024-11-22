from tkinter import *
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from tkinter import messagebox
import re
import datetime

current_time = datetime.datetime.now()
Time = current_time.strftime('%H:%M:%S')
current_date = datetime.date.today()
Date = current_date.strftime('%Y-%m-%d')

# Define the function to retrieve phone number information
def get_phone_info():

    phone = phone_number_entry.get()

    number = phone
    if not number.isdigit() or len(number) != 10:
        messagebox.showerror("Invalid Phone Number Or Invalid country code", "Please enter a valid 10-digit phone number or a valid country code.")
    else:
        # Get the phone number from the user
        country_code = selected_country_code.get()
        numbers_only = re.findall(r'\d+', country_code)
        counrty_code_numbers_only = (", ".join(numbers_only))
        phone_number = f"+{counrty_code_numbers_only} {phone_number_entry.get()}"
        phone_number_parsed = phonenumbers.parse(phone_number, None)


    # Get the phone number details
    location = geocoder.description_for_number(phone_number_parsed, "en")
    carrier_name = carrier.name_for_number(phone_number_parsed, "en")
    time_zone = timezone.time_zones_for_number(phone_number_parsed)

    # Format the output
    output_text1 = phone_number
    output_text2 = location
    output_text3 =  carrier_name
    output_text4 = time_zone[0] if time_zone else 'Unknown'
    y = ('''

         ''')

    FileLog = open("C:\\Users\\NEW\\OneDrive\\Documents\\Ai\\Template for AI\\Jarvis\\\DataBase\\phone_log.txt", "r")
    phone_log_template = FileLog.read()
    FileLog.close()
    phone_log_template_update = phone_log_template + f"\nTime : {Time} \nDate : {Date} \nPhone Number : {phone_number} \nLocation : {location} \nCarrier : {carrier_name} \nTimeZone : {output_text4}\n {y}"

    # Write the updated phone log back to the file
    FileLog = open("C:\\Users\\NEW\\OneDrive\\Documents\\Ai\\Template for AI\\Jarvis\\\DataBase\\phone_log.txt", "w")
    FileLog.write(phone_log_template_update)
    FileLog.close()



    # Output the information to the GUI
    phone_number_entry1.delete(0, END)
    phone_number_entry1.insert(0, output_text1)
    phone_number_entry2.delete(0, END)
    phone_number_entry2.insert(0, output_text2)
    phone_number_entry3.delete(0, END)
    phone_number_entry3.insert(0, output_text3)
    phone_number_entry4.delete(0, END)
    phone_number_entry4.insert(0, output_text4)


# Create the main window
root = Tk()
root.title("Phone Number Lookup")
root.geometry('330x305+600+200')

# Create the phone number entry field and label
large_font = ('Arial', 10)
phone_number_label = Label(root, text="Enter a phone number:")
phone_number_label.grid(row=1, column=0, padx=10, pady=10)
phone_number_entry = Entry(root)
phone_number_entry.grid(row=1, column=1, padx=10, pady=10)

# Create the label to select the country code
country_code_label = Label(root, text="Select country code:")
country_code_label.grid(row=0, column=0, padx=10, pady=10)

# Define the country code options
country_codes = [
    '+1     USA',
'+44    UK',
'+86    China',
'+91    India',
'+81    Japan',
'+33    France',
'+49    Germany',
'+7     Russia',
'+55    Brazil',
'+39    Italy',
'+81    South Korea',
'+234   Nigeria',
'+54    Argentina',
'+57    Colombia',
'+20    Egypt',
'+98    Iran',
'+60    Malaysia',
'+63    Philippines',
'+966   Saudi Arabia',
'+65    Singapore',
'+27    South Africa',
'+90    Turkey',
'+380   Ukraine',
'+971   United Arab Emirates',
'+598   Uruguay',
'+998   Uzbekistan',
'+58    Venezuela',
'+84    Vietnam']

# Create the variable to hold the selected country code
selected_country_code = StringVar(root)
selected_country_code.set(country_codes[0]) # set default value

# Create the option menu for the country code
country_code_option_menu = OptionMenu(root, selected_country_code, *country_codes)
country_code_option_menu.grid(row=0, column=1, padx=10, pady=10)

phone_number_label1 = Label(root, text="Phone Number -->")
phone_number_label1.grid(row=3, column=0, padx=10, pady=10)
phone_number_entry1 = Entry(root)
phone_number_entry1.grid(row=3, column=1, padx=10, pady=10)

phone_number_label2 = Label(root, text="Location     -->")
phone_number_label2.grid(row=4, column=0, padx=10, pady=10)
phone_number_entry2 = Entry(root)
phone_number_entry2.grid(row=4, column=1, padx=10, pady=10)

phone_number_label3 = Label(root, text="Carrier      -->")
phone_number_label3.grid(row=5, column=0, padx=10, pady=10)
phone_number_entry3 = Entry(root)
phone_number_entry3.grid(row=5, column=1, padx=10, pady=10)

phone_number_label4 = Label(root, text="Time Zone    -->")
phone_number_label4.grid(row=6, column=0, padx=10, pady=10)
phone_number_entry4 = Entry(root)
phone_number_entry4.grid(row=6, column=1, padx=10, pady=10)

# Create the button to get the phone number information
get_info_button = Button(root, text="Get Info", command=get_phone_info)
get_info_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)



# Run the main loop
root.mainloop()