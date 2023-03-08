import hashlib

class Hash:
    def hash(text, salt):
        salted = text + salt
        hashed = hashlib.md5(salted.encode())
        return hashed.hexdigest()

# hashed = Hash.hash("ThisHouseIsOnFire", "salt")
# print(hashed)
