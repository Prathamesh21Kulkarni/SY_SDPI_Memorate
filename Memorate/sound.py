import sounddevice
from scipy.io.wavfile import write

fs = 44100
second = 10
record_voice = sounddevice.rec(int(second*fs),samplerate=fs, channels =2)
sounddevice.wait()
write("output.mp3",fs,record_voice)