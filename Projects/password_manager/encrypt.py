import random, base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class Encrypt:
    password: str = ''
    salt: bytes = ''

    def __init__(this, password: str, salt: str):
        this.password = bytes(password, 'utf-8')
        this.salt = bytes(salt, 'utf-8')

    def generate_salt(length = 16):
        return Encrypt.get_random_string(length)

    def get_random_string(number_characters):
        newString = ''
        while len(newString) < number_characters:
            newString += Encrypt.get_random_character()
        return newString

    def get_random_character():
        characters = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + '0123456789'
        return random.choice(characters)

    def encrypt(this, string: str):
        kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=this.salt,
        iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(this.password))
        f = Fernet(key)
        string_as_bytes = bytes(string, 'utf-8')
        encrypted = f.encrypt(string_as_bytes)
        return encrypted

    def decrypt(this, string):
        kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=this.salt,
        iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(this.password))
        f = Fernet(key)
        string_as_bytes = bytes(string, 'utf-8')
        unencrypted = f.decrypt(string_as_bytes).decode()
        return unencrypted




# Example usage
'''
salt = Encrypt.generate_salt()
encryption = Encrypt('password', salt)

message = "Best Buy,leo,password_new,www.bestbuy.com,movies are overpriced here"
encrypted = encryption.encrypt(message)
print(encrypted)

stored_salt = "jiGJEZOhclGghqfu"
stored_encrypted_string = "gAAAAABj2cplQsW9JjZTaKgj7nuf0U4RT9dAA34K6hjsGyUK6pcpX2bBGYEIBHqhcUTZVukMLeEFgQU7zKY2HaBd4-YdBUJEb5KDpW2NjDOgUiFUAXh5CiDwPJvVz8397lvxHkYtYOEbIcgKYpg0efjMgf1mbHz58NaAsBtZFtRMF9ebmkbh1uc="
enc = Encrypt('mypass', stored_salt)
unencrypted = enc.decrypt(stored_encrypted_string)
print(unencrypted)
'''




