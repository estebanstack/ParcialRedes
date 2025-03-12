import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
fs = 10000           # Frecuencia de muestreo en Hz
duration = 1         # Duración de la señal en segundos
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Definición de la señal x(t)
x = np.sin(2 * np.pi * 50 * t) + 0.5 * np.sin(2 * np.pi * 120 * t) + 0.8 * np.sin(2 * np.pi * 200 * t)

# --- Gráfica 1: Señal en el dominio del tiempo ---
fig1 = plt.figure(figsize=(10, 4))
plt.plot(t[:500], x[:500], color='darkblue', lw=1.8)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal en el Dominio del Tiempo')
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Cálculo de la FFT para obtener la transformada de Fourier ---
X = np.fft.fft(x)
N = len(x)
freqs = np.fft.fftfreq(N, d=1/fs)

# Seleccionar únicamente frecuencias positivas (por simetría de señales reales)
positive = freqs >= 0
freqs_pos = freqs[positive]
X_pos = X[positive]
mag = np.abs(X_pos) / N  # Magnitud normalizada

# --- Gráfica 2: Espectro de frecuencia (transformada de Fourier) ---
fig2 = plt.figure(figsize=(10, 4))
plt.stem(freqs_pos, mag, linefmt='r-', markerfmt='ro', basefmt=" ", use_line_collection=True)
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.title('Espectro de Frecuencia de x(t)')
plt.xlim(0, 300)
plt.grid(True)
plt.tight_layout()
plt.show()
