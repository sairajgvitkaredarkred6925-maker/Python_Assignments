from Shapes import area_circle, area_rectangle, area_triangle   

def main():
    shape = input("Enter the shape (circle, rectangle, triangle): ").lower()

    if shape == "circle":
        radius = float(input("Enter the radius of the circle: "))
        area = area_circle(radius)
        print(f"The area of the circle is: {area:.2f}")

    elif shape == "rectangle":
        width = float(input("Enter the width of the rectangle: "))
        height = float(input("Enter the height of the rectangle: "))
        area = area_rectangle(width, height)
        print(f"The area of the rectangle is: {area:.2f}")

    elif shape == "triangle":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = area_triangle(base, height)
        print(f"The area of the triangle is: {area:.2f}")

    else:
        print("Invalid shape entered. Please enter circle, rectangle, or triangle.")

if __name__ == "__main__":          
    main()      