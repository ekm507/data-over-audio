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
frequency_list = [1000.0, 2000.0] # Hz
# number of symbol types. for mFSK 2 is enough.
num_frequency = 2
# sample duration in seconds
duration = 0.001 # seconds

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

# DEMODULATE

t = num_symbol_samples
amplitude = []
for i in range(int(fileSize / t)):
    amplitude.append(np.sum(np.abs(audio[int(t * i):int(t * (i + 1))])) / t)

# for each symbol in audio do:
for i in range(fileSize / num_symbol_samples):
    # calculate fft for symbol
    f = np.fft.fft(audio[i * num_symbol_samples : (i + 1) * num_symbol_samples])
