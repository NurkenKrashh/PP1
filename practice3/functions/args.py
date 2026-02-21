def func(*numbers):
    if len(numbers)== 0:
        return None
    mx = numbers[0]
    for nums in numbers:
        if nums > mx:
            mx = nums
    return mx
print(func(1,2,3,4,1,2,6,7,77))
       
       
