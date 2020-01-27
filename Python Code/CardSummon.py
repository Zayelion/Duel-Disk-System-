import serial
from PIL import Image  

ser = serial.Serial(
	port='COM11',\
	baudrate=115200,\
	parity=serial.PARITY_NONE,\
	stopbits=serial.STOPBITS_ONE,\
	bytesize=serial.EIGHTBITS,\
		timeout=0)

# print("connected to: " + ser.portstr)
count=1


while True:
	data = ser.readline()

	if data :
		data_str = ''
		data_str+=chr(data[0])
		data_str+=chr(data[1])
		data_str+=chr(data[2])
		data_str+=chr(data[3])
		data_str+=chr(data[4])
		data_str+=chr(data[5])
		data_str+=chr(data[6])
		data_str+=chr(data[7])
		# print(data_str)
		if(data_str=='01546123'):
			print("Cyber End Dragon Found!")
			im = Image.open(r"01546123.jpg")
			im.show() 

ser.close()