import random

def simulate_tcp_cwnd(transmissions=20, success_prob=0.8):
    cwnd = 1  # Ventana de congestión inicial
    
    for i in range(1, transmissions + 1):
        if random.random() < success_prob:
            cwnd += 1  # Aumenta la ventana en caso de éxito
            print(f"Transmisión {i}: Éxito - cwnd = {cwnd}")
        else:
            cwnd = 1  # Reinicio a Slow Start en caso de pérdida
            print(f"Transmisión {i}: Pérdida - cwnd = {cwnd}")

# Ejecutar la simulación
simulate_tcp_cwnd()