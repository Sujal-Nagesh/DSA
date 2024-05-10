def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]

    ans = []
    last = 0
    
    for i in queries:
        
        query,x,y = i[0],i[1],i[2]
        
        idx = (x^last)%n
        
        if query == 1:
            arr[idx].append(y)
            
        else:
            last = arr[idx][y%len(arr[idx])]
            
            ans.append(last)
    return(ans)

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

q = int(first_multiple_input[1])

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

result = dynamicArray(n, queries)

print(result)

        