n = int(input())
average_rate = 0
total_sales = 0

for i in range(n):
    sales_rate = int(input())
    rate = sales_rate % 10
    possible_sales = sales_rate // 10
    average_rate += rate
    if rate == 2:
        sales_made = possible_sales * 0
    elif rate == 3:
        sales_made = possible_sales * 0.5
    elif rate == 4:
        sales_made = possible_sales * 0.7
    elif rate == 5:
        sales_made = possible_sales * 0.85
    elif rate == 6:
        sales_made = possible_sales * 1
    total_sales += sales_made

print(f'{total_sales:.2f}')
print(f'{average_rate / n:.2f}')


