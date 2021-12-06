def heapify(arr, n, i):
    global count
    global some_list
    minimum = i  # Initialize minimum as root
    l = 2 * i + 1   # левый ребенок
    r = 2 * i + 2   # правый ребенок

  # Проверяем существует ли левый дочерний элемент меньший, чем корень

    if l < n and arr[i] > arr[l]:
        minimum = l

    # Проверяем существует ли правый дочерний элемент меньший , чем корень

    if r < n and arr[minimum] > arr[r]:
        minimum = r

    # Заменяем корень, если нужно
    if minimum != i:
        arr[i],arr[minimum] = arr[minimum],arr[i] # свап
        count += 1
        some_list+= [[i, minimum]]
        # Применяем heapify к корню.
        heapify(arr, n, minimum)

f = open('input')
count = 0
some_list = []
line = f.readline()
A = list(map(int, f.readline().split()))
for i in range(len(A)//2, -1, -1):
    heapify(A, len(A), i)

file = open('output', 'w')
file.write(str(count)+'\n')
for i in some_list:
    file.write('%d %d \n' %(i[0], i[1]))