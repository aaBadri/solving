# https://codeforces.com/contest/1676/problem/A

for _ in range(int(input())):
    a = input()
    if int(a[0])+int(a[1])+int(a[2]) == int(a[3])+int(a[4])+int(a[5]):
        print("YES")
    else:
        print("NO")