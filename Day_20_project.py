def separate_even_odd_squares(start, end):
    even_squares = []
    odd_squares = []
    for i in range(start, end + 1):
        square = i * i
        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)
    return even_squares, odd_squares

start_num = 1
end_num = 10
even_list, odd_list = separate_even_odd_squares(start_num, end_num)

print(f"Even squares: {even_list}")
print(f"Odd squares: {odd_list}")