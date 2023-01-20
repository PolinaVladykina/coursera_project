import socket
import time
from collections import defaultdict
from select import select

tasks = []

to_read = {}
to_write = {}

class ClientError(Exception):
    pass

def recv_all(sock):
    BUFF_SIZE = 4096 # 4 KiB
    data = b''
    while True:
        part = sock.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break
    return data

def get_a_dict(response):
    number_of_string = response.split("\n")
    answer = [sub_string.split(" ") for sub_string in number_of_string]
    keys = []
    values = []
    for string in answer:
        if string != answer[0] and string != answer[-1]:
            keys.append(string[0])
            values.append((float(string[1]), int(string[2])))
    # keys = [string[0] for string in answer if string != answer[0] and string != answer[-1]]
    # values = ((string[1], string[2]) for string in answer if string != answer[0] and string != answer[-1])
    d = defaultdict(list)
    r = zip(keys, values)

    for k, v in r:
        d[k].append(v)
    #
    # answer = answer[1:-1]
    # d = defaultdict(list)
    # for metric_name, metric_value, timestamp in answer:
    #     d[metric_name].append((metric_value, timestamp))
    return d


class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        try:
            self.socket = socket.create_connection((self.host, self.port), self.timeout)

        except socket.error as err:
            raise ClientError(err)

    def get(self, key):
        try:
            self.socket.send(f"get {key}\n".encode())
            response = recv_all(self.socket).decode("utf-8")
            if 'ok\n' not in response:
                raise ClientError
            if response == "ok\n\n":
                dictionary = {}
            else:
                dictionary = get_a_dict(response)

        except Exception as err:
            raise ClientError(err)

        return dictionary


    def put(self, key, value, timestamp=None):
        if key == 'quit':
            self.socket.send(f"{key} {value} {timestamp}\n".encode())
            response = self.socket.recv(1024).decode("utf-8")
        else:
            try:
                if timestamp == None:
                    timestamp = int(time.time())
                self.socket.send(f"{key} {value} {timestamp}\n".encode())
                response = self.socket.recv(1024).decode("utf-8")
                if 'ok\n' not in response:
                    raise ClientError

            except Exception as err:
                raise ClientError(err)


def main():
    client = Client("127.0.0.1", 8888, timeout=15)
    # client.put("palm.cpu", 0.5, timestamp=1150864247)
    # client.put("palm.cpu", 2.0, timestamp=1150864248)
    # client.put("palm.cpu", 0.5, timestamp=1150864248)
    # client.put("eardrum.cpu", 3, timestamp=1150864250)
    # client.put("eardrum.cpu", 4, timestamp=1150864251)
    # client.put("eardrum.memory", 4200000)
    print(len(client.get('*')['palm.cpu']))
    # print(client.get("coma"))
    # client.put("quit",0)

if __name__ == "__main__":
    main()

   # python C:\Users\flora\PycharmProjects\pythonProject\solution_10.py