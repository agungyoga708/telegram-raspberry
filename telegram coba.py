#coder :- Salman Faris

import sys
import time
#import random
#import datetime
import telepot
from telepot.loop import MessageLoop
import RPi.GPIO as GPIO

#LED
relay = 11
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# set up GPIO output channel
GPIO.setup(relay, GPIO.OUT)

GPIO.output(relay, 0)
#GPIO.output(11, 0)


def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Received: %s' % command)
    if 'on' in command:
        message = "Turned on "
        if 'relay' in command:
            message = message + "relay"
            GPIO.output(relay, 1)
            bot.sendMessage (chat_id, message)
        telegram_bot.sendMessage (chat_id, message)

    if 'off' in command:
        message = "Turned off "
        if 'relay' in command:
            message = message + "relay"
            GPIO.output(relay, 0)
            bot.sendMessage (chat_id, message)
            telegram_bot.sendMessage (chat_id, message)


bot = telepot.Bot('676287701:AAFMeR5b4kkpurJmLVUPDYMviv-HLNBdyac')
print (bot.getMe())
bot.message_loop(action)
print ('Up and Running....')

while 1:
     time.sleep(10)

