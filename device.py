class Device:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def get_consumption(self):
        if self.is_on:
            return self.power
        return 0