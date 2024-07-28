def area_of_triangle(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

print("This program will find the area of two triangles and their contributions")

print("First triangle:")
a1 = float(input("Enter side a1: "))
b1 = float(input("Enter side b1: "))
c1 = float(input("Enter side c1: "))

print("Second Triangle:")
a2 = float(input("Enter side a2: "))
b2 = float(input("Enter side b2: "))
c2 = float(input("Enter side c2: "))

area_of_triangle1 = area_of_triangle(a1, b1, c1)
area_of_triangle2 = area_of_triangle(a2, b2, c2)

total_area = area_of_triangle1 + area_of_triangle2

print("Area of first triangle is:", area_of_triangle1)
print("Area of second triangle is:", area_of_triangle2)

print("Total area covered by both triangles is:", total_area)

print("Contribution % of triangle 1 is:", (area_of_triangle1 / total_area) * 100)
print("Contribution % of triangle 2 is:", (area_of_triangle2 / total_area) * 100)
