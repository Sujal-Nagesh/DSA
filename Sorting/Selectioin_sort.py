def Selection_Sort(n,arr):
    for i in range(n-1):
        mini = i 
        for j in range(i+1,n):
            if arr[j] < arr[mini]:
                mini = j
        temp = arr[i]
        arr[i] = arr[mini]
        arr[mini] = temp
    print(arr)

n = int(input("Enter the LEngth of array : "))
array = list(map(int, input("enter the array seperated with space : ").rstrip().split(" ")))
Selection_Sort(n,array)