'''The distance between two cities (in km.) is input through the keyboard. Write a program to
convert and print this distance in meters, feet, inches and centimeters.'''


# Input distance in kilometers
distance_km = float(input("Enter the distance between two cities (in kilometers): "))

# Conversions
distance_meters = distance_km * 1000         # 1 kilometer = 1000 meters
distance_feet = distance_km * 3280           # 1 kilometer = 3280 feet
distance_inches = distance_km * 39370        # 1 kilometer = 39370 inches
distance_cm = distance_km * 100000           # 1 kilometer = 100000 centimeters

# Output results
print(f"Distance in meters: {distance_meters} m")
print(f"Distance in feet: {distance_feet} ft")
print(f"Distance in inches: {distance_inches} in")
print(f"Distance in centimeters: {distance_cm} cm")
