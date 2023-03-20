from Cryptodome.Cipher import AES
from Cryptodome import Random
key = b'Sixteen byte key'
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)
msg = iv + cipher.encrypt(b'Attack at dawn')
encoded = msg.encode('hex')
print(encoded)
