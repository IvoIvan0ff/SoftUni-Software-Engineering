temp = float(input())

if 5 <= temp <= 11.9:
    print("Cold")
elif 12.00 <= temp <= 14.9:
    print("Cool")
elif 15.00 <= temp <= 20.00:
    print("Mild")
elif 20.1 <= temp <= 25.9:
    print("Warm")
elif 26 <= temp <= 35.00:
    print("Hot")
else:
    print('unknown')

