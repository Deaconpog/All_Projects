sound = 340

seconds = float(input("Please enter the seconds counted before new thunder: "))

distance = sound * seconds

distancekm = round(distance/1000, 2)

print(distancekm, "km away")
