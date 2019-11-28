import numpy as np

# generate symbols for FSK
"""
    FSK symbols generate
"""
def FSK_generate_symbols(frequencies, duration, sampling_rate):
    symbols = []
    t = int(duration * sampling_rate)
    template = np.arange(t) / sampling_rate
    for freq in frequencies:
        symbol = np.sin(template * freq * 2 * np.pi)
        symbols.append(symbol)
    return symbols

# generate symbols for ASK
def ASK_generate_symbols(frequency, amp, duration, sampling_rate):
    symbols = []
    t = int(duration * sampling_rate)
    template = np.sin(frequency * 2 * np.pi * np.arange(t) / sampling_rate)
    for a in amp:
        symbols.append(template * a)
    return symbols

# generate audio for FSK modulated
def generate_audio(data, symbols):
    audio = np.array([])
    for d in data:
        audio = np.append(audio, symbols[d])
    return audio