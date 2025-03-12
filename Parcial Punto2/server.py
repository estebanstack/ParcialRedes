import socket
import threading

def handle_client(client_socket, address):
    print(f"Conexión aceptada desde {address}")
    
    try:
        # Recibe un mensaje del cliente (hasta 1024 bytes) y lo decodifica de UTF-8 a string.
        message = client_socket.recv(1024).decode('utf-8')

        # Obtener el nombre del cliente si el mensaje tiene formato esperado
        print(f"Mensaje recibido: {message}")
       
        # Divide el mensaje en palabras usando espacios como separadores.       
        words = message.split()
        
        # Toma la última palabra como el nombre del cliente. Si el mensaje está vacío, usa "Desconocido".
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
    server.listen(5) #-> configura el servidor para escuchar conexiones de hasta 5 clientes (MODIFICABLE)
    print("Servidor escuchando en el puerto 2010...")
    
    while True: #-> Bucle infinito para aceptar múltiples clientes.

        # Espera una conexión entrante y la acepta cuando ocurre.  
        # Devuelve un nuevo socket para comunicarse con el cliente y su dirección.
        client_socket, addr = server.accept()  
        
        # Crea un nuevo hilo para manejar la comunicación con el cliente sin bloquear el servidor.
        client_handler = threading.Thread(target=handle_client, args=(client_socket, addr))  
        
        # Inicia el hilo para manejar la conexión con el cliente.
        client_handler.start()  

if __name__ == "__main__":
    start_server()
