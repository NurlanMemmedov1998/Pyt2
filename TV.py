import random
import time

class Kumanda():
    def __init__(self, tv_durum = "Kapalı", tv_ses = 0, kanal_listesi = ["Trt"], kanal = "Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def tv_ac(self):
        if (self.tv_durum == "Acik"):
            print("Televiziyon zaten acik")
        else:
            print("Televiziyon aciliyor...")
            self.tv_durum = "Acik"

    def tv_kapat(self):
        if (self.tv_durum == "Kapali"):
            print("Televiziyon zaten kapali")
        else:
            print("Televiziyon kapaniyor...")
            self.tv_durum = "Kapali"

    def ses_ayarlari(self):

        while True:
            cavab = input("Sesi azalt: '<'\nSesi artir: '>'\nCikis: Exit.")

            if (cavab == "<"):

                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses: ",self.tv_ses)

            elif (cavab == ">"):

                if (self.tv_ses != 31):
                    self.tv_ses += 1

                    print("Ses: ",self.tv_ses)

            else:
                print("Ses Guncellendi.", self.tv_ses)
                break
    def kanal_ekle(self, kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)

        self.kanal_listesi.append(kanal_ismi)

        print("Kanal eklendi.")
    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]

        print("Su anki kanal: ", self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv Durumu: {}\nTv ses {}\nKananl listesi: {}\nSu anki kanal: {}\n".format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal)

kumanda = Kumanda()
print("""
Televizyon uygulamasi

1. Tv ac
2. Tv kapat
3. Ses ayarlari 
4. Kanal ekle
5. Kanal sayisi
6. Rastgele kanal
7. Tv bilgileri

Cikmak icin "q" -ye basin
""")

while True:
    islem = input("Islemi secin: ")
    if (islem == "q"):
        print("Tv kapatiliyor...")
        time.sleep(2)
        break
    elif (islem == "1"):
        kumanda.tv_ac()
    elif (islem == "2"):
        kumanda.tv_kapat()

    elif (islem == "3"):
        kumanda.ses_ayarlari()
    elif (islem == "4"):
        kanal_isimleri = input("Kanal isimleri girin: ")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (islem == "5"):
        print("Kanal sayisi:", len(kumanda))
    elif (islem == "6"):
        kumanda.rastgele_kanal()
    elif (islem =="7"):
        print(kumanda)
    else:
        print("Gecersiz islem")





















