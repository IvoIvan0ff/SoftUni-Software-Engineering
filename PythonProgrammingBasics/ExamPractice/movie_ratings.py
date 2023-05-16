movie_qty = int(input())
max_rate = 0
min_rate = 0
average_rate = 0
highest_rate = ''
lowest_rate = ''

for i in range(movie_qty):
    movie_name = input()
    movie_rating = float(input())
    average_rate += movie_rating

    if i == 0:
        max_rate = movie_rating
        min_rate = movie_rating
        highest_rate = movie_name
        lowest_rate = movie_name

    if movie_rating > max_rate:
        max_rate = movie_rating
        highest_rate = movie_name

    elif movie_rating < min_rate:
        min_rate = movie_rating
        lowest_rate = movie_name

print(f"{highest_rate} is with highest rating: {max_rate}")
print(f"{lowest_rate} is with lowest rating: {min_rate}")
print(f"Average rating: {average_rate / movie_qty:.1f}")
