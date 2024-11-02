#Check Subset
n = int(input())
for i in range(n):
    ip1 = int(input())
    a = set(map(int, input().split()))

    ip2 = int(input())
    b = set(map(int, input().split()))
    print(a.issubset(b))