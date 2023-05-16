plastic = int(input())
paint = int(input())
razreditel = int(input())
hrs_to_finish = int(input())

plastic_price = (plastic + 2) * 1.50
paint_price = (paint + (paint * 0.1)) * 14.50
razreditel_price = razreditel * 5
bags = 0.40

total_price = plastic_price + paint_price + razreditel_price + bags
price_per_hrs = total_price * 0.3
total_price = total_price + (price_per_hrs * hrs_to_finish)

print(f'{total_price}')
