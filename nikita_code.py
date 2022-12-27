Count = int(input("Please Enter a Number:"))
output = []


for x in range(0, Count):
    Pattern = str(input("Please Enter pattern:"))
    MainString = str(input("Please Enter a String:"))
    flag = 0
    for letter in Pattern:
        if(letter not in MainString):
            flag = 1
        
    if(flag == 0):
        output.append('YES')
    else:
        output.append('NO')

for x in output:
    print(x)
