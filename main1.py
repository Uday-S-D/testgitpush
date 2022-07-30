x=0
while x<8:
    content = ""
    y=0
    while y<x:
        z=0
        sum=0
        while z<y:
            sum+=6-z
            z+=1
        if (x + 64 + sum) <= (64 + 26):
            content += " " + chr(x + 64 + sum)
        y+=1
    print(content)
    x+=1