number_1 = int(input("Enter number 1: "))
try:
    number_2 = int(input("Enter number 2: "))
except ValueError:
    print("\nThat's not a valid number. Using 0 instead.")
    number_2 = 0
number_3 = int(input("Enter number 3: "))
Sum = (number_1 + number_2 + number_3)
Average = (Sum / 3)
print(f"\nYour numbers: {number_1}, {number_2}, {number_3}")
print(f"Sum: {Sum}")
print(f"Average: {Average}")


