import time 
import os

def timer(t):
	"""
	Takes time t in seconds.
	Performs countdown and prints the timer.
	"""

	os.system('clear')
		
	while t:
		MM, SS = divmod(t, 60)

		print(f'===== {MM:02d}:{SS:02d} =====', end="\r") 
		# \r moves the cursor to the beginning of the 
		# line and then keeps outputting characters as normal
		
		time.sleep(1)

		t -= 1
	
	return


def main():
	MM, SS = input("Time in MM:SS -> ").split(":")
	
	MM, SS = int(MM), int(SS)
	
	t = MM * 60 + SS

	timer(t)

main()