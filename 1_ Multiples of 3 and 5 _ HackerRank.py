
def divisior_sum(n):
    n = n-1
    total_sum =0
    sum_multiples = lambda multiple : (((n//multiple)*((n//multiple)+1))//2)*multiple
    total_sum = sum_multiples(3)+ sum_multiples(5)-sum_multiples(15)
    print(total_sum)



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    divisior_sum(n)