import time
import board
import adafruit_dht
from datetime import datetime
from gpiozero import LED

sensor = adafruit_dht.DHT11(board.D16) # Change the pin number to the data pin of your DHT11 
red= LED(19) 
blue = LED(26) 

with open("temperature.csv", "a") as d:
    d.write("time,celsius,fahrenheit" "\n")

def to_fahrenheit(c):
    f = (c * 1.8) + 32
    return f 

while True:
    try:
        celsius = sensor.temperature # Get the temperature in Celcius from the sensor
        fahrenheit = to_fahrenheit(celsius)
        current_time = datetime.now()
        with open("temperature.csv", "a") as d:
            d.write("{0}".format(current_time.strftime("%H:%M:%S")) + "," + str(celsius) + "," + str(float(fahrenheit)) + "\n")
        red.off()
        blue.off()
        if fahrenheit <= 72:
            blue.on()
            red.off
        if fahrenheit >= 72:
            red.on()
            blue.off()
        time.sleep(3.0)
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error    
