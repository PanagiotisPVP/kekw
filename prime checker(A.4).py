flag=True
import math
a=input("give your string:")
str_num=""
for letter in a:
    str_num+=str(ord(letter))
print("your string as a number represented in ASCII is:"+str_num)
N=int(str_num)
sqrt_N=int(math.sqrt(N))
if(N==1 or N==2):
    print("the number is prime")
else:
    for i in range(3,sqrt_N):
        if((N%i)==0):
            print("number is not prime")
            flag = False
            break;
if(flag and N>2):
    print("the number is prime")
x=input("press enter to close the program")
