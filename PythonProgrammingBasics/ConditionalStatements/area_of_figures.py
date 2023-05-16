import math

type_figure = str(input())

if type_figure == 'square':
    side = float(input())
    area_square = side * side
    print(f"{area_square:.3f}")
elif type_figure == 'rectangle':
    side1 = float(input())
    side2 = float(input())
    area = side2 * side1
    print(f"{area:.3f}")
elif type_figure == 'circle':
    radius = float(input())
    area = math.pi * radius * radius
    print(f"{area:.3f}")
else:
    lenght = float(input())
    h = float(input())
    area = lenght * h / 2
    print(f"{area:.3f}")
