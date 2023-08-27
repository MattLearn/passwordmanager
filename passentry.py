import random
import string

# basic file I/O was used pandas might be a better alternative as it gets larger
def store_credentials(website, username, password):
    with open("stores.txt", "a") as passfile:
        passfile.write(f"{website}|{username}|{password}\n")


def generate_pass():
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_string = ''.join(random.choices(characters, k=12))
    return generated_string

