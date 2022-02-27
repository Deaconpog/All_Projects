class Bus:
    def __init__(self, number, route, driver):
        self.number = number
        self.route = route
        self.driver = driver
        bus_list.append(self)


# Main routine
bus_list = []

bus1 = Bus(2010, "Y", "Bill")
bus2 = Bus(2012, "P", "Greg")
bus3 = Bus(2077, "130", "Hillary")

for bus in bus_list:
    print(f"The bus number is {bus.number} "
          f"the bus route is {bus.route} "
          f"with {bus.driver} as your driver.")
