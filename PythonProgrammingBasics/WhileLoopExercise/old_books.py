book_name = input()
book_qty = 0

while True:
    user_input = input()
    if user_input == book_name:
        print(f'You checked {book_qty} books and found it.')
        break
    if user_input == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {book_qty} books.')
        break
    book_qty += 1
