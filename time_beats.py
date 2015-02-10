import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
import pickle

#read audio samples
input = read("Roja 2.wav")
sample_per_sec = input[0]     #input[0] contains samples per second. 44.1k in this case

print "-------------"

audio = input[1]  
audio = abs(audio)

#len(audio) = 13230000. Duration of song = 300 sec. But actual duration is 390. This is because the .mp4 to .flac converter converts only the first 5 min of song. Resolvable.
#44.1k samples per second is correct according to audacity. 

Bavg_list = []
BmaxSavg_list = []

#BW increments by 85ms each iteration.
#SW increments 5ms each iteration
#44.1 samples per ms. So, 220.5 ~ 221 samples per 5ms. And 3748.5 ~ 3749 increments every 85ms.

markers = []

for BW in xrange(0,len(audio),3749):
  Bwin = audio[BW:BW+4410]
  max = np.mean(Bwin)

  SWindex = BW

  for SW in xrange(BW, BW+4410, 221):
    Swin = audio[SW:SW+882]
    #if (sum(abs(j) for j in Swin)/len(Swin)) > max:
    if (np.mean(Swin)) > max:
	     SWindex = SW
	     max = np.mean(Swin)


  markers.append(SWindex/44100.0)  #converting from samples to time

#removing duplicates if any
set = set(markers)
result = list(set)
print(result)

print "-------------"
print len(result)

with open('markers.txt', 'wb') as f:
    pickle.dump(markers, f)


