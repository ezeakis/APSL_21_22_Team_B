#We based this code from this lesson
#https://projects.raspberrypi.org/en/projects/code-for-your-astro-pi-mission-space-lab-experiment/3
https://projects.raspberrypi.org/en/projects/code-for-your-astro-pi-mission-space-lab-experiment/9




import csv
from sense_hat import SenseHat
from datetime import datetime, timedelta
from pathlib import Path
from time import sleep
#We need CPU Temperature, in order to understand how temperature measured by the sensor is affected
from gpiozero import CPUTemperature

sense = SenseHat()
cpu = CPUTemperature()

#This command sets the path where the file will be stored.
base_folder = Path(__file__).parent.resolve()
data_file = base_folder/'data.csv'




with open(data_file, 'w', buffering=1) as f:
    writer = csv.writer(f)
    header = ("Date/time", "Temperature", "Humidity", "Pressure", "CPU Temperature")
    writer.writerow(header)
    #It will run 300 times which is less than three hours
    for i in range(300):
        row = (datetime.now(), round(sense.temperature), round(sense.humidity), round(sense.pressure), round(cpu.temperature))
        writer.writerow(row)
        #This is to show message on the display, it is part of the rules for a "Life in Space" experiment.
        sense.show_message(str(i))
        sleep(30)

        
        
        
