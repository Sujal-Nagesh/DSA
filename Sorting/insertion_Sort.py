def insertionSort(alist, n):
    
    for i in range(n):
        j = i
        while j > 0 and alist[j-1] > alist[j]:
            t = alist[j-1]
            alist[j-1] = alist[j]
            alist[j] = t
            j-=1
    
    
    print(alist)

n = int(input("Enter the Length of array : "))
array = list(map(int, input("Enter the array seperated with space : ").rstrip().split(" ")))
insertionSort(array,n)