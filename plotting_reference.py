import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

#read audio samples
input = read("01. The Eagles - Hotel California.wav")
sample_per_sec = input[0]     #input[0] contains samples per second. 44.1k in this case

print "-------------"

audio = input[1]  
audio = abs(audio)  #absolute values

#len(audio) = 13230000. Duration of song = 300 sec. But actual duration is 390. Check why this is happening. 
#44.1k samples per second is correct according to audacity. 

Bavg_list = []
BmaxSavg_list = []

#BW increments by 85ms each iteration.
#SW increments 5ms each iteration
#44.1 samples per ms. So, 220.5 ~ 221 samples per 5ms. And 3748.5 ~ 3749 increments every 85ms.

markers = []
bigwindow = []
for BW in xrange(0,len(audio),3749):
  Bwin = audio[BW:BW+4410]
  #max = sum(i for i in Bwin)/len(Bwin)  
  max = np.mean(Bwin)
  bigwindow.append(BW)
  SWindex = BW

  for SW in xrange(BW, BW+4410, 221):
    Swin = audio[SW:SW+882]
    if (np.mean(Swin)) > max:
	SWindex = SW
	max = np.mean(Swin)

  markers.append(SWindex)
 
print len(markers) 
y = np.empty(len(markers))
y.fill(3)

#Sampling one audio sample every 10 samples
#sampled_audio = [audio[i] for i in xrange(0,len(audio),10)]

x = np.arange(0,len(audio))

plt.plot(x,audio,'g.')

for k in xrange(0,35000,1000):
  y = np.empty(len(markers))
  y.fill(k)
  plt.plot(markers,y,'r|')
  plt.plot(bigwindow,y,'b|')

plt.show()

