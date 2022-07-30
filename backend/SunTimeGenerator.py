# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 22:56:15 2022

@author: thomas
"""

class SunTimeGenerator:
    #mockup sunrise / sundown hours for hypothetical location
    sunrise_sec = 19800     #5:30h
    sundown_sec = 73800     #20:30h
    
    
    #@staticmethod
    #def get_sunRise_sunDown(latitude, longitude):
    #    pass
        

    @staticmethod
    def get_relative_solarTime_factor(epochTimestamp, location):
        sunrise = SunTimeGenerator.sunrise_sec
        sundown = SunTimeGenerator.sundown_sec
        daytime = epochTimestamp % (60*60*24)
        return 2 * (daytime - sunrise) / (sundown - sunrise)
        



    
    # =============================================================================
    #       Once a day for each hive the sunriseTime and sundownTime should be
    #       updated. So either the class should not be static and an object 
    #       created for each hive; or the times are stored in the hive object and
    #       this SunRiseGenerater is automatically called once a day to update all
    #       hive objects
    #
    #       Data provided by
    #       https://sunrise-sunset.org/api
    # =============================================================================
    @staticmethod
    def update_sunRiseTimes():
        pass