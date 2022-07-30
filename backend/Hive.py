class Hive:
    def __init__(self, id, name, locationGPSString, beeType):
        self.id = id
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
            'predictedHealthStatus': [],
            'weather': []
        }

    def addMeasurement(self, measurement):
        self.sensorData['temperature'].append(measurement['temperature'])
        self.sensorData['humidity'].append(measurement['humidity'])
        self.sensorData['pressure'].append(measurement['pressure'])
        self.sensorData['airQuality'].append(measurement['airQuality'])
        self.sensorData['beeSoundVolume'].append(measurement['beeSoundVolume'])
        self.sensorData['weight'].append(measurement['weight'])

        # TODO lookup and add epochTime
        # TODO lookup and add solarTime
        # TODO lookup and add weather
        # TODO calculate predictedHealthStatus

        # self.sensorData['epochTime'].append(measurement['epochTime'])
        # self.sensorData['solarTime'].append(measurement['solarTime'])
        # self.sensorData['weather'].append(measurement['weather'])
