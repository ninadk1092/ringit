import numpy as np
import scipy
from scipy.io.wavfile import read
from scipy.signal import hann
from scipy.fftpack import rfft
import matplotlib.pyplot as plt

#read audio samples
input = read("01. The Eagles - Hotel California.wav")
audio = input[1]

#apply Hanning window
#window = hann(1024)
#audio = audio[0:1024]

#fft
mags = abs(rfft(audio))

#convert to dB
mags = 20*scipy.log10(mags)

#normalise to 0 dB max
#mags -= max(mags)

#plot 
plt.plot(mags)
plt.ylabel("Magnitude (dB)")
plt.xlabel("Frequency")
plt.title("Hotel California Fourier Domain")
plt.show()

'''
plt.plot(audio[0:10000000000])
plt.ylabel("Amplitude")
plt.xlabel("Time(samples)")
plt.title("Kid in Town")
plt.show()
'''
