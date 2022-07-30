# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 00:20:40 2022

@author: thomas
"""

class HealthStatus_Algorithm:
    threshold_death_limit = 10 #volume below % indicates death
    threshold_death_fluctuation = 5 #fluctuation below % indicates death
    
    @staticmethod
    def health_calc_simple(hives_sensorData):
        dat = hives_sensorData
        datapoints_24hours = 6*24
        volumeData = dat['beeSoundVolume'][-datapoints_24hours:]
        
        minD = min(volumeData)
        maxD = max(volumeData)
        if ((maxD - minD)/2 < HealthStatus_Algorithm.threshold_death_limit and 
        maxD - minD < HealthStatus_Algorithm.threshold_death_fluctuation):        
            health = 0
        else:
            health = 100
        
        return health
        
        
        
    @staticmethod
    def health_calc_ANN(hives_sensorData):
        dat = hives_sensorData
# =============================================================================
#         Here should be running the machine learning algorithm
# =============================================================================
        pass

    
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