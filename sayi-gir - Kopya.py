print("İki sayı girmeni istiyorum")

while True:
    try:
        print("1.Sayıyı Gir")
        say1 = int(input())
        print("2.Sayıyı Gir")
        say2 = int(input())
          
        
    except ValueError:
            print("Hatalı Giriş!")
            break
            
    islem = str(input("İşlem nedir? ( Toplama için (+), Çıkarma için (-), Çarpma için (*), Bölme için (/)"))

    if islem == "+":
        print("Sonuç", say1 + say2)
        break
    elif islem == "-":
        print("Sonuç", say1 - say2)
        break
    elif islem == "*":
        print("Sonuç", say1 * say2)
        break
    elif islem == "/":
        print("Sonuç", say1 / say2)
        break
    else:
        print("Hatalı Giriş")
        break