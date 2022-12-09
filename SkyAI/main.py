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
	print('1. open google\n2. open youtube\n3. Quit\n4. Prank')


# Duration Second Openned Selenium Chrome
def durationOpened(command):
	time.sleep(command)
	print('Duration > ', command, 'Second')


def searchGoogle(comamnd):
	driver = webdriver.Chrome()
	driver.get('https://www.google.com')
	formTextField = driver.find_elements(by=By.NAME, value='q');
	formTextField[0].send_keys(comamnd)
	time.sleep(3)
	btnSubmit = driver.find_elements(by=By.NAME, value='btnK')
	btnSubmit[0].send_keys(Keys.ENTER)

	durationSecond = int(input('Duration Second ? > '))
	durationOpened(durationSecond)

	print('running.....')

def searchYoutube(command):
	driver = webdriver.Chrome()
	driver.get('https://www.youtube.com')
	formTextField = driver.find_elements(by=By.NAME, value='search_query')
	formTextField[0].send_keys('python is')
	btnSubmit = driver.find_elements(by=By.ID, value='search-icon-legacy')
	btnSubmit[0].send_keys(Keys.ENTER)

	durationSecond = int(input('Duration Second ? > '))
	durationOpened(durationSecond)

	print('running.....')


if __name__ == '__main__':
	# testing area
	

	# formTextField = driver.find_elements(by=By.NAME, value='q');
	# formTextField[0].send_keys(command)
	# time.sleep(3)
	# btnSubmit = driver.find_elements(by=By.NAME, value='btnK')
	# btnSubmit[0].send_keys(Keys.ENTER)


	# Show My Method 
	print()
	welcome()

	while True:
		menu()
		ask = input('choose > ')

		if ask == "1":
			print('Opened Google...')
			print('waiting... ')
			time.sleep(1)
			searchGoogle = input('Please Search > ')
			print('Result Search = ', searchGoogle)
			
			searchGoogle(searchGoogle)
			
		elif ask == "2":
			print('Opened Youtube...')
			print('waiting... ')
			time.sleep(1)
			searchYoutube = input('Please Search > ')
			print('Result Search = ', searchYoutube)
			
			searchYoutube(searchYoutube)

			break
		elif ask == "3":
			print("coming soon")
			quit(1)
		elif ask == "4":
			print('========== WELCOME ==========')
			print('')

		else:
			print('nothing')