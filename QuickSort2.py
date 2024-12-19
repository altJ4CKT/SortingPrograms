data = []
def menu():
    n = int(input("How much data items do you want to input: \n"))
    for i in range(n):
        usr_input = input("Input your data (Note: data must be off same format, strings, integers and etc): \n")
        data.append(usr_input)
        print(data)
    print(QuickSort2(data))

def QuickSort2(listToSort):
    if len(listToSort) <= 1:
        return listToSort
    else:
        pivot = listToSort[0]
        left = 1
        right = len(listToSort) -1
        while left <= right:
            while left <= right and listToSort[left] < pivot:
                left += 1
            while left <= right and listToSort[right] >= pivot:
                right -= 1
            if left <= right:
                if listToSort[left] > pivot and listToSort[right] < pivot:
                    listToSort[left], listToSort[right] = listToSort[right], listToSort[left]

        listToSort[0], listToSort[right] = listToSort[right], listToSort[0]

        left_part = QuickSort2(listToSort[:right])
        right_part = QuickSort2(listToSort[right+1:])
        return left_part + [listToSort[right]] + right_part

menu()