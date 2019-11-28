# ASK demodulation

# used for editing wave files
import wave
# for basic mathematic operations
import numpy as np
# for using with wave functions
import struct

# frequency of ASK
frequency = 1000.0 # Hz
# sample duration in seconds
duration = 0.01 # seconds
# norm amplitude of zeros in modulated audio
zeroamp = 0.7
# audio file to be read from
audiofilename = "test.wav"

# open audio file
audiofile = wave.open(audiofilename, 'r')

# get number of frames in file
fileSize = audiofile.getparams()[3]

# get sample rate of recorded file
sample_rate = audiofile.getparams()[2]

# extract file into a list
audio_samples = audiofile.readframes(fileSize)


# number of samples for each symbol
num_symbol_samples = duration * sample_rate

def byte2int(byte):
    if byte > 127:
        return (256-byte) * (-1)
    else:
        return byte

def twoByte2int(byteH, byteL):
    f = (byteH << 8) | byteL
    if(byteH > 127):
        return (-1) * (2 ** 16 - f)
    else:
        return f

zipedAudio = zip(*[iter(audio_samples)] * 2)

# use numpy arrays
audio = np.array([twoByte2int(b1, b2) for b1, b2 in zipedAudio])

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

print(data)
