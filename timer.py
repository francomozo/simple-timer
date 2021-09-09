import argparse
import os

from src.timers import *

ap = argparse.ArgumentParser()

group = ap.add_mutually_exclusive_group()
group.add_argument('-p','--pomodoro', nargs='+', 
                help='Set Study/Rest in minutes. ie: -p 50 10.')
group.add_argument('-s','--simple', nargs='+', 
                help='Set simple timer mins/secs. ie: -s 2 15 (2 min 15 secs).')
group.add_argument('-d','--default', 
                help='Defaults for Pomodoro Study/Rest. Options: A:(30/30), B:(40/20), C:(45/15), D:(50/10).')

params = vars(ap.parse_args())

os.system('clear')

pomodoro_defaults = {'A': [30, 30], 'B': [40, 20], 'C': [45, 15], 'D': [50, 10]}

if params['pomodoro'] is not None:
	MM_study = int(params['pomodoro'][0])
	MM_rest = int(params['pomodoro'][1])
	pomodoro_technique(MM_study, MM_rest)
if params['simple'] is not None:
	MM = int(params['simple'][0])
	SS = int(params['simple'][1])
	simple_timer(MM, SS)
else:
	MM_study = pomodoro_defaults[params['default']][0]
	MM_rest = pomodoro_defaults[params['default']][1]
	pomodoro_technique(MM_study, MM_rest)
