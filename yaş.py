from datetime import datetime

def yas_hesapla(dogum_tarihi):
    # Şu anki tarih
    bugun = datetime.today()

    # Yaşı hesapla
    yas = bugun.year - dogum_tarihi.year

    # Ay ve günleri kontrol ederek tam yaşı hesapla
    if (bugun.month, bugun.day) < (dogum_tarihi.month, dogum_tarihi.day):
        yas -= 1

    return yas

# Doğum tarihini kullanıcıdan al
dogum_gunu = int(input("Doğum gününüzü girin (gün):13 "))
dogum_ayi = int(input("Doğum ayınızı girin (ay): april"))
dogum_yili = int(input("Doğum yılınızı girin (yıl):2007 "))

# Doğum tarihini datetime objesine çevir
dogum_tarihi = datetime(dogum_yili, dogum_ayi, dogum_gunu)

# Yaşı hesapla
yas = yas_hesapla(dogum_tarihi)

# Sonucu ekrana yazdır
print(f"Yaşınız: {yas}")
