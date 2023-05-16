width = int(input())
length = int(input())
total_pieces = width * length
pieces_taken = 0

while True:
    piece = input()
    if piece == 'STOP':
        break
    piece = int(piece)
    pieces_taken += piece
    if pieces_taken >= total_pieces:
        break

if pieces_taken < total_pieces:
    print(f'{abs(total_pieces - pieces_taken)} pieces are left.')
else:
    print(f'No more cake left! You need {abs(total_pieces - pieces_taken)} pieces more.')

