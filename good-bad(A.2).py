flag=False
x = input("give the file path:")
file = open(x, "r")
whole_text =file.read()+" "
kako_grama=kalo_grama=0
ALL_LETTERS=("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
kaka_sumfwna=("fckrFCKR")
kala_sumfwna=("bdghjlmnpqstvwxyzBDGHJLMNPQSTVWXYZ")
for char in whole_text:
    if (not(char in ALL_LETTERS)):
        if(flag==True):
            if(kako_grama<kalo_grama):
                print(":good word")
            elif(kako_grama==0 and kalo_grama==0):
                print(":word has no consonant")
            else:
                print(":bad word")
            flag=False
            kalo_grama=kako_grama=0
    else:
        print(char,end="")
        flag=True
        if(char in kaka_sumfwna):
            kako_grama+=1
        if(char in kala_sumfwna):
            kalo_grama+=1
x=input("press enter to close the program")
file.close()