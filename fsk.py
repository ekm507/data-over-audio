# used for editing wave files
import wave
# for basic mathematic operations
import numpy as np
# for using with wave functions
import struct
# used for getting arguments
import sys
# for generating symbols
from functions import FSK_generate_symbols, generate_audio


# The sampling rate of the analog to digital convert
sampling_rate = 48000.0
# frequency of symbols to generate
frequency_list = [1000.0, 2000.0]
# symbol length in secounds
duration = 0.01 # secounds
# number of symbol types. for mFSK 2 is enough.
num_frequency = 2
# amplitude of the audio
amplitude = 16000

# audio file to be saved into
try:
    audiofile = sys.argv[1]
except IndexError:
    audiofile = "test.wav"

# generate symbols
symbol = FSK_generate_symbols(frequency_list, duration, sampling_rate)

# data to modulate
data = [0, 1, 1, 0, 0, 1]

import random
data = [random.getrandbits(1) for i in range(100)]

# generate an audio based on data fsk
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