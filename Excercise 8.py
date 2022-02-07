def sphere():
    radius = int(
        input("Please enter the radius of the sphere (in centimeters): "))
    surfacearea = 4 * 3.141592653589793 * radius * radius
    volume = 4 / 3 * 3.141592653589793 * radius * radius * radius
    rounded_value_volume = round(volume, 2)
    rounded_value_surfacearea = round(surfacearea, 2)
    print("This is the surface area: ", rounded_value_surfacearea, "cubic centimeters")
    print("This is the volume of the sphere:", rounded_value_volume, "cubic centimeters")


sphere()
