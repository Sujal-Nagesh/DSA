x = int(input("Enter only one no. for a square 2D array 'NxN' : "))
arr = []
sumList = []
y = x-2
def hourglassSum(arr):
    i = 0 
    while i<y:

        j = 0

        while j<y:

            l1=[arr[0+i][0+j],arr[0+i][1+j],arr[0+i][2+j],
                            arr[1+i][1+j],
                arr[2+i][0+j],arr[2+i][1+j],arr[2+i][2+j]]

            sumList.append(sum(l1))
            j+=1

        i+=1 
    return(sumList)




for _ in range(x):
    arr.append(list(map(int, input("Enter the 2D array of %dx%d with a space in it : " %(x,x)).rstrip().split())))

result = hourglassSum(arr)
print(arr)
print(sumList)
print(max(result))

