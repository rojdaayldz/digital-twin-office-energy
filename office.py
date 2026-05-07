class Office:
    def __init__(self, name):
        self.name = name
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def total_consumption(self):
        total = 0

        for device in self.devices:
            total += device.get_consumption()

        return total