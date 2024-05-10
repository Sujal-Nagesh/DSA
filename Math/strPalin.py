def isPalindrome(s):

    def alnum(string1):
        alnums = ""
        for i in string1:
            if i.upper():
                i=i.lower()
            if i.isalnum():
                alnums+=i
        return(alnums)

    def ispali(i,n,string):
        if i>=n/2:
            return True
        if string[i]!=string[n-i-1]:
            return False
        return ispali(i+1,n,string)

    st = alnum(s)
    return ispali(0,len(st),st)
    
string = input("Enter the sentence or a word for checking palindrome : ")
print(isPalindrome(string))

