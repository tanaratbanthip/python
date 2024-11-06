userName = input("UserName: ")
passWord = input("Password: ")

if userName == "admin" and passWord == "123":
    print("Welcome-To-My-Shop-")
    print("รายการสินค้า")
    print("1. นม ราคา 10 บาท")
    print("2. น้ำ ราคา 8 บาท")
    print("3. ลูกอม ราคา 20 บาท")

    milk_price = 10
    water_price = 8
    candy_price = 20

    total = 0

    print("เลือกรายการสินค้า (1-3)")
    select = int(input("เลือกสินค้าที่ต้องการซื้อ: "))

    if select == 1:
        quantity = int(input("จำนวน: "))
        total += milk_price * quantity
    elif select == 2:
        quantity = int(input("จำนวน: "))
        total += water_price * quantity
    elif select == 3:
        quantity = int(input("จำนวน: "))
        total += candy_price * quantity
    else:
        print("เลือกสินค้าไม่ถูกต้อง")

    print("ยอดรวมทั้งหมด:",total, "บาท")
else:
    print("ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
