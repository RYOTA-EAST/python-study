import socket
# サーバーを立ち上げる
# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind(('127.0.0.1', 50007))
#     s.listen(1)
#     while True:
#         conn, addr = s.accept()
#         with conn:
#             while True:
#                 data = conn.recv(1024)
#                 if not data:
#                     break
#                 print('data: {}, addr:{}'.format(data, addr))
#                 # 送信されたものに付け加える
#                 conn.sendall(b'Received: '+ data)
# サーバーを立ち上げる
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind(('127.0.0.1', 50007))
    while True:
        data, addr = s.recvfrom(1024)
        # 表示する
        print("data: {}, addr: {}".format(data, addr))