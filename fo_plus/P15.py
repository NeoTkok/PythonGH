def S(x): #сумма цифр
    P = 0
    while(x > 0):
        P += x % 10
        x =x // 10
    return P

n = int(input())

while(n>=10):
    n = S(n)
print(n)