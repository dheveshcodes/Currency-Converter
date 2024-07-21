import tkinter as tk
import pyttsx3
import threading

window = tk.Tk()
window.title("Currency Converter")
window.config(bg="green2")
window.iconbitmap("C:/Users/dheve/Downloads/currency.ico")

conversion_rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "GBP": 0.75,
    "INR": 73.5,
}

currency_symbols = {
    "USD": "$",
    "EUR": "€",
    "GBP": "£",
    "INR": "₹",
}

def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()
        
        amount_in_usd = amount / conversion_rates[from_currency]
        converted_amount = amount_in_usd * conversion_rates[to_currency]
        
        symbol = currency_symbols[to_currency]
        result_text = f"Your available amount is {symbol}{converted_amount:.2f} {to_currency}, Thank you visit again!!!"
        
        result_textbox.delete(1.0, tk.END)
        result_textbox.insert(tk.END, result_text)
        
        threading.Thread(target=speak_text, args=(result_text,)).start()
        
    except ValueError:
        result_textbox.delete(1.0, tk.END)
        result_textbox.insert(tk.END, "Please enter a valid number for the amount.")
    except KeyError:
        result_textbox.delete(1.0, tk.END)
        result_textbox.insert(tk.END, "Please select valid currencies.")

def speak_text(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    
    engine.setProperty('voice', voices[1].id)
    
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def backspace():
    current_text = amount_entry.get()
    if current_text:
        amount_entry.delete(len(current_text) - 1, tk.END)


label1 = tk.Label(window, text="Currency Converter", bg="gold", font=("Times New Roman", 16))
label1.grid(row=0, column=0, columnspan=3, pady=10)

amount_label = tk.Label(window, text="Amount:", bg="turquoise1")
amount_label.grid(row=1, column=0, padx=30, pady=25)
amount_entry = tk.Entry(window)
amount_entry.grid(row=1, column=1, padx=40, pady=40, sticky="ew")

backspace_button = tk.Button(window, text="←", command=backspace, bg="cyan")
backspace_button.grid(row=1, column=2, padx=30, pady=10, sticky="w")

from_currency_label = tk.Label(window, text="From Currency:", bg="aquamarine2")
from_currency_label.grid(row=2, column=0, padx=10, pady=10)
from_currency_var = tk.StringVar(window)
from_currency_var.set("USD")
from_currency_menu = tk.OptionMenu(window, from_currency_var, *conversion_rates.keys())
from_currency_menu.grid(row=2, column=1, columnspan=2, padx=40, pady=40, sticky="ew")

to_currency_label = tk.Label(window, text="To Currency:", bg="aquamarine2")
to_currency_label.grid(row=3, column=0, padx=10, pady=10)
to_currency_var = tk.StringVar(window)
to_currency_var.set("EUR")
to_currency_menu = tk.OptionMenu(window, to_currency_var, *conversion_rates.keys())
to_currency_menu.grid(row=3, column=1, columnspan=2, padx=40, pady=40, sticky="ew")

convert_button = tk.Button(window, text="Convert", command=convert_currency, bg="OrangeRed2")
convert_button.grid(row=4, column=0, columnspan=3, pady=20)

result_label = tk.Label(window, text="Your Amount:", bg="peach puff")
result_label.grid(row=5, column=0, columnspan=3, pady=5)
result_textbox = tk.Text(window, height=5, width=60, bg = "deep sky blue")
result_textbox.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
