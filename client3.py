import socket

def send_text_to_server(text):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9999))
    client.send(text.encode())
    translation = client.recv(1024).decode()
    client.close()
    return translation

text = input("Введіть рядок для перекладу: ")
translated_text = send_text_to_server(text)
print("Переклад:", translated_text)