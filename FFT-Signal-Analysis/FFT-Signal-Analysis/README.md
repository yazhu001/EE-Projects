
# FFT Signal Analysis

## Introduction
This project generates a composite sine-wave signal (e.g., 50 Hz + 120 Hz) and analyzes it using the Fast Fourier Transform (FFT).
It produces two figures: the time-domain waveform and the single-sided amplitude spectrum.

## Files
- `fft_signal_analysis.py`: Main script containing signal generation and FFT utilities.
- `requirements.txt`: Dependencies (`numpy`, `matplotlib`).
- Example outputs (created after running the script):
  - `fft_demo_time_series.png`
  - `fft_demo_spectrum.png`

## Quick Start
1) Install dependencies:
```bash
pip install -r requirements.txt
```

2) Run the script:
```bash
python fft_signal_analysis.py
```

This will display the plots and save two images in the same folder.

## Customize
You can modify parameters in `run_demo(...)`:
- `fs`: sampling rate (Hz)
- `duration`: length of signal (s)
- `freqs`: tuple of signal frequencies
- `amps`: amplitudes for each frequency
- `noise_std`: standard deviation of added white noise (0 for none)

## Notes
- A Hann window is applied before FFT to reduce spectral leakage. The amplitude is scaled to single-sided spectrum.
- This demo showcases Python-based signal processing and visualization suitable for an EE portfolio.
