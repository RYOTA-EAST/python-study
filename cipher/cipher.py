import string
import random

from Crypto.Cipher import AES

key = ''.join(random.choice(string.ascii_letters) for _ in range(AES.block_size))
iv = ''.join(random.choice(string.ascii_letters) for _ in range(AES.block_size))

# 暗号化
with open('plane.txt', 'r') as f, open('enc.dat', 'wb') as e:
    plaintext = f.read()
    # plaintext = 'jdhagheghjkashfjkalhfaohgioahgioa'
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 区切る文字数間隔からズレている数を算出
    padding_length = AES.block_size - len(plaintext) % AES.block_size
    # その文字数分の文字を付け加える
    plaintext += chr(padding_length) * padding_length
    # 暗号化
    cipher_text = cipher.encrypt(plaintext)
    e.write(cipher_text)

# 復元
with open('enc.dat', 'rb') as f:
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    decrypted_text = cipher2.decrypt(f.read())
    print(decrypted_text[:-decrypted_text[-1]].decode('utf-8'))
