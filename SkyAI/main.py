# Library
import pyttsx3 as outputSound
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Method
def speak(command):
	# engine sound voice
	engine = outputSound.init()
	engine.say(command)
	engine.runAndWait()

def welcome():
	# datetime now
	dateNow = datetime.now()
	print('date:', dateNow, '\n')

	# say me on time 	
	if dateNow.hour >= 0 and dateNow.hour <= 10:
		print('Good Morning, Sir')
		speak('Good Morning, si')
	elif dateNow.hour >= 10 and dateNow.hour <= 18:
		print('Good afternoon, Sir')
		speak('Good afternoon, Sir')	
	elif dateNow.hour >= 18 and dateNow.hour <= 21:
		print('Good Night, Sir')
		speak('Good Night, Sir')
	else:
		print('Good Evening')
		speak('Good Evening')

	print('Hi Valent!, can i help you?')

def menu():
	print('1. open google\n2. open youtube\n3.Quit')

def searchGoogle(comamnd):
	driver = webdriver.Chrome()
	driver.get('https://www.google.com')
	driver.find_elements(by=By.NAME, value='q')
	driver.Send_keys(comamnd)
	time.sleep(3)
	driver.find_elements(by=By.NAME, value='btnK')
	driver.Send_keys(Keys.ENTER)
	time.sleep(3)
	driver.close
	

if __name__ == '__main__':
	# testing area
	searchingGoogle = input('Please Search > ')
	searchGoogle(searchingGoogle)

	# Show My Method 
	print()
	welcome()
	
	while True:
		menu()
		ask = input('choose > ')
		
		if ask == "1":
			print('Opened Google...')
			time.sleep(3)
			print('waiting... ')
			time.sleep(2)
			searchingGoogle = input('Please Search > ')
			searchGoogle(searchingGoogle)
			print('Result Search > ', searchingGoogle)

		elif ask == "2":
			print("coming soon")
			break
		elif ask == "3":
			print("coming soon")
			quit(1)
		else:
			print('nothing')