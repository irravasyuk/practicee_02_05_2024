# Завдання 2
# Реалізуйте клієнт-серверний додаток погоди. Клієнт
# звертається до сервера із зазначенням країни та міста.
# Сервер, отримавши запит, видає погоду на тиждень для
# вказаної місцевості. Використовуйте для реалізації додатку
# багатопотокові механізми. Дані про погоду мають
# бути наперед визначеними та взяті з файлу.
import socket
import threading
import json

def load_weather():
    with open('weather_data.json', 'r') as file:
        return json.load(file)

def client_connect(client_socket, address, weather_data):
    print(f'Клієнта  підключено: {address}')

    while True:
        request = client_socket.recv(1024).decode()
        if not request:
            break

        if request in weather_data:
            response = weather_data[request]
        else:
            response = 'Таких даних про погоду немає'

        client_socket.send(response.encode())

    client_socket.close()
    print(f"Зв'язок перервано з: {address}")

weather_data = load_weather()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8888))
server.listen(2)
print('Сервер запущений')

while True:
    client, address = server.accept()
    connect_client = threading.Thread(target=client_connect, args=(client, address, weather_data))
    connect_client.start()

