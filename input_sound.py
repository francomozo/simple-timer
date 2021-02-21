import sounddevice as sd
from numpy import linalg as LA
import numpy as np
import os
from time import sleep

def alert_noise(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print(volume_norm)
    if volume_norm > 15:
        os.system('say "Please shut up"')
        sleep(4)
        
        
# duration in seconds
def start_listening(duration):
    with sd.Stream(callback=alert_noise):
        sd.sleep(duration * 1000)