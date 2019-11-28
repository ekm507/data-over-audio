# used for editing wave files
import wave
# for basic mathematic operations
import numpy as np
# for using with wave functions
import struct
# for generating symbols
from functions import ASK_generate_symbols, generate_audio

# The sampling rate of the analog to digital convert
sampling_rate = 48000.0
# frequency of symbols
frequency = 1000.0
# symbol length in secounds
duration = 0.01 # secounds
# amplitude of the audio
amplitude = 16000
# amplitude for 0 and 1
amp = [0.2, 1]
# audio file to be saved into
audiofile = "test.wav"

# generate ASK symbols
symbol = ASK_generate_symbols(frequency, amp, duration, sampling_rate)

# data to modulate
data = [0, 1, 1, 0, 0, 1]

import random
random.seed(0)
data = [random.getrandbits(1) for i in range(100)]

print(data)

audio = generate_audio(data, symbol)

# file properties
nframes = len(audio)
comptype="NONE"
compname="not compressed"
nchannels=1
sampwidth=2

# open wave file
wav_file=wave.open(audiofile, 'w')
# set properties
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

# write the audio to file
for s in audio:
   wav_file.writeframes(struct.pack('h', int(s*amplitude)))

wav_file.close()