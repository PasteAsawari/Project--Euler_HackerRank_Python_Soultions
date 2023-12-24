def sum_even_fibonacci(n):
    total_sum =0
    a,b = 1, 2 
    for i in range(0,n):
        if a%2 == 0 and a<n:
            total_sum +=a
        if a <n:
            a, b = b, a+b
        else:
            break
    print(total_sum)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum_even_fibonacci(n)