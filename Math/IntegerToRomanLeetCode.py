
def intToRoman(num: int):
    r = {
        1:"I",2:"II",3:"III",4:"IV",
        5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",
        10:"X",20:"XX",30:"XXX",40:"XL",
        50:"L",60:"LX",70:"LXX",80:"LXXX",90:"XC",
        100:"C",200:"CC",300:"CCC",400:"CD",
        500:"D",600:"DC",700:"DCC",800:"DCCC",900:"CM",
        1000:"M",2000:"MM",3000:"MMM"
    }

    ans = []
    n = str(num)
    for i in range(len(n)):
        x = int(n[-1+i*(-1)])
        y = x*(10**i)
        ans.insert(-1+i*(-1),y)
    
    ans = [val for val in ans if val != 0]

    st = ""
    for i in ans:
        st = st + r[i]
    print(st)

intToRoman(int(input("Enter the number (0 < num <= 3999) : ")))