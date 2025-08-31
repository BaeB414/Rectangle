# Bethany Butler
# CIS 261
# Week 8 Rectangle Lab
# 08/31/2025

from turtle import width


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
     
    @property
    def perimeter(self):
        return 2 * (self.height + self.width)

    @property
    def area(self):
        return self.height * self.width

    def draw(self):
        for i in range(self.height):
            if i == 0 or i == self.height - 1:
                print("* " * self.width)
            else:
                print("* " + " " (self.width - 2) + "*")

def main():
    while True:
        print("Rectangle Calculator")
        height = int(input("Height: "))
        width = int (input("Width: "))

        rect = Rectangle(height, width)

        print("Perimeter:", rect.perimeter)
        print("Area:". rect.area)

        rect.draw()

        choice = input("\nContinue? (y/n): ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()

