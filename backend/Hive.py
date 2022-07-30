import time
import itertools

class Hive:
    id_iter = itertools.count()
    
    def __init__(self, name, locationGPSString, beeType):
        self.id = next(Hive.id_iter)
        self.name = name
        self.locationGPSString = locationGPSString
        self.beeType = beeType

        self.sensorData = {
            'temperature': [],
            'humidity': [],
            'pressure': [],
            'airQuality': [],
            'beeSoundVolume': [],
            'weight': [],
            
            'epochTime': [],
            'solarTime': [],
            'weather': [],
            'predictedHealthStatus': []
        }

    def addMeasurement(self, measurement):
        self.sensorData['temperature'].append(measurement['temperature'])
        self.sensorData['humidity'].append(measurement['humidity'])
        self.sensorData['pressure'].append(measurement['pressure'])
        self.sensorData['airQuality'].append(measurement['airQuality'])
        self.sensorData['beeSoundVolume'].append(measurement['beeSoundVolume'])
        self.sensorData['weight'].append(measurement['weight'])
        
        now = round(time.time())
        
        
        self.sensorData['epochTime'].append()
        # TODO lookup and add epochTime
        # TODO lookup and add solarTime
        # TODO lookup and add weather
        # TODO calculate predictedHealthStatus


