import math

n = 20
m = 13
x = 45

# T: O(N), S:O(1)
def Ifib(n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            temp = b
            b = a + b
            a = temp
        return b

# T: O(2^n), S:O(N)
def Rfib(n):
    if n <= 1:
        return n
    else:
        return Rfib(n-1) + Rfib(n-2)

# T: O(N), S:O(1)
def IfibMod(n):
    if n <= 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            temp = b%m
            b = (a%m + b%m)%m
            a = temp
        return b

# T: O(2^n), S:O(N)
def RfibMod(n):
    if n <= 1:
        return n
    else:
        return (RfibMod(n-1)%m + RfibMod(n-2)%m)%m

# T: O(N), S:O(1)
def fibMod_formula(n):
    if n == 0:
        return 1
    else:
        return (((fibMod_formula(n//2)**2)%m) * (x**(n%2))%m)%m

print(Ifib(n))
print(Rfib(n))
print(IfibMod(n))
print(RfibMod(n))
print(fibMod_formula(x))