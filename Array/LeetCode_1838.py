def maxFrequency(nums: list[int], k: int) -> int:
    nums.sort()
    l,r=0,0
    res,total=0,0
    while r<len(nums):
        total+=nums[r]
        if l+1<=r and nums[r]*(r-l+1) > total+k:
            total-=nums[l]
            l+=1
        res=max(res,r-l+1)
        r+=1
    return res

nums = list(map(int, input("enter the list of numbers with space : ").rstrip().split()))
k = int(input("enter the value of k : "))
print(maxFrequency(nums,k))