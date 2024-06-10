def bubbleSort(arr, n):
    diff = 0
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                diff = 1
        if diff == 0:
            print(arr)
    print(arr)

n = int(input("Enter the Length of array : "))
array = list(map(int, input("Enter the array seperated with space : ").rstrip().split(" ")))
bubbleSort(array,n)