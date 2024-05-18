def strStr(haystack: str, needle: str):
    if needle in haystack:
        print(haystack.index(needle)) # will return the index of the first Occurring string
    else:
        print(-1) # else it will return -1 if not their

x = input("Enter the Haystack : ")
y = input("Enter the Needle : ")
strStr(x,y)