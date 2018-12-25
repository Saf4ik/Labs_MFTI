
"""
 #Вариант сортировки выбором из книги "Грокаем алгоритмы"
def find_smallest(list):
    n = list[0]
    m = 0
    for x in range(1, len(list)):
        if list[x] < n:
            n = list[x]
            m = x
    return m

def select_sort(list):

    new_list = []
    for x in range(len(list)):
        smallest = find_smallest(list)
        new_list.append(list.pop(smallest))
    return new_list
"""


def insert_sort(A):
    """ сортировка вставками """
    for top in range(1, len(A)):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -= 1


def select_sort(A):
    """ сортировка выбором """
    for pos in range(0, len(A)-1):
        for k in range(pos+1, len(A)):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def bubble_sort(A):
    """ сортировка методом пузырька """
    for bypass in range(1, len(A)):
        for k in range(0, len(A)-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]


def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    print("testcase #1: ", end="")
    A = [4, 2, 3, 5, 1]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(20))
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")


test_sort(insert_sort)
test_sort(select_sort)
test_sort(bubble_sort)