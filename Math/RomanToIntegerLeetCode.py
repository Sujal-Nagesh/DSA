def romanToInt(s:str):
    rr = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }

    ans = 0
    for i in range(len(s)):
        if i < len(s)-1 and rr[s[i]] < rr[s[i+1]]:
            ans-=rr[s[i]]
        else:
            ans+=rr[s[i]]
    print(ans)

romanToInt(input("Enter any roman number : "))