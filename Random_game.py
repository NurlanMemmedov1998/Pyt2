print("""
***********************************
Təxmin etmə oyununa xoş Gəlmisiniz..
***********************************
""")


import random
import time

Random_num = random.randint(1,40)

texmin_sayi = 5

while True:
    sayi = int(input("Rəqəm təxminizi girin: "))

    if (sayi < Random_num):
        print("Hesablanır...")
        time.sleep(1)
        print("Daha yüksək rəqəm girin.")
        texmin_sayi -= 1
    elif (sayi > Random_num):
        print("Hesablanır...")
        time.sleep(1)
        print("Daha aşağı rəqəm girin.")
        texmin_sayi -= 1
    else:
        print("Hesablanır...")
        time.sleep(1)
        print("Təbriklər cavab doğrudur. Cavab: ", Random_num)
        break
    if (texmin_sayi == 0):
        print("Təxmin etmə sayınız bitti. Şansınızı bir daha sınayın.")
        break