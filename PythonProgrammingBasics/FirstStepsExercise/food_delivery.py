chicken = int(input())
fish = int(input())
veggie = int(input())

chicken_price = 10.35
fish_price = 12.40
veggie_price = 8.15
delivery = 2.50

total_chicken = chicken * chicken_price
total_fish = fish * fish_price
total_veggie = veggie * veggie_price

total_price = total_fish + total_veggie + total_chicken
desert = total_price * 0.2
total_total_price = total_price + desert + delivery
print(total_total_price)