v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

p1_full = p1 * h
p2_full = p2 * h
total = p1_full + p2_full
p1_percentage = p1_full / total
p2_percentage = p2_full / total
total_percentage = total / v
excess_water = total - v

if total <= v:
    print(f"The pool is {(total_percentage * 100):.2f}% full. Pipe 1: {(p1_percentage * 100):.2f}%. Pipe 2: {(p2_percentage * 100):.2f}%.")

else:
    print(f"For {h:.2f} hours the pool overflows with {abs(excess_water):.2f} liters.")
