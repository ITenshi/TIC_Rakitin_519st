import numpy as np
from scipy import signal, fft
import matplotlib.pyplot as plt

def generate_random_signal(n, mean=0, std=10):
    return np.random.normal(mean, std, n)

def plot_signal(time, signal, xlabel, ylabel, title, save_path):
    fig, ax = plt.subplots(figsize=(21/2.54, 14/2.54))
    ax.plot(time, signal, linewidth=1)
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    plt.title(title, fontsize=14)
    fig.savefig(save_path, dpi=600)

def plot_spectrum(freqs, spectrum, xlabel, ylabel, title, save_path):
    fig, ax = plt.subplots(figsize=(21/2.54, 14/2.54))
    ax.plot(freqs, spectrum, linewidth=1)
    ax.set_xlabel(xlabel, fontsize=14)
    ax.set_ylabel(ylabel, fontsize=14)
    plt.title(title, fontsize=14)
    fig.savefig(save_path, dpi=600)

n = 500
Fs = 1000
F_max = 31

time = np.arange(n) / Fs
random_signal = generate_random_signal(n)

w = F_max / (Fs / 2)
sos = signal.butter(3, w, 'low', output='sos')
filtered_signal = signal.sosfiltfilt(sos, random_signal)

plot_signal(time, filtered_signal, 'Час (секунди)', 'Амплітуда сигналу',
            'Сигнал з максимальною частотою F_max=31Гц', './figures/signal.png')

spectrum = fft.fft(filtered_signal)
spectrum = np.abs(fft.fftshift(spectrum))
freqs = fft.fftfreq(n, 1/Fs)
freqs = fft.fftshift(freqs)

plot_spectrum(freqs, spectrum, 'Частота (Гц)', 'Амплітуда спектру',
              'Спектр сигналу з максимальною частотою F_max=31Гц', './figures/spectrum.png')
