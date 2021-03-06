class SpaceAge:
    def __init__(self, segundos):
        self.edad_años_terrestres = segundos / 31557600

    def on_earth(self):
        return self.tasa_edad(1)

    def on_mercury(self):
        return self.tasa_edad(0.2408467)

    def on_venus(self):
        return self.tasa_edad(0.61519726)

    def on_mars(self):
        return self.tasa_edad(1.8808158)

    def on_jupiter(self):
        return self.tasa_edad(11.862615)

    def on_saturn(self):
        return self.tasa_edad(29.447498)

    def on_uranus(self):
        return self.tasa_edad(84.016846)

    def on_neptune(self):
        return self.tasa_edad(164.79132)

    def tasa_edad(self, tasa):
        return round(self.edad_años_terrestres / tasa, 2)
