#Coded by | lucifer
#https://github.com/technosier
import os,time
import webbrowser
from pykeyboard import PyKeyboard
os.system("title WhatsApp Spammer")

print "WhatsApp Spammer Initiated"

time.sleep(2)

webbrowser.open("https://web.whatsapp.com")# After opening link, scan QR

time.sleep(10)

keyboard = PyKeyboard()
keyboard.press_key(keyboard.tab_key)#Keyboard press 'TAB'

keyboard.type_string("test")#Name of contact to be spammed

keyboard.press_key(keyboard.enter_key)#Keyboard press 'ENTER'

time.sleep(2)

for i in range(1000):
	keyboard.type_string("Spam Test")#Spam message here
	keyboard.tap_key(keyboard.enter_key)


    
