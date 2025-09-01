# Bethany Butler
# CIS 261
# Week 8 Rectangle Lab (2 Attempt)
# 09/01/2025

class Rectangle:
    def __init__(self, height, width):
        self._height = height
        self._width = width

    # Property for height
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    # Property for width
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value

    # Method to calculate perimeter  
    def get_perimeter(self):
        return 2 * (self.height + self.width)

    #Method to calculate area
    def get_area(self):
        return self.height * self.width

    # Method to print rectangle
    def print_rectangle(self):
        for i in range(self.height):
            if i == 0 or i == self.height - 1:
                print("* " * self.width)
            else:
                print("*" + " " * (2 * self.width - 3) + "*")

def main():
    while True:
        print("\nRectangle Calculator\n")

        # Get user input
        height = int(input("Height: "))
        width = int(input("Width: "))

        # Create Rectangle object
        rect = Rectangle(height, width)

        # Display perimeter and area
        print(f"Perimeter: {rect.get_perimeter()}")
        print(f"Area: {rect.get_area()}\n")

        # Print rectangle
        rect.print_rectangle()

        #ask user if they want to continue
        cont = input("\nContinue? (y/n): ").lower()
        if cont != "y":
            break

if __name__ == "__main__":
    main()

