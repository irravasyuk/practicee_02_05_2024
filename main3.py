# Завдання 3
#  Створіть клієнтсько-серверний додаток, де клієнт
# надсилає рядок тексту або слово на сервер для
# перекладу на іншу мову. Сервер повертає переклад і
# відправляє його клієнту. Наприклад, клієнт надсилає
# рядок "Hello, how are you?" на сервер, а сервер повертає
# переклад цього рядка на вказану мову. Скористайтеся
# бібліотекою googletrans.
import socket
from googletrans import Translator

def translate_text(text, dest='en'):
    translator = Translator()
    translation = translator.translate(text, dest=dest)
    return translation.text

def client_connect(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        translation = translate_text(data)
        client_socket.send(translation.encode())

    client_socket.close()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 9999))
    server.listen(1)
    print('Сервер запущений')

    while True:
        client, address = server.accept()
        print(f'Клієнта підключено: {address}')
        client_connect(client)