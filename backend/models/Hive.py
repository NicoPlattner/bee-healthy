import time
import itertools
from SunTimeGenerator import SunTimeGenerator
from WeatherDataGenerator import WeatherDataGenerator
from HealthStatus_Algorithm import HealthStatus_Algorithm

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
        self.sensorData['epochTime'].append(now)
        
        
        solarTime = SunTimeGenerator.get_relative_solarTime_factor(
            now,
            self.locationGPSString
        )
        self.sensorData['solarTime'].append(solarTime)
        
        weatherState = WeatherDataGenerator.get_weather(self.locationGPSString)
        self.sensorData['weather'].append(weatherState)
        
        
        
        health = HealthStatus_Algorithm.health_calc_simple(self.sensorData)
        self.sensorData['predictedHealthStatus'].append(health)