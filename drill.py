class Mobile:
    def __init__(self, brand, model, color, no_of_camera, processor, battery, os):
        self.brand = brand
        self.model = model
        self.color = color
        self.no_of_camera = no_of_camera
        self.processor = processor
        self.battery = battery
        self.os = os

    def swich_on(self):
        return False


class Motorbike:
    def __init__(self, brand, model, type_of_engine, fuel_type, no_of_gear, color):
        self.brand = brand
        self.model = model
        self.type_of_engine = type_of_engine
        self.fuel_type = fuel_type
        self.no_of_gear = no_of_gear
        self.color = color

    def turn_on(self):
            return False

    def isrunning(self):
            return False

