def building():
    type = input("Building type (Commercial/Residential): ")
    length = int(input("Length (In meters): "))
    width = int(input("Width (In meters): "))
    depth = int(input("Depth (In meters): "))
    volume = length * width * depth
    print("Building type:", type)
    print("The volume of concrete required for a slab with a length of",
          length, "and a width of", width, "and a depth of", depth, "is",
          volume, "cubic meters")
    userinfo = input("Would you like to calculate another building?:")
    if userinfo == "y" and "Y" and "yes" and "Yes":
        building()
    else:
        print("You're calculated building(s) equals:",volume, "meters cubed")

building()
