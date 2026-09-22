n = int(input("Enter n: "))

a = 0
b = 1

for i in range(n + 1):
    print(a, end=" ")
    c = a + b
    a = b
    b = c