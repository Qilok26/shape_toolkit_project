from shapes import Rectangle, Circle, Triangle
from utils import cm2_to_m2, compare_areas


def welcome():
    print("Welcome to the Shape Toolkit!")
    print("You can create the following shapes:")
    print("Rectangle (width, height)")
    print("Circle (radius)")
    print("Triangle (base, height)")
    print("-" * 40)


def create_shape():
    choice = input("Which shape would you like to create: ").lower()

    if choice == "rectangle":
        w = float(input("Enter width (cm): "))
        h = float(input("Enter height (cm): "))
        return Rectangle(w, h)
    elif choice == "circle":
        r = float(input("Enter radius (cm): "))
        return Circle(r)
    elif choice == "triangle":
        b = float(input("Enter base (cm): "))
        h = float(input("Enter height (cm): "))
        return Triangle(b, h)
    else:
        print("Invalid choice. Try again.")
        return None


def main():
    welcome()
    shape = create_shape()

    if shape:
        print(shape.describe())
        area_cm2 = shape.area()
        print(f"Area: {area_cm2:.2f} cm^2")
        print(f"Area: {cm2_to_m2(area_cm2):.4f} m^2")


if __name__ == "__main__":
    main()
