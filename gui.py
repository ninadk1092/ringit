import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import pickle

markers = []

spf = wave.open('Roja 2.wav','r')

#reading all markers from markers.txt
with open('markers.txt', 'rb') as f:
    markers = pickle.load(f)

print markers

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
signal = np.fromstring(signal, 'Int16')
fs = spf.getframerate()

#converting into seconds
Time=np.linspace(0, len(signal)/(fs*2), num=len(signal))

#plotting graph
plt.figure(1)
plt.title('Roja')
plt.plot(Time,signal)

#drawing all the markers on the waveform
for number in markers:
	plt.axvline(x=number,linewidth=2,linestyle='dotted', color='r')

plt.show()


