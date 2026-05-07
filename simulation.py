import time
import random
import csv
from datetime import datetime

from device import Device
from office import Office


lamp = Device("Lamp", 10)
computer = Device("Computer", 120)
air_conditioner = Device("Air Conditioner", 900)
printer = Device("Printer", 300)

office = Office("Smart Office")

office.add_device(lamp)
office.add_device(computer)
office.add_device(air_conditioner)
office.add_device(printer)


with open("energy_log.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["time", "device", "is_on", "consumption_watt"])

    for i in range(10):
        print(f"\nSimulation step: {i + 1}")

        for device in office.devices:
            device.is_on = random.choice([True, False])

            consumption = device.get_consumption()

            print(
                f"{device.name} | ON: {device.is_on} | Consumption: {consumption} W"
            )

            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                device.name,
                device.is_on,
                consumption
            ])

        print("Total Consumption:", office.total_consumption(), "W")

        time.sleep(1)