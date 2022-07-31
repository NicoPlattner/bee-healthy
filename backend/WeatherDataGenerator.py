# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 23:46:30 2022

@author: thomas
"""

import enum

class WeatherDataGenerator:
    class WeatherState(enum.Enum):
        sunny = 0
        lightCloud = 1
        heavyCloud = 2
    
    #mockup weather state
    weather = WeatherState.lightCloud
    
    
    #Mockup method to get weather
    @staticmethod
    def get_weather(location):
        return WeatherDataGenerator.weather
        
    @staticmethod
    def mockup_changeWeather(weather):
        WeatherDataGenerator.weather = weather


    
    # =============================================================================
    #       Once a day for each hive the weather should be
    #       updated. So either the class should not be static and an object 
    #       created for each hive; or the times are stored in the hive object and
    #       this class is automatically called once a day to update all
    #       hive objects
    #
    #       Data provided by
    #       https://sunrise-sunset.org/api
    # =============================================================================
    @staticmethod
    def update_weather():
        pass