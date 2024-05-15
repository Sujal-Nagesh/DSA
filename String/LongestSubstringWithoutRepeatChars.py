def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0
    res = 0
    for i in range(len(s)):
        while s[i] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[i])
        res = max(res,i-l+1)
    print(res)

lengthOfLongestSubstring(input("Enter the String : "))