A=int(input("please enter the first number: "))
B=int(input("please enter the second number: "))
OP=input("please enter the operater: ")
if OP=="+":
    print("the result is:",A+B)
elif OP=="-":
    print(" the result is:",A-B)
elif OP=="*":
    print("the resul is:",A*B)
elif OP=="/":
    print("the resul is:",A/B)
else:
    print("operator not found")
