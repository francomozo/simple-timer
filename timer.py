import time
import os
from sys import platform
import threading
from input_sound import start_listening


mac = True if platform == 'darwin' else False


def timer(t, label):
	"""
	Takes time t in seconds.
	Performs countdown and prints the timer.
	"""

	while t >= 0:
		MM, SS = divmod(t, 60)

		if label is not None:
			print(f' {label} == {MM:02d}:{SS:02d} ==', end="\r")
		else:
			print(f' == {MM:02d}:{SS:02d} ==', end="\r")
		# \r moves the cursor to the beginning of the
		# line and then keeps outputting characters as normal

		time.sleep(1)
		t -= 1
	return

def sound(sound=None, message=None):
	if sound: 
		freq, duration, times = sound
	#duration = 1  # secs
	if not mac:
		for _ in range(times):
			os.system(f'play -nq -t alsa synth {duration} sine {freq}')
	else:
		os.system(f'say "{message}"')

# ================================================================================
def simple_timer():
	MM, SS = input("Time in MM:SS -> ").split(":")
	MM, SS = int(MM), int(SS)
	t = MM * 60 + SS

	os.system('clear')
	timer(t, label=None)

	os.system('clear')
	print("Finished")

	freq = 391.995  # It's a G
	sound(freq, duration=1, times=1)

# ================================================================================
def pomodoro_technique():
	MM_study, SS_study = input("Study sprint time in MM:SS -> ").split(":")
	MM_study, SS_study = int(MM_study), int(SS_study)

	MM_rest, SS_rest = input("Rest sprint time in MM:SS -> ").split(":")
	MM_rest, SS_rest = int(MM_rest), int(SS_rest)

	os.system('clear')
	
	sprint = 0
	freq,times, duration= 391.995, 1, 1
	t = threading.Thread(target=start_listening, args=(MM_study*60+SS_rest,))
	while True:
		# You can pass the tuple as parameters by puting an asterisc like this:
		# function(*vairable=name) 
		sound(None, message='Focus time')
		t.start()
		t_study = MM_study * 60 + SS_study
		timer(t_study, label="Study")
		
		t.do_run = False
		t.join()
		sound(None, message='Rest time')


		t_rest = MM_rest * 60 + SS_rest
		timer(t_rest, label="Rest ")

		sprint += 1
		sound(None, message=f'Sprint {sprint} completed')
		print(f' Sprint {sprint} completed')
		time.sleep(2)

def main():
	os.system('clear')
	mode = input("Press (p) for Pomodoro Technique, (s) for Simple Timer: ")
	if mode == "s":
		simple_timer()
	elif mode == "p":
		pomodoro_technique()
	else:
		print("Invalid option.")

if __name__ == '__main__':
	main()
