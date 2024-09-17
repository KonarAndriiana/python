num1 = float(input("Zadaj prve cislo:"))
num2 = float(input("Zadaj druhe cislo:"))
operator = input("Zadaj operator (+ - / *):")

if operator == "+":
    print(num1 , "+" , num2  ,"=" ,num1 + num2)
elif operator == "-":
    print(num1 , "-" , num2  ,"=" ,num1 - num2)
elif operator == "*":
    print(num1 , "*" , num2  ,"=" ,num1 * num2)
elif operator == "/":
    if num2 == 0:
        print("Nemozno delit nulou")
    else:
        print(num1 , "/" , num2  ,"=" ,num1 / num2)
else:
    print("Zly operator")

