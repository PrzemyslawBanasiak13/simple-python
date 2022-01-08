
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    password_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(4, 8)
    nr_symbols = random.randint(2, 6)
    nr_numbers = random.randint(2, 6)
    nr_chars = nr_numbers + nr_letters + nr_symbols

    password = ""

    for letter in range(0, nr_chars):
        password += letters[random.randint(0, len(letters) - 1)]

    for number in range(0, nr_numbers):
        password += numbers[random.randint(0, len(numbers) - 1)]

    for symbol in range(0, nr_symbols):
        password += symbols[random.randint(0, len(symbols) - 1)]

    password = list(password)
    random.shuffle(password)
    password = "".join(password)

    pyperclip.copy(password)
    password_input.insert(0, password)

# ---------------------------- LOOK FOR PASSWORD ------------------------------- #


def search():
    website = website_input.get()
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            if website in data:
                username = data[website]["username"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"username: {username}\nPassword: {password}")
            else:
                messagebox.showinfo(title=website, message="Not found")

    except (FileNotFoundError, ValueError):
        messagebox.showinfo(title=website, message="Not found")

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if website == "" or username == "" or password == "":
        messagebox.showerror(message="Don't leave any blank boxes!")
    else:
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)

        except (FileNotFoundError, ValueError):
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)

        website_input.delete(0, END)
        username_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

logo = Canvas(width=200, height=200, highlightthickness=0)
logo_png = PhotoImage(file="logo.png")
logo.create_image(100, 100, image=logo_png)
logo.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_input = Entry(width=35)
website_input.grid(column=1, row=1)
website_input.focus()
website_search_button = Button(width=15, text="Search existing", command=search)
website_search_button.grid(column=2, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_input = Entry(width=54)
username_input.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_input = Entry(width=35)
password_input.grid(column=1, row=3)
password_button = Button(width=15, text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(width=40, text="Add", command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
