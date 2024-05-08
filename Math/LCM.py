def LCM(arr):
    max_num = max(arr)

    lcm = max_num
    while True:
        
        if all(lcm%i == 0 for i in arr):
            break
        lcm+=max_num

    return lcm
x = list(map(int, input("Enter integers separated by spaces: ").split()))
print(LCM(x))

