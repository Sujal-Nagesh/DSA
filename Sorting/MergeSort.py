class Solution:
    def merge(self,arr, l, m, r): 
        temp = []
        left = l
        right = m+1
        while left<=m and right <= r:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        while left<=m:
            temp.append(arr[left])
            left+=1
            
        while right<=r:
            temp.append(arr[right])
            right+=1
        
        for i in range(l,r+1):
            arr[i] = temp[i-l]
        
    def mergeSort(self,arr, l, r):
        if l==r:
            return
        mid = (l+r)//2
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        self.merge(arr,l,mid,r)

n = int(input("Enter the Length of array : "))
array = list(map(int, input("Enter the array seperated with space : ").rstrip().split(" ")))
Solution().mergeSort(array,0,n-1)
print(array)
