# NLP_SpeechVisualization

## Overview

The program loads a speech audio file, generates a waveform, and creates a spectrogram to visualize the speech signal.
The purpose of this project was to learn how speech can be converted into data that a computer can analyze for speech recognition and natural language processing tasks.

The program will:

1. Load the speech audio file
2. Generate a waveform visualization
3. Generate a spectrogram visualization
4. Save the images as `waveform.png` and `spectrogram.png`

---

# Results

## Waveform

<img width="587" height="239" alt="image" src="https://github.com/user-attachments/assets/72fcf034-635b-48d1-9cee-85f95c3894ec" />


The waveform represents the speech signal in the time domain. It shows how the amplitude of the audio changes throughout the recording.

## Spectrogram

<img width="588" height="235" alt="image" src="https://github.com/user-attachments/assets/31f9a577-bc72-4b3d-83de-8bfe6385e373" />


The spectrogram represents the speech signal in the time-frequency domain. It displays how different frequencies appear and change over time.

---

# Analysis Questions

## 1. What does the waveform show about the speech signal?

The waveform shows how the volume of my speech changed during the 3.52-second recording. There is very little activity during the first half second, followed by several larger peaks between about 0.7 and 2.0 seconds. These peaks represent the louder portions of the recording. After about 2.5 seconds, the waveform gradually gets smaller as the recording comes to an end. 

## 2. What does the spectrogram show that the waveform does not?

The spectrogram shows which frequencies are present in the speech and how they change throughout the recording. While the waveform only shows changes in volume, the spectrogram shows how strong different frequencies are at different points in time. Most of the speech energy is concentrated below about 7,000 Hz, which is typical for human speech.

## 3. Where does the signal appear louder or stronger?

The signal appears strongest between about 0.7 and 2.0 seconds. In the waveform, this section contains the largest peaks, reaching amplitudes close to ±0.6. In the spectrogram, these same sections appear brighter, showing stronger energy across multiple frequencies.

## 4. Do you notice any regions that appear more steady or more noisy?

Yes. Some sections show more consistent frequency patterns, which appear steadier and are likely associated with vowel sounds. Other sections appear more spread out across frequencies, creating a noisier appearance that is typical of consonant sounds. There are also brief lower-energy areas between speech segments that likely represent short pauses.

## 5. Why might a spectrogram be more useful than a waveform for speech recognition tasks?

A spectrogram is more useful because it shows both frequency and time information. Speech recognition systems use frequency patterns to identify different sounds and words. The spectrogram makes these patterns visible, while the waveform only shows changes in volume over time. Because of this, the spectrogram provides more information for analyzing and recognizing speech.

---

# Time-Domain vs. Time-Frequency Representation

The waveform is a time-domain representation because it shows how the signal amplitude changes over time. The spectrogram is a time-frequency representation because it shows how the frequency content changes throughout the recording. While both visualizations provide useful information, the spectrogram offers a more detailed view of speech characteristics and is commonly used in speech processing and speech recognition systems.

---

# Conclusion

This project showed how speech can be visualized using both a waveform and a spectrogram. The waveform shows changes in volume over time, while the spectrogram shows how frequencies change throughout the recording. Together, they provide different ways to analyze speech and demonstrate how audio can be represented as data for speech processing applications.
