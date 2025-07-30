# Generates random password
import random
import string
def genPass() -> str:
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits + symbols


    password = ''.join(random.choices(all_chars, k=20))

    return password