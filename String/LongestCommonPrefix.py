def longestCommonPrefix(strs):
    ans = ""
    lis = sorted(strs)
    first = lis[0]
    last = lis[-1]
    for i in range(min(len(first),len(last))):
        if first[i] != last[i]:
            return ans
        ans+=first[i]
    print(ans)

lis = list(map(str, input("enter the list of word seperated with comma : ").rstrip().split(",")))
longestCommonPrefix(lis)