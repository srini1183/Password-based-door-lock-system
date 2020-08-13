import RPi.GPIO as GPIO
from twilio.rest import Client

Matrix = [['1','2','3','A'],['4','5','6','B'],['7','8','9','C'],['*','0','#','D']]

ROW = [7,11,13,15]
COL = [12,16,18,22]

for j in range(4):
	GPIO.setup(COL[j],GPIO.OUT)
	GPIO.output(COL[j],1)

for i in range(4):
	GPIO.setup(ROW[i],GPIO.IN)

s = ""
password = "1234"
count = 0

def alert():
	account_sid = 'YOUR ACCOUNT_SID'
	auth_token = 'YOUR AUTH TOKEN'
	client = CLient(account_sid,auth_token)
	message = client.message.create(
					body = 'Someone is trying to gain unauthorized access!',
					from_ = 'from number',
					to = 'to number' 
					)
def get():
	global s
	global password
	global count
	try:
		while True:
			while(len(s)<=4):
				for j in range(4):
					GPIO.output(COL[j],0)
					for i in range(4):
						if GPIO.input(ROW[i])==0:
							s+=Matrix[i][j]
							while GPIO.input(ROW[i])==0:
								pass

					GPIO.output(COL[j],1)
			if s == password:
				print('ACCESS GRANTED')
				s = ""
			else:
				print('ACCESS DENIED!)
				print('Try again!!')
				s = ""
				count = count+1
				if count>3:
					alert()
					break
		
	except KeyboardInterrupt:
		GPIO.cleanup()

if __name__=='__main__':
	get()