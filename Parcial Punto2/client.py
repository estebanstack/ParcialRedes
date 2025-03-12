import socket

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #-> crea el socket
    try:
        client.connect(('127.0.0.1', 2010))
        print("Conectado al servidor en localhost:2010")
        
        message = input('Ingrese el mensaje a enviar: ')
        print(f"Enviando mensaje: {message}")
        client.sendall(message.encode('utf-8')) #->  Convierte el mensaje en bytes usando codificación UTF-8 y lo envía al servidor.
        # sendall solo recibe bytes
        
        # Espera recibir una respuesta del servidor (hasta 1024 bytes) y la decodifica de UTF-8 a string.
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
