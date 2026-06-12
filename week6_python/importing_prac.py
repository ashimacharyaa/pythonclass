#firstly importing math module
import math 

station_name = "Kathmandu_Weather_Station"
temperatures = [18.4, 22.1, 15.7, 29.3, 11.8, 25.6, 19.2]

def get_average(temps):
    return sum(temps)/len(temps)

def get_deviation(temps):
    mean = get_average(temps)

    variance = 0

    for temp in temps:
        variance += (temp-mean)**2 # eg: (10−14)2=(−4)2=16
    
    variance = variance/len(temps)
    return math.sqrt(variance)

def get_summary(temps):
    print("Station Name:",station_name)
    print("Minimum Temperature:",min(temps))
    print("Maximum Temperature:",max(temps))
    print("Standard Deviation:",round(get_deviation(temps),2))
    print("Average Temperature:",round(get_average(temps),2))
    
get_summary(temperatures)