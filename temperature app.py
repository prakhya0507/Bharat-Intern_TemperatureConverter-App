import tkinter as tk

def convert_temperature():
    try:
        temperature = float(entry.get())
        from_unit = from_var.get()
        to_unit = to_var.get()

        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (temperature * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (temperature - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = temperature + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = temperature - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (temperature + 459.67) * 5/9
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (temperature * 9/5) - 459.67
        else:
            result = temperature

        result_label.config(text=f"Result: {result:.2f} {to_unit}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

app = tk.Tk()
app.title("Temperature Converter")

from_var = tk.StringVar()
from_var.set("Celsius")
to_var = tk.StringVar()
to_var.set("Fahrenheit")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

frame.grid(column=0, row=0)

entry_label = tk.Label(frame, text="Enter Temperature:")
entry_label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=1)

from_label = tk.Label(frame, text="From:")
from_label.grid(row=1, column=0)

from_menu = tk.OptionMenu(frame, from_var, "Celsius", "Fahrenheit", "Kelvin")
from_menu.grid(row=1, column=1)

to_label = tk.Label(frame, text="To:")
to_label.grid(row=2, column=0)

to_menu = tk.OptionMenu(frame, to_var, "Celsius", "Fahrenheit", "Kelvin")
to_menu.grid(row=2, column=1)

convert_button = tk.Button(frame, text="Convert", command=convert_temperature)
convert_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(frame, text="Result: ")
result_label.grid(row=4, column=0, columnspan=2)

app.mainloop()
