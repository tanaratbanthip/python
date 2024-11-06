userName = input("UserName: ")
passWord = input("Password: ")
if userName == "admin" and passWord == "123":
    print("Welcome")
    print("----My-Shop----")
    print("1. Vat calculator")
    print("2. Price calculator")
    userInput1 = input(">>")
    if userInput1 == "1":
        price = int(input("Price: "))
        vat = 7
        result = price+(price * vat)/100
        print(result)
    elif userInput1 == "2":
        price1 = int(input("Price1: "))
        price2 = int(input("price2: "))
        result = price1 + price2
        print(result)
else:
    print("Exit")
