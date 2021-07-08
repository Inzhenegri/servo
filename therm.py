import time
import board
import adafruit_dht


dht_device = adafruit_dht.DHT11(pin=board.D17)

while True:
    try:
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity
        print(temperature_c, humidity)
    except RuntimeError as error:
        print(error.args[0])

    time.sleep(2)
