pen_qty = int(input())
marker_qty = int(input())
litre = int(input())
discount_in_p = int(input())

price_pen = 5.80
price_markers = 7.20
price_litre = 1.20

total_price_pen = pen_qty * price_pen
total_price_marker = marker_qty * price_markers
total_price_litre = litre * price_litre


total_sum = total_price_pen + total_price_marker + total_price_litre
total_sum = total_sum - (total_sum * discount_in_p / 100)
print(total_sum)
