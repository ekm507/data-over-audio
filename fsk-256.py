# used for editing wave files
import wave
# for basic mathematic operations
import numpy as np
# for using with wave functions
import struct
# used for getting arguments
import sys
# for generating symbols
from functions import FSK_generate_symbols_2, generate_audio


# The sampling rate of the analog to digital convert
sampling_rate = 48000.0
# frequency of symbols to generate
frequency_list = [1500.0 + 45.0 * x for x in range(256)]

# symbol length in secounds
"""
wave envelope shape for each sign is like this:
a       ________
m     /          \
p___/              \___
\time<a ><  b   ><c ><d >

a: rise time
b: time in maximum amplitude
c: fall time
d: time in void

"""
# rise time
rise_duration = 0.010
# time in maximum amplitude
max_duration = 0.050
# fall time
fall_duration = 0.010
# time in void
void_duration = 0.010
# total time
total_duration = rise_duration + max_duration + fall_duration + void_duration
# number of symbol types. for fsk-256 it's 256.
num_frequency = 256
# amplitude of the audio
amplitude = 32000

# audio file to be saved into
try:
    audiofile = sys.argv[1]
except IndexError:
    audiofile = "test.wav"

# generate symbols
symbol = FSK_generate_symbols_2(frequency_list, (rise_duration, max_duration, fall_duration, void_duration), sampling_rate)

# data to modulate
data = [0, 1, 1, 0, 0, 1]

import random
random.seed(0)
data = [random.randint(0, 256) for i in range(100)]
print(data)

# data = [x for x in range(256)]

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
