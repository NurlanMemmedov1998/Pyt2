def calculator():

    try:
        print("Birinci reqemi giriniz: ")
        a = float(input())
    except ValueError:
        print("Reqem giriniz")
        print("Birinci reqemi giriniz: ")
        a = float(input())

    try:
        print("Ikinci reqemi giriniz: ")
        b = float(input())
    except ValueError:
        print("Reqem giriniz")
        print("Ikinci reqemi giriniz: ")
        b = float(input())

    try:
        print("Hesab emelini giriniz: ", "+", "-", "*", "/")
        c = input()
    except ValueError:
        print("Zehmet olmasa 4 hesabdan birini giriniz")

    if c == "+":
        print("Cavab: ", a+b)
    elif c == "-":
        print("Cavab: ", a-b)
    elif c == "*":
        print("Cavab: ", a*b)
    elif c == "/":
        print("Cavab: ", a/b)

calculator()