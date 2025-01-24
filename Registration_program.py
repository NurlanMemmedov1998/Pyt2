print("""

***************************

Hesaba giris programi

***************************

""")


sys_username = "Nurlan"
sys_password = "Porsche33"
enter = 3

while True:
    username = input("UserName: ")
    password = input("Password: ")

    if username == sys_username and password != sys_password:
        print("Password isn't correct...")
        enter -= 1
    elif username != sys_username and password == sys_password:
        print("UserName isn't correct...")
        enter -= 1
    elif username != sys_username and password != sys_password:
        print("UserName and Password isn't correct...")
        enter -= 1
    else:
        print("Correct....")
        break

    if enter == 0:
        print("Enter time over....")
        break