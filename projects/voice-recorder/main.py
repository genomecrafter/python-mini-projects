# Voice Recorder

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv

# Sampling frequency
freq = 44100

# Recording duration
duration = 5

recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
sd.wait()
write("recording0.wav", freq, recording)
# or wv.write("recording0.wav", recording, freq, sampwidth=2)