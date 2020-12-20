import time
import os

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

def end_sound(freq, duration, times):
	#duration = 1  # secs
	for _ in range(times):
		os.system(f'play -nq -t alsa synth {duration} sine {freq}')


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
	end_sound(freq, duration=1, times=1)

# ================================================================================
def pomodoro_technique():
	MM_study, SS_study = input("Study sprint time in MM:SS -> ").split(":")
	MM_study, SS_study = int(MM_study), int(SS_study)

	MM_rest, SS_rest = input("Rest sprint time in MM:SS -> ").split(":")
	MM_rest, SS_rest = int(MM_rest), int(SS_rest)

	os.system('clear')

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
		time.sleep(5)

def main():
	os.system('clear')
	mode = input("Press (p) for Pomodoro Technique, (s) for Simple Timer: ")

	if mode == "s":
		simple_timer()
	elif mode == "p":
		pomodoro_technique()
	else:
		print("Invalid option.")


main()
