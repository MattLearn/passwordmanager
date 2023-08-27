from tkinter import *
from tkinter import messagebox
import passentry

window = Tk()
window.title("Password Manager")
window.resizable(False, False)
window.config(padx=50, pady=50)


def save():
    passentry.store_credentials(website_entry.get(),
                                login_entry.get(),
                                pass_entry.get())
    website_entry.delete(0, "end")
    login_entry.delete(0, "end")
    pass_entry.delete(0, "end")
    messagebox.showinfo(title="Save status", message="Credentials saved!")

def generate():
    pass_entry.delete(0, "end")
    pass_entry.insert(0, passentry.generate_pass())


# This frame was for potentially adding this to a multiscreen application in the future
passmngr_frame = Frame()
passmngr_frame.grid(column=0, row=0)

logo_canvas = Canvas(passmngr_frame)
logo_image = PhotoImage(file="logo.png")
logo_canvas.create_image(200, 150, image=logo_image)
logo_canvas.grid(column=0, row=0, columnspan=3)

# Website name
login_canvas = Frame(passmngr_frame)
login_canvas.grid(column=0, row=1, columnspan=3)
website_lbl = Label(login_canvas, text="Website:")
website_lbl.grid(column=0, row=1, sticky="E")
website_entry = Entry(login_canvas, width=52)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="W", columnspan=2)

# url
url_lbl = Label(login_canvas, text="URL:")
url_lbl.grid(column=0, row=2, sticky="E")
url_entry = Entry(login_canvas, width=52)
url_entry.grid(column=1, row=2, sticky="W", columnspan=2)

# login
login_lbl = Label(login_canvas, text="User/Email:")
login_lbl.grid(column=0, row=3, sticky="E")
login_entry = Entry(login_canvas, width=52)
login_entry.grid(column=1, row=3, sticky="W", columnspan=2)

# password
pass_lbl = Label(login_canvas, text="Password:")
pass_lbl.grid(column=0, row=4, sticky="E")
pass_entry = Entry(login_canvas, width=33)
pass_entry.grid(column=1, row=4, sticky="W")
pass_gen = Button(login_canvas, text="Generate Password", command=generate)
pass_gen.grid(column=2, row=4, sticky="EW")

# button frame
save_btn = Button(login_canvas, text="Save", width=44, command=save)
save_btn.grid(column=1, row=5, columnspan=2, sticky="W")

window.mainloop()
