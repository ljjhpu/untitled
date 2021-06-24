def MergeTwoArr(arr1, arr2):
    arr = []
    count = 0
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr.append(arr1[i])
            i += 1
            count += 1
        else:
            arr.append(arr2[j])
            j += 1
            count += 1
        if count == 10:
            print(arr[9])
            break


arr11 = [1, 3, 4, 6, 6, 9, 11, 13, 15, 16]
arr22 = [2, 3, 5, 6, 7, 10, 12, 13, 14, 18]
MergeTwoArr(arr11, arr22)
