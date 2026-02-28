def count_100_(n):
    for i in range(1,n+1):
        yield i

for x in count_100_(100):
    print(x)