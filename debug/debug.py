from math import pi


def area_of_circle(radius):
    return pi*radius**2


if __name__ == "__main__":
    A = area_of_circle(input("input a radius:"))
    print(A)