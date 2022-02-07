bike = 200
jog = 475
swim = 275

biking = int(input("How long do you spend biking? (In hours): "))
jogging = int(input("How long do you spend jogging? (In hours): "))
swimming = int(input("How long do you spend swimming? (In hours): "))

weightloss = biking * bike + jogging * jog + swimming * swim

print("Calories burned:", weightloss)

result = weightloss/3500 * 0.454

print("You have lost", result, "Kilograms")
