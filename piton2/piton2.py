sayi1=10
sayi2=20
toplam= sayi1 + sayi2
print(toplam)
isimkullanici = input ("Adın nedir ?")
print("Mirhaba", isimkullanici)
sayi = int(input("Bir sayı değeri"))
kare = sayi*sayi
print("Sayının karesi", kare)
sayitekcift = int(input("Bir sayı değeri gir"))
if sayitekcift % 2 == 0:
    print("çift")
else:
    print("tek")
    asalsayi = int(input("Asal olup olmadığını bulmak için sayı gir"))
    if asalsayi < 2:
        print ("Asal değil")
    else:
        asal = True
        for i in range(2, sayi):
            if sayi%i == 0:
                asal = False
                break 
            if asal:
                print("Asal")
            else:
                print("Asal değil")