numbers = [1 , 3 , 4 ,5 ]
iter1 = iter(numbers)
while True:
    try:
        print(next(iter1))
    except StopIteration:
        break