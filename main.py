from device import Device
from office import Office

# Devices
lamp = Device("Lamp", 10)
computer = Device("Computer", 120)
air_conditioner = Device("Air Conditioner", 900)

# Turn on some devices
lamp.turn_on()
computer.turn_on()

# Office
office = Office("Smart Office")

office.add_device(lamp)
office.add_device(computer)
office.add_device(air_conditioner)

# Results
print("Office:", office.name)

for device in office.devices:
    print(
        f"{device.name} | ON: {device.is_on} | Consumption: {device.get_consumption()} W"
    )

print("\nTotal Consumption:", office.total_consumption(), "W")