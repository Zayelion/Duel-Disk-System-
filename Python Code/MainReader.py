import serial
import FieldUpdater as FU 
import CardDB as CDB
import time
from selenium import webdriver


driver = webdriver.Chrome(r'C:\Users\Augusto\Documents\Unmovable\chromedriver.exe')
# driver.fullscreen_window()
driver.get("file:///C:/Users/Augusto/Documents/Proyectos/Duel%20Disk/DashboardTest.html")

ser = serial.Serial(
	port='COM12',\
	baudrate=9600,\
	parity=serial.PARITY_NONE,\
	stopbits=serial.STOPBITS_ONE,\
	bytesize=serial.EIGHTBITS,\
		timeout=1)
print("connected to: " + ser.portstr)

MonsterZones = [None,None,None,None,None]
SpellTrapZones = [None,None,None,None,None]
FieldZone = [None]
Graveyard = [None]
Vanished = [None]

while True:
	data = ser.readline()

	if data :
		print(data)
		action_str = ''
		action_str+=chr(data[0])
		action_str+=chr(data[1])
		action_str+=chr(data[2])
		
		cardid_str = ''
		cardid_str+=chr(data[3])
		cardid_str+=chr(data[4])
		cardid_str+=chr(data[5])
		cardid_str+=chr(data[6])
		cardid_str+=chr(data[7])
		cardid_str+=chr(data[8])
		cardid_str+=chr(data[9])
		cardid_str+=chr(data[10])

		print(action_str)
		print(cardid_str)
		
		Card = CDB.Get_Card_Data(cardid_str)
		print(Card)


		if action_str == "001":
			Card['pos'] = 'atk'
			print("Setting Monster in ATK mode")
			FU.Modify_Field_Value(Card, zone="P1MZ1",card_img='img/'+Card["id"]+".jpg",position=Card['pos'],delete=False) # Position and zone is determined by card reader sensors
			MonsterZones[1] = Card
			driver.get("file:///C:/Users/Augusto/Documents/Proyectos/Duel%20Disk/DashboardTest.html")

		if action_str == "010":
			Card['pos'] = 'def'
			print("Setting Monster in DEF mode")
			FU.Modify_Field_Value(Card, zone="P1MZ1",card_img='img/'+Card["id"]+".jpg",position=Card['pos'],delete=False) # Position and zone is determined by card reader sensors
			MonsterZones[1] = Card
			driver.get("file:///C:/Users/Augusto/Documents/Proyectos/Duel%20Disk/DashboardTest.html")

		if action_str == "011":
			Card['pos'] = 'atk'
			print("Setting Magic Trap or Pendulum")
			FU.Modify_Field_Value_Spells(Card, zone="P1STZ1",card_img='img/'+Card["id"]+".jpg",position=Card['pos']) # Position and zone is determined by card reader sensors
			SpellTrapZones[1] = Card
			driver.get("file:///C:/Users/Augusto/Documents/Proyectos/Duel%20Disk/DashboardTest.html")

		if action_str == "101":
			Card['pos'] = 'atk'
			print("Vanishing Monster in ATK mode")
			FU.Modify_Field_Value(Card, zone="P1MZ1",card_img='img/None.png',position=Card['pos'],delete=True) # Position and zone is determined by card reader sensors
			MonsterZones[1] = None
			driver.get("file:///C:/Users/Augusto/Documents/Proyectos/Duel%20Disk/DashboardTest.html")

		if action_str == "110":
			Card['pos'] = 'atk'
			print("Vanishing Monster in DEF mode")
			FU.Modify_Field_Value(Card, zone="P1MZ1",card_img='img/None.png',position=Card['pos'],delete=True) # Position and zone is determined by card reader sensors
			MonsterZones[1] = None
			driver.get("file:///C:/Users/Augusto/Documents/Proyectos/Duel%20Disk/DashboardTest.html")

		if action_str == "111":
			Card['pos'] = 'atk'
			print("Vanishing Magic Trap or Pendulum")
			FU.Modify_Field_Value_Spells(Card, zone="P1STZ1",card_img='img/None.png',position=Card['pos']) # Position and zone is determined by card reader sensors
			SpellTrapZones[1] = None
			driver.get("file:///C:/Users/Augusto/Documents/Proyectos/Duel%20Disk/DashboardTest.html")


ser.close()

# Card = CDB.Get_Card_Data('89631139')
# Card['pos'] = 'atk'
# print(Card["name"]+" Found!")
# time.sleep(2)
# FU.Modify_Field_Value(Card,Card, zone="P2MZ3",card_img='img/'+Card["id"]+".jpg",position=Card['pos']) # Psition and zone is determined by card reader sensors
# MonsterZones[1] = Card
# driver.get("file:///C:/Users/Augusto/Documents/Proyectos/Duel%20Disk/DashboardTest.html")