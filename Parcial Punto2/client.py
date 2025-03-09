import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect(('127.0.0.1', 2010))
        print("Conectado al servidor en localhost:2010")
        
        message = input('Ingrese el mensaje a enviar: ')
        print(f"Enviando mensaje: {message}")
        client.sendall(message.encode('utf-8'))
        
        response = client.recv(1024).decode('utf-8')
        if response:
            print(f"Respuesta del servidor: {response}")
        else:
            print("No se recibió respuesta del servidor.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    start_client()
