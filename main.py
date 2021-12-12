from random import *
tahmin = ""
parol = input("Buziladigan parolni kiriting: ")
harflar = ["a","b","c","d","e","f","j","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","v","z"]
while(tahmin !=parol):
    tahmin = ""
    for harf in range(len(parol)):
       tahmin_harf=harflar[randint(0,25)]
       tahmin=str(tahmin_harf) + str(tahmin)
       print(tahmin)
print("parol muvaffiyaqatli buzildi")
tugatish = input(f"parol:<<{tahmin}>>dasturdan chiqish uchun istalgan tugmani bosing")