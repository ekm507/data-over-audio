# ASK demodulation

# used for editing wave files
import wave
# for basic mathematic operations
import numpy as np
# for using with wave functions
import struct
# used for getting arguments
import sys
# used for calculating hash sum of data
import hashlib

# frequency of ASK
frequency = 1000.0 # Hz
# sample duration in seconds
duration = 0.01 # seconds
# norm amplitude of zeros in modulated audio
zeroamp = 0.50
# audio file to be read from
try:
    audiofilename = sys.argv[1]
except IndexError:
    audiofilename = "test.wav"

# open audio file
audiofile = wave.open(audiofilename, 'r')

# get number of frames in file
fileSize = audiofile.getparams()[3]

# get sample rate of recorded file
sample_rate = audiofile.getparams()[2]


# extract file into a list
audio = []
for i in range(fileSize):
    x = audiofile.readframes(1)
    audio.append(struct.unpack('h', x))

# number of samples for each symbol
num_symbol_samples = duration * sample_rate


"""
each symbol will be detected this way:
1. read a sublist of the audio with length t
2. get mediate value for absolute value of samples
"""

# demodulate

t = num_symbol_samples
amplitude = []
for i in range(int(fileSize / t)):
    amplitude.append(np.sum(np.abs(audio[int(t * i):int(t * (i + 1))])) / t)

# numpy array of amplitudes
amps = np.array(amplitude)

# normalize amplitudes
amps /= np.max(amps)

# quantize amps to get data
data = 1 * (amps > zeroamp)

# for testing
print(data)
hash = hashlib.md5(data)
print(hash.hexdigest())
