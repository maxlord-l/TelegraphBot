#i, n, flag - переменные целого типа

flag = 1

if n > 2:

    flag = 0

    for i in range(2, n):

        if n % i == 0:

            flag = 1

            break

print(n == 2 or flag == 0)