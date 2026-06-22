a=int(input("Enter First Number:"))
b=int(input("Enter Second Number:"))
print("Enter 1 for Additon , Enter 2 for Subtration , Enter 3 for Multiplication , Enter 4 for DIvision")
c=int(input("Enter Your Choice"))
if c==1:
    print("Additon :",a+b)
elif c==2:
    print("Subtraction :",a-b)
elif c==3:
    print("MUltiplication :",a*b)
elif c==4:
    print("Division :",a/b)
else:
    print("Invalid Choice")
            