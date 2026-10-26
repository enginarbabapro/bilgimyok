
print("Toplama için 1")
print("Çıkarma için 2")
print("Çarpma için 3")
print("Bölme için 4")

secim = input("Lütfen yapmak istediğiniz işlemi seçiniz: ")

sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))

if secim == '1':
    sonuc = sayi1 + sayi2
    print("Sonuç:", sonuc)

elif secim == '2':
    sonuc = sayi1 - sayi2
    print("Sonuç:", sonuc)

elif secim == '3':
    sonuc = sayi1 * sayi2
    print("Sonuç:", sonuc)

elif secim == '4':
    if sayi2 != 0:
        sonuc = sayi1 / sayi2
        print("Sonuç:", sonuc)
    else:
        print("Hata: Bir sayıyı sıfıra bölemezsiniz.")

else:
    print("Hata: Geçersiz işlem seçtiniz.")