# Bethany Butler
# CIS 261
# Week 8 Rectangle Lab
# 08/31/2025

while True:
    print("Rectangle Calculator")

    # Get user input for height and width
    height = int(input("\nHeight: "))
    width = int(input("Width: "))

    # Calculate perimeter and area
    perimeter = 2 * (height + width)
    area = height * width

    # Display results
    print(f"Perimeter: {perimeter}")
    print(f"Alea: {area}")

    # Print the rectangle
    for i in range(height):
        if i == 0 or i == height - 1:
            print("* " * width)
        else:
            print("*" + " " * (2 * width - 3) + "*")

    # Ask user if they want to continue
    cont = input("\nContinue? (y/n): ").lower()
    if cont != 'y':
        break

