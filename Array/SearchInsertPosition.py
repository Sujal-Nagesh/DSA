def searchInsert(nums,target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            print(mid)
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print(left)

array = list(map(int, input("Enter the Sorted array seperated with space : ").rstrip().split(" ")))
n = int(input("Enter the Target : "))

searchInsert(array,n)