# Library
import pyttsx3 as outputSound
from datetime import datetime

def speak(command):
	# engine sound voice
	engine = outputSound.init()
	engine.say(command)
	engine.runAndWait()
	


# Method
def welcome():
	# datetime now
	dateNow = datetime.now()
	print('date:', dateNow, '\n')

	# say me on time 	
	if dateNow.hour >= 0 and dateNow.hour <= 10:
		print('Good Morning, Sir')
	elif dateNow.hour >= 10 and dateNow.hour <= 18:
		print('Good afternoon, Sir')
	elif dateNow.hour >= 18 and dateNow.hour <= 21:
		print('Good Night, Sir')
	else:
		print('Good Evening')

	print('Hi Valent!, can i help you?')


if __name__ == '__main__':
	# Method
	print()
	welcome()

	while True:
		speak('hello world')