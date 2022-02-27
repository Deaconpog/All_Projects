class Bus:
    bus_list = []  # List moved to the class

    def __init__(self, number, route, driver):
        self.number = number
        self.route = route
        self.driver = driver
        Bus.bus_list.append(self)

    def display_info(self):  # Display info method moved into the class
        for bus in Bus.bus_list:
            if bus == self:
                print(
                    f"Bus number is {self.number}. Route is {self.route} and "
                    f"driver is {self.driver}")


# Search function outside of class
def find_bus(question):
    bus_to_find = input(question)
    for bus in Bus.bus_list:  # Refers to class variable (bus_list)
        if bus_to_find == bus.number:
            return Bus.display_info(bus)  # Calls method within class
        print(f"Bus {bus_to_find} is not yet registered on the system.")


# Main routine
# Instantiate 3 objects
bus1 = Bus(2010, "Y", "Bill")
bus2 = Bus(2012, "P", "Greg")
bus3 = Bus(2077, "130", "Hillary")

# Print information
find_bus("Which bus do you want? (e.g. '2010', '2012', '2077' etc): ")
