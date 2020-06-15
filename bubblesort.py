def bubblesort(list, reverse = 1):
    length = len(list)
    for i in range(0, length-1):
        for j in range(0, length-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    
    if reverse:
        list.reverse()
    return list
    