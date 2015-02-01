from scipy.io.wavfile import read
import matplotlib.pyplot as plt

input = read("01. The Eagles - Hotel California.wav")
audio = input[1]
plt.plot(audio[0:10000000000])
plt.ylabel("Amplitude")
plt.xlabel("Time(samples)")
plt.title("Kid in Town")
plt.show()
