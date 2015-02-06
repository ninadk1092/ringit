import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

#read audio samples
input = read("01. The Eagles - Hotel California.wav")
sample_per_sec = input[0]     #input[0] contains samples per second. 44.1k in this case

print "-------------"

audio = input[1]  

#len(audio) = 13230000. Duration of song = 300 sec. But actual duration is 390. Check why this is happening. 
#44.1k samples per second is correct according to audacity. 

Bavg_list = []
BmaxSavg_list = []

#BW increments by 85ms each iteration.
#SW increments 5ms each iteration
#44.1 samples per ms. So, 220.5 ~ 221 samples per 5ms. And 3748.5 ~ 3749 increments every 85ms.

for BW in xrange(0,len(audio),3749):
  Bwin = audio[BW:BW+4410]
  Bavg = sum(abs(Bwin))/len(Bwin)
  Bavg_list.append(Bavg)
  Savg_list = []

  for SW in xrange(BW, BW+4410, 221):
    Swin = audio[SW:SW+882]
    if len(Swin)>0:
      Savg = sum(abs(Swin))/len(Swin)
    Savg_list.append(Savg)
  
  #maxS = max(Savg_list)
  BmaxSavg_list.append(Savg_list)

print type(BmaxSavg_list)

x=np.arange(len(BmaxSavg_list))
print type(x)
#x = np.linspace(0, len(BmaxSavg_list), len(BmaxSavg_list) +1)   #np.linspace(start,stop,number_of_numbers) 
print len(x), len(BmaxSavg_list)
plt.scatter(x,BmaxSavg_list)
plt.autoscale(tight=True)
plt.grid()
plt.show()

