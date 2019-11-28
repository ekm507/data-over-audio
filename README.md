# Data over audio transmission

this is a solution for transmitting data over audio. like dial-up modems.

methods like **FSK**, **ASK** and **PSK** are going to be used for modulation.

for more knowledge see [this link of wikipedia]("https://en.wikipedia.org/wiki/Modulation#Digital_modulation_methods")

## ASK modulation and demodulation
in the transmitter side, using ask.py you can modulate a data into audio.  
and then in the receiver side, you can demodulate audio using de-ask.py

demodulation is done by getting mean value of absolute value of a set of samples  
and then comparing it with a normalized value.

also a synchronization method is needed for this algorithm (TODO).
