




import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 8888))
sock.listen(2)
conn, addr = sock.accept()

print('Соединение установлено:', addr)

# переменная response хранит строку возвращаемую сервером, если вам для
# тестирования клиента необходим другой ответ, измените ее
# response = b'ok\npalm.cpu 10.5 1501864247\npalm.cpu 13.4 1501864237\neardrum.cpu 15.3 1501864259\n\n'
tmp = '\n'
response = f"ok\n{tmp.join(['palm.cpu 10.5 1501864247' for i in range(1000)])}\n".encode()

while True:
    data = conn.recv(1024)
    if not data:
        print("error\nwrong command\n\n")
        break
    if 'quit' in data.decode("utf-8"):
        print(f'Получен запрос: quit')
        print("Соединение завершено")
        response = 'done'
        conn.send(response.encode())
        break
    else:
        request = data.decode('utf-8')
        if 'get' not in request:
            response = response.decode("utf-8")
            response = response[:-1] + request + '\n'
            response = response.encode()
            print(f'Получен запрос: {ascii(request)}')
            print(f'Отправлен ответ ok\n\n')
        else:
            response = response.decode("utf-8")
            key = request.replace('get ','').rstrip('\n')
            if "*" not in key:
                new_response = 'ok\n'
                number_of_string = response.split("\n")
                for line in number_of_string:
                    if key in line:
                        new_response = new_response + line + '\n'
                response = new_response.encode()
            else:
                response = response.encode()
            print(f'Получен запрос: {ascii(request)}')
            print(f'Отправлен ответ {ascii(response.decode("utf-8"))}')
        conn.send(response)

conn.close()