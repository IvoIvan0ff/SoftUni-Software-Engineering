x = float(input())
y = float(input())
h = float(input())

side_wall = x * y
window = 1.5 * 1.5
side_wall_total = (side_wall * 2) - (window * 2)
back_wall = x * x
door = 1.2 * 2
back_wall_total = (back_wall * 2) - door
total_walls = back_wall_total + side_wall_total
total_walls_paint = total_walls / 3.4
print("%.2f" % total_walls_paint)

roof_main = 2 * (x * y)
roof_sides = 2 * ((x * h) / 2)
total_roof = roof_main + roof_sides
total_roof_paint = total_roof / 4.3
print("%.2f" % total_roof_paint)
