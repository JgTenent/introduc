import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

Led_Verde = 12

GPIO.setup(Led_Verde, GPIO.OUT)

#control + c sai

try:
	while True:
		print('Led Verde')
		GPIO.output(Led_Verde,True)
		time.sleep(2)
		print('Apagando')
		GPIO.output(Led_Verde,False)
		time.sleep(2)

except KeyboardInterrupt:
	print('Desligando...')
	GPIO.cleanup()
