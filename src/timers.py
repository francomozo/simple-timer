import os

from src.utils import *


def simple_timer(MM, SS):
    
	MM, SS = int(MM), int(SS)
	t = MM * 60 + SS

	os.system('clear')
	timer(t, label=None)

	os.system('clear')
	print("Finished")

	freq = 391.995  # It's a G
	end_sound(freq, duration=1, times=1)

 
def pomodoro_technique(MM_study, MM_rest, SS_study=0, SS_rest=0):

    MM_study, SS_study = int(MM_study), int(SS_study)
    MM_rest, SS_rest = int(MM_rest), int(SS_rest)

    os.system('clear')
    print(f'==> Pomodoro {MM_study}/{MM_rest}.')
    
    freq = 391.995  # It's a G
    sprint = 0

    while True:
        end_sound(freq=440, duration=1, times=1)

        t_study = MM_study * 60 + SS_study
        timer(t_study, label="Study")
        end_sound(freq, duration=1, times=1)


        t_rest = MM_rest * 60 + SS_rest
        timer(t_rest, label="Rest ")
        end_sound(freq, duration=.5, times=2)

        sprint += 1
        print(f' Sprint {sprint} completed')
        time.sleep(1)
