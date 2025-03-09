import socket
import threading

def handle_client(client_socket, address):
    print(f"Conexión aceptada desde {address}")
    
    try:
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Mensaje recibido: {message}")

        # Obtener el nombre del cliente si el mensaje tiene formato esperado
        words = message.split()
        client_name = words[-1] if len(words) > 0 else "Desconocido"

        response = f"Mensaje recibido de {client_name}"
        client_socket.send(response.encode('utf-8'))

        # Imprimir la respuesta enviada en el servidor
        print(f"Respuesta enviada: Mensaje recibido de {client_name}")

    except Exception as e:
        print(f"Error con el cliente {address}: {e}")
    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 2010))
    server.listen(5)
    print("Servidor escuchando en el puerto 2010...")
    
    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))
        client_handler.start()

if __name__ == "__main__":
    start_server()
