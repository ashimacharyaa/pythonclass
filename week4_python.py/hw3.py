sensors = [
    ("Chatara", 2.8),
    ("Tribeni Ghat", 5.4),
    ("Koshi Barrage", 4.1),
    ("Sunkoshi Bridge", 1.9),
    ("Sapatakoshi Camp", 6.0),
]

# check_water_level FUNCTION TO CHECK WATER LEVEL

def check_water_level(location, level_meters):

    if level_meters < 3:
        return "No Worries stay chill"

    elif 3 <= level_meters <= 5:
        return "Warning: Please be Alert, water level rising"
    else:
        return "DANGER: Water level above safe limit!"

# Record of Report
print("====== Flood Monitoring Report ======")

for location, level in sensors:
    status = check_water_level(location, level)

    print(f"{location} ({level}m): {status}")