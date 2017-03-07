import numpy as np
import wave
import alsaaudio
import sys

inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE)
inp.setchannels(1)
inp.setrate(44100)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)
inp.setperiodsize(1024)

name = sys.argv[1]
file_name = name+'.wav'
w = wave.open(file_name, 'w')
w.setnchannels(1)
w.setsampwidth(2)
w.setframerate(44100)
for i in range(300):
	l, data = inp.read()
	a = np.fromstring(data, dtype='int16')
	w.writeframes(a)