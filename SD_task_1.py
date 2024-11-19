import tkinter as tk
from tkinter import ttk, messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))

def kelvin_to_fahrenheit(kelvin):
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))

def convert_temperature():
    try:
        temp_value = float(entry_temp.get())
        conversion = combo_conversion.get()

        if conversion == "Celsius to Fahrenheit":
            result = celsius_to_fahrenheit(temp_value)
            result_label.config(text=f"{temp_value}°C = {result:.2f}°F")
        elif conversion == "Fahrenheit to Celsius":
            result = fahrenheit_to_celsius(temp_value)
            result_label.config(text=f"{temp_value}°F = {result:.2f}°C")
        elif conversion == "Celsius to Kelvin":
            result = celsius_to_kelvin(temp_value)
            result_label.config(text=f"{temp_value}°C = {result:.2f} K")
        elif conversion == "Kelvin to Celsius":
            result = kelvin_to_celsius(temp_value)
            result_label.config(text=f"{temp_value} K = {result:.2f}°C")
        elif conversion == "Fahrenheit to Kelvin":
            result = fahrenheit_to_kelvin(temp_value)
            result_label.config(text=f"{temp_value}°F = {result:.2f} K")
        elif conversion == "Kelvin to Fahrenheit":
            result = kelvin_to_fahrenheit(temp_value)
            result_label.config(text=f"{temp_value} K = {result:.2f}°F")
        else:
            messagebox.showerror("Error", "Please select a valid conversion type.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a numeric value for the temperature.")

# GUI Setup
root = tk.Tk()
root.title("Temperature Converter")

# Input
frame_input = ttk.Frame(root, padding=10)
frame_input.grid(row=0, column=0, columnspan=2, pady=10)

ttk.Label(frame_input, text="Enter Temperature:").grid(row=0, column=0, padx=5, sticky="w")
entry_temp = ttk.Entry(frame_input, width=20)
entry_temp.grid(row=0, column=1, padx=5)

# Conversion Options
frame_options = ttk.Frame(root, padding=10)
frame_options.grid(row=1, column=0, columnspan=2, pady=10)

ttk.Label(frame_options, text="Conversion Type:").grid(row=0, column=0, padx=5, sticky="w")
combo_conversion = ttk.Combobox(frame_options, state="readonly", width=30)
combo_conversion["values"] = [
    "Celsius to Fahrenheit",
    "Fahrenheit to Celsius",
    "Celsius to Kelvin",
    "Kelvin to Celsius",
    "Fahrenheit to Kelvin",
    "Kelvin to Fahrenheit"
]
combo_conversion.grid(row=0, column=1, padx=5)
combo_conversion.current(0)

# Buttons
frame_buttons = ttk.Frame(root, padding=10)
frame_buttons.grid(row=2, column=0, columnspan=2)

convert_button = ttk.Button(frame_buttons, text="Convert", command=convert_temperature)
convert_button.grid(row=0, column=0, padx=5)

exit_button = ttk.Button(frame_buttons, text="Exit", command=root.quit)
exit_button.grid(row=0, column=1, padx=5)

# Result
frame_result = ttk.Frame(root, padding=10)
frame_result.grid(row=3, column=0, columnspan=2)

result_label = ttk.Label(frame_result, text="Result will be displayed here", font=("Arial", 12, "bold"))
result_label.grid(row=0, column=0)

# Run the application
root.mainloop()
