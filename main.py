#We based this code from this lesson
#https://projects.raspberrypi.org/en/projects/code-for-your-astro-pi-mission-space-lab-experiment/3

import csv
from sense_hat import SenseHat
from datetime import datetime
from pathlib import Path
from time import sleep

sense = SenseHat()

#This command sets the path where the file will be stored.
base_folder = Path(__file__).parent.resolve()
data_file = base_folder/'data.csv'

with open(data_file, 'w', buffering=1) as f:
    writer = csv.writer(f)
    header = ("Date/time", "Temperature", "Humidity", "Pressure")
    writer.writerow(header)
    for i in range(10):
        row = (datetime.now(), sense.temperature, sense.humidity, sense.pressure)
        writer.writerow(row)
        sense.show_message(datetime.now())
        sleep(30)
