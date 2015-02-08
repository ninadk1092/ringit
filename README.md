# ringit

The bigger window

The process will be based on a 'sufficient' increase in the amplitudes over a 20ms window. This 'sufficiency' is indicative of a flare in the waveform.
The task is to identify the 20ms flare and get it to the centre of the 100ms window.
For the sake of convenience, 100ms window will be referred to as the BigWindow(BW) and 20ms as SmallWindow(SW).
For this purpose, with inspiriation from Nyquist sampling, BW will be shifted ahead by BW/2 = 50ms every iteration. and SW be shifted by SW/2 = 10ms every iteration within the BW until SW's upper limit coincides with BW's upper limit. This means 9 SWs and 8 SW-shifts per BW. !!!(To be thought about: this may not be the most efficient calculation. Leave that for the optimization phase. Don't optimize prematurely)


