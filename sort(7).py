# Реализация пирамидальной сортировки на Python

# Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[]. n - размер кучи
def heapify(arr, n, i):
    minimum = i
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
        arr[i],arr[minimum] = arr[minimum],arr[i]

        # Применяем heapify к корню
        heapify(arr, n, minimum)

# Основная функция для сортировки массива заданного размера
def heapSort(arr): # n*log n
    n = len(arr)

    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # Один за другим извлекаем элементы
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

f  = open('input')
f.readline()

arr = list(map(int, f.readline().split()))
heapSort(arr)
n = len(arr)
file = open('output', 'w')

for i in range(n):
    file.write(str(arr[i])+' ')
