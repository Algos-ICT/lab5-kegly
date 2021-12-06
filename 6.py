def get_min(a):
    if len(a)==0:
        return '*'
    else:

        k = a[0]
        a[0] = a[len(a) - 1]
        a.pop()
        heapify(a, 0)
        return str(k)


def heapify(a, i):  # log n   # sift down
    while 2 * i + 1 < len(a):
        l = 2 * i
        r = 2 * i + 1
        minimum = l
        if r < len(a) and a[r] < a[l]:
            minimum = r

        if a[i] <= a[minimum]:
            break
        a[i], a[minimum] = a[minimum], a[i]
        i = minimum


def add(a, x):
    a.append(x)
    i = len(a) - 1
    while i > 0 and a[(i - 1) // 2] > a[i]:  # sift up
        a[(i - 1) // 2], a[i] = a[i], a[(i - 1) // 2]
        i = (i - 1) // 2


def change(a, old, new):
    k = 0
    for i in range(len(a)):
        if a[i] == old:
            a[i] = new
            k = i
            break
    while k > 0 and a[(k - 1) // 2] > a[k]:  # sift up
        a[(k - 1) // 2], a[k] = a[k], a[(k - 1) // 2]
        k = (k - 1) // 2


f = open('input')
file = open('output', 'w')
opr = int(f.readline())
A = []
for x in range(opr):
    i = f.readline().rstrip()
    if i == 'X':
        file.write(get_min(A)+'\n')
    elif i[0] == 'A':
        add(A, int(i[2:]))
    elif i[0] == 'D':
        list_change = i.split()
        change(A, A[int(list_change[1])-1], int(list_change[2]))
