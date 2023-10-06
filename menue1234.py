"""
Name:Raees 
Surname:Ramson

"""

import array as arr

# Declare and initialise variables
Price_list = arr.array('f', [9.50, 18.75, 37])
intCar_C = 0
intBike_C = 0
intTruck_C = 0
Cash_Total = 0
file = open("Totals.txt", 'w')
# Prompt user for input
print('MAIN MENU')
print('1.Register vehicle ')
print('2.Show totals ')
print('3.End day')
print('4.Write report ')
print('5.Exit Program')

# Choice
while True:
    choiceOpt = input("Enter option  ;> ")

    if choiceOpt == '1':
        print(Price_list)
        v_count = input("Please enter vehicle type (b, c, or t): ")

        if v_count.lower() == 'c':
            intCar_C += 1
            Cash_Total += Price_list[1]
        elif v_count.lower() == 'b':
            intBike_C += 1
            Cash_Total += Price_list[0]
        elif v_count.lower() == 't':
            intTruck_C += 1
            Cash_Total += Price_list[2]
        else:
            print("Invalid vehicle type. Please enter b, c, or t.")

    elif choiceOpt == '2':
        print("Totals:")
        print("Cars:", intCar_C)
        print("Bikes:", intBike_C)
        print("Trucks:", intTruck_C)
        print("Money : R", Cash_Total)

    elif choiceOpt == '3':
        print("The total number of cars is", intCar_C)
        print("The total number of Bikes is", intBike_C)
        print("The total number of trucks is", intTruck_C)
        print("The total income is R ", Cash_Total)

    elif choiceOpt == '4':
        print("Writing report.")
        file.write("Total number of bikes is: " + str(intBike_C) + "\n")
        file.write("Total number of cars is: " + str(intCar_C) + "\n")
        file.write("Total number of trucks is: " + str(intTruck_C) + "\n")
        file.write("Total number of vehicles is: " + str(intBike_C + intCar_C + intTruck_C) + "\n")
        file.write("Total income is R " + str(Cash_Total))

    elif choiceOpt == '5':
        print("Exiting the program.")
        file.close()
        break

    else:
        print("Invalid option. Please choose a valid option.")

print("Program has ended.")
