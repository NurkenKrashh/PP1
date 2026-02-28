def evenn(n):
    for i in range(2,n+1,2):
        yield i 
for x in evenn(10):
    print(x)