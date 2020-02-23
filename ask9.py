ngtv=False
sum=0
num= int(input("give me your number"))
if (num<0):
    ngtv=True
while((num<-9) or (num>9)):
    num*=3
    num+=1
    num_str=str(num)
    for digit in num_str:
        if(digit=="-"):
            continue
        sum=sum+int(digit)
    num=sum
    if(ngtv):
        num=num*-1
    sum=0
    print(num)
x=input("press enter to close the program")