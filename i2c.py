import smbus

# スレーブ1（RaspberryPi　ルート取得用）
SLAVE_RASPI1 = 0x11

# スレーブ2（RaspberryPi　送受信用）
SLAVE_RASPI2 = 0x22

# スレーブ3（ArduinoUNO　モータ制御用）
SLAVE_ARDUINO1 = 0x33

# スレーブ4（ArduinoUNO　センサー値取得用）
SLAVE_ARDUINO2 = 0x44

# スレーブ5（Arduino nano　荷物受け取り用 上段）
SLAVE_ARDUINO3 = 0x55

# スレーブ6（Arduino nano　荷物受け取り用 下段）
SLAVE_ARDUINO3 = 0x66


def main():
	i2c = smbus.SMBus(1)

	motor_power = []

	while True:
		# センサ値の取得
		motor_power = i2c.read_i2c_block_data(SLAVE_ARDUINO2, 1, 2)

		# モータへの出力値の取得
		motor_power = i2c.read_i2c_block_data(SLAVE_RASPI1, 1, 2)

		# モータへの出力
		i2c.write_i2c_block_data(SLAVE_ARDUINO1, 0, motor_power)
		
		# センサ値のDB格納

main()