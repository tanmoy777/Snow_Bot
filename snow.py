import os, argparse, datetime
import wikipedia, platform
from os import system
from time import sleep
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from selenium import webdriver

bot = ChatBot('Snow')
#function for facebook login automation using selenium webdriver
def fb_login():
	browser = webdriver.Chrome(executable_path=r'./chromedriver')
	browser.get('https://facebook.com')
	#later i'll add a better way to provide credentials
	user = browser.find_element_by_id('email')
	#change the username to u'r facebook username
	user.send_keys('example@gmail.com')
	password = browser.find_element_by_id('pass')
	#change the password to u'r facebook password
	password.send_keys("pass123")
	password.submit()

#function to greet users based on the time zone.
def greet():
	current_time = int(datetime.datetime.now().hour)

	if current_time >= 0 and current_time < 12:
		print('\nsnow: good morning sir!')

	if current_time >= 12 and current_time < 18:
		print('\nsnow: good afternoon sir!')

	if current_time >= 18 and current_time != 0:
		print('\nsnow: good evening sir!')

greet()
#setting up the location of the dataset to be trained
try:
	conv = open('chats.txt', 'r').readlines()

except FileNotFoundError:
	print('\n[-] You dont have any data to train the bot\n')

bot.set_trainer(ListTrainer)

#setting up the train command via argparse library
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--train', help='Train and save the data to the Db', action='store_true')
args = parser.parse_args()

if args.train:
	bot.train(conv)

#the input and output handling loop
while True:
	request = input('\nUser: ').lower()
	if request == 'login to facebook' or request == 'login fb':
		print('snow: logging in to facebook')
		fb_login()
		continue
	if request == 'bye' or request == 'exit':
		print('snow: bye sir\n')
		exit()
	if request == 'poweroff' or request == 'shut down':
		print('arya: shutting down the system')
		sleep(1)
		system('poweroff')
	if request == 'restart' or request == 'reboot':
		print('arya: rebooting the system the system')
		sleep(1)
		system('reboot')
#try to pull data from the trained db
	response = bot.get_response(request)
	if response.confidence >= 0.7:
		print('snow:', response)
		print('')
	else:
		try:
			result = wikipedia.summary(request, sentences=2)
			print('snow:', result)
		except:
			print('snow: i am sorry sir i dont have any data about this')
