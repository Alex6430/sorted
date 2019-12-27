def quicksort(nums, fst, lst):
    if fst >= lst:
        return
    i, j = fst, lst
    pivot = nums[i + (lst - i) // 2]

    while i <= j:
        while nums[i] < pivot: i += 1
        while nums[j] > pivot: j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
            quicksort(nums, fst, j)
            quicksort(nums, i, lst)


def bublesort(mas):
    for i in range(0, len(mas)):
        for j in range(0, len(mas)):
            if mas[i] < mas[j]:
                mas[i], mas[j] = mas[j], mas[i]


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i, j, k = 0, 0, 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


def insertsort(mas):
    for i in range(1, len(mas)):
        j = i
        while (j > 0 and mas[j - 1] > mas[j]):
            mas[j - 1], mas[j] = mas[j], mas[j - 1]
            j-=1


m = [1, 4, 5, 2, 4, 6, 8, 4, 23, 7, 5, 43, 56, 32]
# m = [1, 4, 2, 5]
# quicksort(m, 0, len(m) - 1)
# bublesort(m)
# mergeSort(m)
insertsort(m)
print(m)

