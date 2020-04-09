x = 1
y = 2
res = 2
i = x + y

while i < 4000000:
    if (x + y) % 2 == 0:
        res = res + x + y
    i = x + y
    x = y
    y = i

print(res)