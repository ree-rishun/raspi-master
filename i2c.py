# import
import smbus
import sqlite3
import datetime
import sys
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# firestore
cred = credentials.Certificate("/key/raspberry-cd286-firebase-adminsdk-5wkl2-1efe47f7a1.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# define
SLAVE_RASPI1 = 0x11	# スレーブ1（RaspberryPi　ルート取得用）
SLAVE_RASPI2 = 0x22	# スレーブ2（RaspberryPi　送受信用）
SLAVE_ARDUINO1 = 0x33	# スレーブ3（ArduinoUNO　モータ制御用）
SLAVE_ARDUINO2 = 0x44	# スレーブ4（ArduinoUNO　センサー値取得用）
SLAVE_ARDUINO3 = 0x55	# スレーブ5（Arduino nano　荷物受け取り用 上段）
SLAVE_ARDUINO3 = 0x66	# スレーブ6（Arduino nano　荷物受け取り用 下段）

# main
def main():
	i2c = smbus.SMBus(1)
	time.sleep(1)
	motor_power = [ 0x40 , 0x2e ]

	while True:
		users_ref = db.collection(u'state')
		docs = users_ref.stream()
		for doc in docs:
			print(u'{} => {}'.format(doc.id, doc.to_dict()))

		# モータへの出力
		# i2c.write_i2c_block_data(SLAVE_ARDUINO1, 0, motor_power)

		# センサ値のDB格納

main()
