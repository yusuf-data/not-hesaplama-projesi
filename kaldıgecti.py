not1 = int(input ("İlk sınav notun kaç?"))
not2 = int(input ("İkinci sınav notun kaç?"))
not3 = int(input ("Üçüncü sınav notun kaç?"))
ortalama = (not1 + not2 + not3) / 3
print("Ortalaman: " + str(ortalama))
if ortalama >= 50:
    print ("Sınıfı geçtin")
else:   print ("Sınıfta kaldın")