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

    print("\n[First Shape]")
    shape1 = create_shape()
    if not shape1:
        return
    print(shape1.describe())
    area1 = shape1.area()
    print(f"Area: {area1:.2f} cm^2 ({cm2_to_m2(area1):.4f} m^2)")

    
    compare = input("\nWould you like to compare this with another shape? (yes/no): ").strip().lower()
    if compare == "yes":
        print("\n[Second Shape]")
        shape2 = create_shape()
        if not shape2:
            return
        print(shape2.describe())
        area2 = shape2.area()
        print(f"Area: {area2:.2f} cm^2 ({cm2_to_m2(area2):.4f} m^2)")

        result = compare_areas(shape1, shape2)
        print(f"\nComparison Result: {result}")

    print("\nThank you for using the Shape Toolkit!")

if __name__ == "__main__":
    main()
