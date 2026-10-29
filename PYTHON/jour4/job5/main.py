def calcule(num1,operator,num3):
    if operator == "+":
        return (num1+num3)
    elif operator == "-":
        return (num1-num3)
    elif operator == "*":
        return (num1*num3)
    elif operator == "%":
        return (num1%num3)
    elif operator == "/":
        return (num1/num3)

print(calcule(1,"+",4))
print(calcule(1,"*",5))
print(calcule(4, "-",2))
print(calcule(10,"%",5))
print(calcule(10,"/",5))
    

