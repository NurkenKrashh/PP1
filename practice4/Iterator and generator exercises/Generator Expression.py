squares_list = [x*x for x in range(1,5)]
squares_gen = (x*x for x in range(1,5))
print(squares_list)
print(next(squares_gen))
print(next(squares_gen))