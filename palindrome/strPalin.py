def ispali(i,n,string):

    if i>=n/2:
        return True
    if string[i]!=string[n-i-1]:
        return False
    return ispali(i+1,n,string)

string = input("Enter the string : ")
ans = ispali(0,len(string),string)
print(ans)