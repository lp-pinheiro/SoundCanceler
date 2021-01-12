import soundcard as sc
import numpy

default_mic = sc.default_microphone()
default_speaker = sc.default_speaker()

print(default_mic)

data = default_mic.record(samplerate=48000, numframes=48000)
default_speaker.play(data/numpy.max(data), samplerate=48000)
