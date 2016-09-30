cases = int(input())
for case in range(cases):
    [n, m, s] = [int(i) for i in input().split()]
    result = (n+m+s-1)%n
    print (n if result == 0 else result)
