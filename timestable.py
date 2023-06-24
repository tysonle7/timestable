number = int(input("Enter the investigated number: "))
lower_range = int(input("Enter the lower number of the range: "))
upper_range = int(input("Enter the upper number of the range: "))

for i in range(lower_range, upper_range + 1):
    result = number * i
    print(f"{number} x {i} = {result}")

while True:
    number = int(input("Enter the investigated number (0 to exit): "))
    if number == 0:
        print("Exiting the program...")
        break

    lower_range = int(input("Enter the lower number of the range: "))
    upper_range = int(input("Enter the upper number of the range: "))

    if lower_range >= upper_range or upper_range - lower_range > 10:
        print("Invalid range. Please try again.")
        continue


    for i in range(lower_range, upper_range + 1):
        result = number * i
        print(f"{number} x {i} = {result}")


