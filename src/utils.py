import os
import time


def timer(t, label):
    """
    Takes time t in seconds.
    Performs countdown and prints the timer.
    """
    
    while t >= 0:
        MM, SS = divmod(t, 60)
        HH, MM = divmod(MM, 60)

        if label is not None:
            fstr = f" {label} == {HH:02d}:{MM:02d}:{SS:02d} =="
            print(fstr, end="\r")
        else: # label is none for simple timer
            fstr = f' == {HH:02d}:{MM:02d}:{SS:02d} =='
            print(fstr, end="\r")

        
        time.sleep(1)
        print(" " * len(fstr), end="\r")
        t -= 1
    return

def end_sound(freq, duration, times):
    # duration = 1  # secs
    for _ in range(times):
    	os.system(f'play -nq -t alsa synth {duration} sine {freq}')


def echo_html(ts, label):
    with open('html/index.html', 'r') as file:
        data = file.readlines()

    data[19] = f'<p> {label} </p>\n'    
    data[25] = f'var date = "{ts}";\n'

    with open('html/index.html', 'w') as file:
        file.writelines(data)
