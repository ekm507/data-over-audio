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


# generate symbols for FSK mode 2
"""
    FSK symbols generate
"""
def FSK_generate_symbols_2(frequencies, durations, sampling_rate):
    rise_duration, max_duration, fall_duration, void_duration = durations
    total_duration = rise_duration + max_duration + fall_duration + void_duration
    symbols = []
    t = int(total_duration * sampling_rate)
    template = np.arange(t) / sampling_rate
    rise_temp = np.arange(rise_duration * sampling_rate) / (rise_duration * sampling_rate)
    fall_temp = 1 - np.arange(fall_duration * sampling_rate) / (fall_duration * sampling_rate)
    max_temp = np.ones(int(max_duration *sampling_rate)) * 1.0
    void_temp = np.zeros(int(void_duration * sampling_rate))
    amp_temp = np.append(np.append(rise_temp, max_temp), np.append(fall_temp, void_temp))
    for freq in frequencies:
        symbol = np.sin(template * freq * 2 * np.pi) * amp_temp
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