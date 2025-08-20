import secrets
import string
import tkinter as tk
import math

#All character pools
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

#Password generation
def generate_password(Flength, allow_lowercase, allow_uppercase, allow_digits, allow_symbols):
    pools=[]

    if allow_lowercase:
        pools.append(lowercase)
    if allow_uppercase:
        pools.append(uppercase)
    if allow_digits:
        pools.append(digits)
    if allow_symbols:
        pools.append(symbols)

    if not pools:
        raise ValueError("No character sets selected!")

    if Flength < len(pools):
        raise ValueError(f"Password length must be at least {len(pools)} to include all selected character types")

    #Ensure at least 1 of each character is present
    password_chars = []
    for pool in pools:
        password_chars.append(secrets.choice(pool))

    #Then, choose characters randomly from all the pools
    all_chars = "".join(pools)
    for _ in range(Flength - len(pools)):
        password_chars.append(secrets.choice(all_chars))

    secrets.SystemRandom().shuffle(password_chars)
    password = "".join(password_chars)

    calculate_entropy(Flength, len(all_chars))

    textboxPassword.insert(tk.END, password)

#Calculates entropy (password unpredictability)
def calculate_entropy(Flength, pool_size):
    textboxEntropy.delete(1.0, tk.END)
    textboxEntropy.insert(tk.END, int(Flength * math.log2(pool_size)))


def on_generate():
    textboxPassword.delete("1.0", tk.END)  # Clear old text
    try:
        generate_password(length.get(), allowLowercase.get(), allowUppercase.get(), allowDigits.get(), allowSymbols.get())
    except Exception as e:
        textboxPassword.insert(tk.END, f"Error: {e}")

root = tk.Tk()

#Checkbox variables
allowLowercase = tk.BooleanVar(value=True)
allowUppercase = tk.BooleanVar(value=True)
allowDigits = tk.BooleanVar(value=True)
allowSymbols = tk.BooleanVar(value=True)
length = tk.IntVar(value=16)

#Window config
root.geometry("400x500")
root.title("Password Generator by nedra23")
root.configure(bg="#303030")

#Title
labelTitle = tk.Label(root, text="Choose password options:", font=("", 18), bg="#303030", fg="white")
labelTitle.pack(pady=10)

#Length label
labelLength = tk.Label(root, text="Length:", font=("", 14), bg="#303030", fg="white")
labelLength.pack()

#Password length
inputLength = tk.Entry(root, font=("", 11), bg="#303030", fg="white", width=10, textvariable=length)
inputLength.pack(pady=10)

#Checkboxes
boxFrame = tk.Frame(root, bg="#303030")
boxFrame.columnconfigure(0, weight=1)
boxFrame.columnconfigure(1, weight=1)
boxFrame.columnconfigure(2, weight=1)
boxFrame.columnconfigure(3, weight=1)

box1 = tk.Checkbutton(boxFrame, text="Lowercase", variable=allowLowercase, onvalue=True, offvalue=False)
box1.config(bg="#303030", fg="white", font=("", 11), selectcolor="#303030")

box2 = tk.Checkbutton(boxFrame, text="Uppercase", variable=allowUppercase, onvalue=True, offvalue=False)
box2.config(bg="#303030", fg="white", font=("", 11), selectcolor="#303030")

box3 = tk.Checkbutton(boxFrame, text="Numbers", variable=allowDigits, onvalue=True, offvalue=False)
box3.config(bg="#303030", fg="white", font=("", 11), selectcolor="#303030")

box4 = tk.Checkbutton(boxFrame, text="Special Characters", variable=allowSymbols, onvalue=True, offvalue=False)
box4.config(bg="#303030", fg="white", font=("", 11), selectcolor="#303030")

box1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
box2.grid(row=0, column=1, padx=10, pady=5, sticky="w")
box3.grid(row=1, column=0, padx=10, pady=5, sticky="w")
box4.grid(row=1, column=1, padx=10, pady=5, sticky="w")

boxFrame.pack()

#Generate password button
buttonGenerate = tk.Button(root, text="Generate", font=("", 18), bg="green", fg="white",
                           command=on_generate)
buttonGenerate.pack(pady=20)

#Password output field
textboxPassword = tk.Text(root, height=5, font=("", 11))
textboxPassword.pack(padx=20, pady=20)

#Entropy label
labelLength = tk.Label(root, text="Entropy:", font=("", 14), bg="#303030", fg="white")
labelLength.pack()

#Entropy output field
textboxEntropy = tk.Text(root, height=1, width=3, font=("", 11))
textboxEntropy.pack(pady=10)

root.mainloop()