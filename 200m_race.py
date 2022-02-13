# This is a program that asks for the finishing times of a 200m race until the
# user inputs -1, it will then print out the fastest time and the average time
# along with a list of all the times.

# List to fill in by the user of times
time_list = []

# Variables all set to 0 so as to receive inputs and store in list

time = 0
total_time = 0
fastest = 0

# While loop that repeats until the user enters -1 or 0

while time != -1:
    time = float(input("What was the time of the contestant?: "))

    if time > 0:
        total_time += time
        time_list.append(time)

    else:
        break

# Used to calculate the fastest time
for times in time_list:
    if times >= fastest:
        fastest = times

# Used to work out and print the average time, and print the fastest time
average = total_time / len(time_list)
print(time_list)
print("Average time of runs were: {}".format(average))
print("The fastest time was: {} seconds".format(fastest))
