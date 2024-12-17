data = [13, 17, 3, 10, 12, 2, 20, 15]

def QuickSort(listToSort):
    if len(listToSort) <= 1:
        return listToSort
    else:
        pivot = listToSort[0]
        less = []
        equal = []
        greater = []
        for i in range(len(listToSort)):
            if listToSort[i] < pivot:
                less.append(listToSort[i])
            elif listToSort[i] == pivot:
                equal.append(listToSort[i])
            elif listToSort[i] > pivot:
                greater.append(listToSort[i])
        return QuickSort(less) + equal + QuickSort(greater)
    
print(QuickSort(data))
