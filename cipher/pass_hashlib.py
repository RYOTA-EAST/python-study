import base64
import hashlib
import os

print(hashlib.sha256(b'test').hexdigest())
print(hashlib.sha256(b'test').hexdigest())

user_name = 'user1'
user_pass = 'password'
db = {}

# パスワードに追加するワードを作る
salt = base64.b64encode(os.urandom(32))


# def get_digest(password):
#     password = bytes(password, 'utf-8')
#     # パスワードに追加する
#     digest = hashlib.sha256(salt + password).hexdigest()
#     # 暗号化したものを暗号化を繰り返す
#     for _ in range(10000):
#         digest = hashlib.sha256(bytes(digest, 'utf-8')).hexdigest()
#         print(digest)
#     print(digest)
#     return digest

# db[user_name] = get_digest(user_pass)


# 上と同じ（パスワーとにsaltを追加、10000回暗号化を繰り返す）
digest = hashlib.pbkdf2_hmac(
    'sha256', bytes(user_pass, 'utf-8'), salt, 10000)

db[user_name] = digest


# def is_login(user_name, password):
#     return get_digest(password) == db[user_name]


def is_login(user_name, password):
    digest = hashlib.pbkdf2_hmac(
        'sha256', bytes(password, 'utf-8'), salt, 10000)
    return digest == db[user_name]


print(is_login(user_name, user_pass))
