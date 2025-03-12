import numpy as np
import matplotlib.pyplot as plt

# Parámetros
fs = 10000        # Frecuencia de muestreo en Hz
T_total = 1       # Duración total de la señal (segundos)
t = np.linspace(0, T_total, int(fs*T_total), endpoint=False)

# Definición de la señal x(t)
x = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t) + 0.8*np.sin(2*np.pi*200*t)

# --- Gráfica en el dominio del tiempo ---
plt.figure(figsize=(10, 4))
plt.plot(t[:500], x[:500], label='x(t)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal en el dominio del tiempo')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Cálculo de la FFT para el dominio de la frecuencia ---
X = np.fft.fft(x)
N = len(x)
freqs = np.fft.fftfreq(N, 1/fs)
mask = freqs >= 0    # Usamos solo el lado positivo
freqs_pos = freqs[mask]
X_pos = X[mask]
magnitude = np.abs(X_pos) / N  # Normalizamos

# --- Gráfica en el dominio de la frecuencia ---
plt.figure(figsize=(10, 4))
plt.stem(freqs_pos, magnitude, use_line_collection=True)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.title('Espectro de frecuencia de x(t)')
plt.xlim(0, 300)
plt.grid(True)
plt.tight_layout()
plt.show()
