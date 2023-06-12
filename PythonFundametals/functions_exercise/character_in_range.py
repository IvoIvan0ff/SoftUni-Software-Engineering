def charachters(first_symbol, second_symbol):
    for i in range(ord(first_symbol) + 1, ord(second_symbol)):
        symbols.append(chr(i))

    return symbols


first_char = input()
second_char = input()
symbols = []
charachters(first_char, second_char)
print(" ".join(symbols))
