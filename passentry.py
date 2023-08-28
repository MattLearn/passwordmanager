import random
import string
import pyperclip
import json


# basic file I/O was used pandas might be a better alternative as it gets larger
def store_credentials(website, username, password):
    json_export ={
        website: {
            "email": username,
            "password": password,
        }
    }
    try:
        with open("stores.json", "r") as pass_file:
            data = json.load(pass_file)
    except FileNotFoundError:
        with open("stores.json", "w") as pass_file:
            json.dump(json_export, pass_file, indent=4)
    else:
        data.update(json_export)

        with open("stores.json", "w") as pass_file:
            json.dump(json_export, pass_file, indent=4)


def retrieve_credentials(website):
    with open("stores.json", "r") as pass_file:
        data = json.load(pass_file)
    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        code = 0
    else:
        code = -1
        email = ""
        password = ""
    return email, password, code


def generate_pass():
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_string = ''.join(random.choices(characters, k=12))
    pyperclip.copy(generated_string)
    return generated_string

