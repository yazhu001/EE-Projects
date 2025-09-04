
import numpy as np
import matplotlib.pyplot as plt

def generate_signal(fs=1000, duration=1.0, freqs=(50, 120), amps=(1.0, 0.5), noise_std=0.05, phase_deg=(0.0, 0.0)):
    t = np.arange(0, duration, 1.0/fs)
    x = np.zeros_like(t, dtype=float)
    for f, a, p in zip(freqs, amps, phase_deg):
        x += a * np.sin(2*np.pi*f*t + np.deg2rad(p))
    if noise_std > 0:
        rng = np.random.default_rng(0)
        x += rng.normal(0.0, noise_std, size=t.shape)
    return t, x

def single_sided_fft(x, fs, window=True):
    N = len(x)
    if window:
        w = np.hanning(N)
        xw = x * w
        U = np.sum(w) / N
    else:
        xw = x
        U = 1.0
    X = np.fft.rfft(xw)
    f = np.fft.rfftfreq(N, 1.0/fs)
    A = (2.0 / (N * U)) * np.abs(X)
    if N % 2 == 0:
        A[-1] *= 0.5
    return f, A

def run_demo(fs=1000, duration=1.0, freqs=(50, 120), amps=(1.0, 0.5), noise_std=0.05,
             save_prefix="fft_demo", show=True):
    t, x = generate_signal(fs=fs, duration=duration, freqs=freqs, amps=amps, noise_std=noise_std)
    plt.figure()
    plt.plot(t, x)
    plt.title("Composite Signal (Time Domain)")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    if save_prefix:
        plt.savefig(f"{save_prefix}_time_series.png", dpi=200, bbox_inches="tight")
    f, A = single_sided_fft(x, fs=fs, window=True)
    plt.figure()
    plt.plot(f, A)
    plt.title("Single-Sided Amplitude Spectrum (FFT)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    if save_prefix:
        plt.savefig(f"{save_prefix}_spectrum.png", dpi=200, bbox_inches="tight")
    if show:
        plt.show()
    return (t, x), (f, A)

if __name__ == "__main__":
    run_demo()
