import random
import string

def generate_password(length):

    characters = string.ascii_letters + string.digits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = 12


new_password = generate_password(password_length)
print(" YOUR NEW :D Generated password:", new_password)
