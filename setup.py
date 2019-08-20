from os import system, path
from platform import system as systemos, architecture

system('clear')

system('pip3 install -r requirements.txt')

print('\n [+] All the required python librarys have been installed sucessfully\n')
from wget import download

def check_webdriver():
	if path.isfile('chromedriver') == False:
		print('\n [+] Downloading chromedriver...\n')
		url = 'https://chromedriver.storage.googleapis.com/2.41/chromedriver_linux64.zip'
		file = download(url)
		system('unzip ' + file)
		system('rm -Rf ' + file)
		system('clear')
	else:
		print('\n[*] chromedriver aldready installed...\n')

if __name__ == '__main__':
	try:
		check_webdriver()
		system('chmod 755 snow.py')
	except KeyboardInterrupt:
		print('\n\n [-] Keyboard Interrupted... \n')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)