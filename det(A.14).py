x = input("give the file path:")
file = open(x, "r")
A=[[0 for i in range(3)] for i in range(3)]
for i in range(3):
    j=0
    line_str=file.readline()+" "
    temp_string=""
    for k in line_str:
        if(k==" "):
            temp_num = int(temp_string)
            A[i][j] = temp_num
            j += 1
            temp_string=""
            continue
        temp_string+=k
print("o pinakas sou:")
for i in range(3):
    for j in range(3):
        print (A[i][j],end=" ")
    print()
det_A=0
for i in range(3):
    det_A+=A[0][i]*(A[1][(i+1)%3]*A[2][(i+2)%3]-A[1][(i+2)%3]*A[2][(i+1)%3])*pow(-1,i)
print("me orizousa: "+str(det_A))
x=input("press enter to close the program")
file.close()