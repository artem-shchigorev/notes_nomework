import random
import string

def generate_unique_id(length=5):
    letters_and_digits = string.ascii_letters + string.digits
    unique_id = ''.join(random.choice(letters_and_digits) for _ in range(length))
    return unique_id


