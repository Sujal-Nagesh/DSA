def reverse(x):
    x = str(x)
    m = ""

    if x[0] == "-":
        m = x.replace(x[1:],"")
        x = x.replace(x[0],"")
    
    for i in range(len(x)):
        m+=x[(i+1)*(-1)]
        
    print(int(m))

reverse(int(input("Enter the Integer : ")))