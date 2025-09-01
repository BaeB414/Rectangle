# Bethany Butler
# CIS 261
# Week 8 Rectangle Lab
# 08/31/2025

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
     
    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, value):
        if value <- 0:
            raise ValueError("Height must be a positive number.")
        self.height = value

    @property
    def width(self):
        return self.width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be a positive number.")
        self.width = value 
   
    @property
    def perimeter(self):
        return 2 * (self.height * self.width)

    @property
    def area(self):
        return self.height * self.width

    def draw(self):
        if self.height <= 0 or self.width <= 0:
            print("Cannot draw a rectangle with non-positive dimensions.")
            return
       
        print("-" * 15)

        print("*" * self.width)

        for _ in range(self.height - 2):
            if self.width <= 1:
                print("*")
            else:
                print("*" + " " * (self.width - 2) + "*")

        if self.height > 1:
            print("*" * self.width)

        print("-" * 15)

def main():
    while True:
        try:
            print("Rectangle Calculator")
            height = int(input("Height: "))
            width = int(input("Width: "))

            rectangle = Rectangle(height, width)

            print("Perimeter:", rectangle.perimeter)
            print("Area:", rectangle.area)

            rectangle.draw()

        except ValueError as e:
            print("Error:", e)
            print("Please enter a valid integer for height and width.")
            continue

        choice = input("Continue? (y/n): ")
        if choice.lower() != 'y':
            break   

if __name__ == "__main__":
    main()

