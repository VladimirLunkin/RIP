from Figures.rectangle import Rectangle
from Figures.square import Square
from Figures.circle import Circle

def main():
    my_rectangle = Rectangle(15, 10, "красный")
    my_square = Square(10, "желтый")
    my_circle = Circle(5, "фиолетовый")

    print(my_rectangle)
    print(my_square)
    print(my_circle)

    #pip

if __name__ == "__main__":
    main()
