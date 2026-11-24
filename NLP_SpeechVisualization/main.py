"""
main.py

Student Starter Template
Speech Visualization Assignment

Instructions:
- Complete all TODO sections
- Load an audio file
- Generate a waveform
- Generate a spectrogram
"""

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# SETTINGS
# -----------------------------
AUDIO_FILE = "speech.wav"


# -----------------------------
# LOAD AUDIO
# -----------------------------
def load_audio(file_path):
    """
    Load an audio file.
    Returns:
    - y: audio signal
    - sr: sample rate
    """
    y, sr = librosa.load(file_path, sr=None)
    return y, sr


# -----------------------------
# PLOT WAVEFORM
# -----------------------------
def plot_waveform(y, sr):
    """
    Plot the waveform of the audio signal.
    """
    plt.figure(figsize=(10, 4))

    librosa.display.waveshow(y, sr=sr)

    plt.title("Speech Waveform")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")

    plt.tight_layout()

    plt.savefig("waveform.png")

    plt.show()


# -----------------------------
# PLOT SPECTROGRAM
# -----------------------------
def plot_spectrogram(y, sr):
    """
    Generate and plot a spectrogram.
    """
    S = np.abs(librosa.stft(y))

    S_db = librosa.amplitude_to_db(S, ref=np.max)

    plt.figure(figsize=(10, 4))

    librosa.display.specshow(
        S_db,
        sr=sr,
        x_axis="time",
        y_axis="hz"
    )

    plt.title("Speech Spectrogram")
    plt.xlabel("Time (seconds)")
    plt.ylabel("Frequency (Hz)")

    plt.colorbar(format="%+2.0f dB")

    plt.tight_layout()

    plt.savefig("spectrogram.png")

    plt.show()


# -----------------------------
# MAIN
# -----------------------------
def main():
    print("Loading audio file...")

    try:
        y, sr = load_audio(AUDIO_FILE)
    except Exception:
        print(f"ERROR: Could not load {AUDIO_FILE}")
        return

    print(f"Sample rate: {sr}")

    length = len(y) / sr
    print(f"Audio Length: {length:.2f} seconds")

    print("\nGenerating waveform...")
    plot_waveform(y, sr)

    print("Generating spectrogram...")
    plot_spectrogram(y, sr)

    print("\nDone! Your images should be saved.")


if __name__ == "__main__":
    main()