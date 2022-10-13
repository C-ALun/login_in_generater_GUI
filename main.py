import json
from tkinter import *
from tkinter import messagebox
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import choice, randint, shuffle
def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_data = website_entry.get()
    user_name_data = user_name_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            'email': user_name_data,
            'password': password_data,
        },
    }


    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title='Oops', message=f"Please make sure you haven't left any fields empty.")
    else:
        try:
            with open('data.json', 'r') as file:

                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open('data.json', 'w') as file:
                #Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
def find_password():
    website = website_entry.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found.')
    else:
        if website in data:
            website_data = data[website]
            password = website_data['password']
            email = website_data['email']
            messagebox.showinfo(title='Result', message=f'Email: {email} \nPassword: {password}\n')
        else:
            messagebox.showinfo(title='Error', message='No details for the website exists.')

    # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)


#Label
website = Label(text='Website:')
website.grid(row=1, column=0)

user_name = Label(text='Email/Username:')
user_name.grid(row=2, column=0)

password = Label(text='Password:')
password.grid(row=3, column=0)
#Buttons

search_button = Button(width=14, text='Search', command=find_password)
search_button.grid(row=1, column=2)

password_generate = Button(text='Generate Password', command=generate_password)
password_generate.grid(row=3, column=2)

generate = Button(text='Add', width=36, command=save)
generate.grid(row=4, column=1, columnspan=2)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

user_name_entry = Entry(width=35)
user_name_entry.grid(row=2, column=1, columnspan=2)
user_name_entry.insert(0, 'abc2123@gmail.com')

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

window.mainloop()