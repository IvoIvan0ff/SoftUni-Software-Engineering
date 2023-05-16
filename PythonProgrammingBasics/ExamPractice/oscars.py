hall_rent = int(input())

statues = hall_rent - (hall_rent * 0.3)
food = statues - (statues * 0.15)
sound = food / 2

total = hall_rent + statues + food + sound
print(f'{total:.2f}')