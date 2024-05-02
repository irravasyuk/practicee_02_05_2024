# Завдання 1
# Реалізуйте клієнт-серверний додаток з можливістю
# зворотного обміну повідомленнями. Для початку спілкування
# встановіть з’єднання. Після з’єднання використайте текстовий
# формат. У бесіді беруть участь лише дві
# особи. Після завершення спілкування сервер переходить
# до очікування нового учасника розмови.
##Server
import socket

server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM
                       )
server.bind(('127.0.0.1', 8080))
server.listen(1)

while True:
    print('Waiting ...')

    client, address = server.accept()
    print(f"Клієнта підключено: {address}")

    while True:
        data = client.recv(1024).decode()
        print(data)

        if data == 'exit':
            break

        print('Клієнт:', data)

        response = input('Відповідь сервера:')
        client.send(response.encode())

    client.close()
    print("Звя'язок перервано.")







