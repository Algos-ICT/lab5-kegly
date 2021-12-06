# хто же я? куча ... иль нет?


f = open('input')
n = f.readline()
line= f.readline()
a = line.split()
flag = 1

for i in range(len(a)):
    if 2*i +2 <= len(a)-1:
        if a[i] > a[2*i+1] or a[i] > a[2*i+2]:
            flag = 0

    else:
        break


file = open('output', 'w')

if flag == 1:
    file.write('YES')
else:
    file.write('NO')


