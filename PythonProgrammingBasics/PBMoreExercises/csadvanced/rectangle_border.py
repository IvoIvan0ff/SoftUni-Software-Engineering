x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

if x2 >= x >= x1 and y == y1:
    print("Border")
# check if the point is on the upper(y1<y2) horizontal (x) side
elif x2 >= x >= x1 and y == y2:
    print("Border")
# check if the point is on the left(x1<x2) vertical(y) side
elif y1 < y < y2 and x == x1:
    print("Border")
# check if the point is on the right(x1<x2) vertical(y) side
elif y1 < y < y2 and x == x2:
    print("Border")
else :
    print("Inside / Outside")
