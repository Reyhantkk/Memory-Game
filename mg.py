import random

def olustur_tahta(boyut):
    sayilar = list(range(1, boyut * 2 + 1))
    tahta = sayilar + sayilar
    random.shuffle(tahta)
    return [tahta[i:i+boyut] for i in range(0, len(tahta), boyut)]

def tahtayi_goster(tahta, acik=None):
    for satir in range(len(tahta)):
        for sutun in range(len(tahta[satir])):
            if acik and (satir, sutun) in acik:
                print(tahta[satir][sutun], end=' ')
            else:
                print('X', end=' ')
        print()

def oyunu_oyna(boyut):
    tahta = olustur_tahta(boyut)
    acik = []
    hamle_sayisi = 0

    while len(acik) < boyut * boyut:
        tahtayi_goster(tahta, acik)

        secim1 = input("İlk kartın konumunu girin (örn. 1,2): ")
        x1, y1 = map(int, secim1.split(','))
        secim2 = input("İkinci kartın konumunu girin (örn. 1,2): ")
        x2, y2 = map(int, secim2.split(','))

        if tahta[x1][y1] == tahta[x2][y2]:
            print("Eşleşme bulundu!")
            acik.append((x1, y1))
            acik.append((x2, y2))
        else:
            print("Eşleşme bulunamadı!")

        hamle_sayisi += 1

    print(f"Tebrikler! Oyunu {hamle_sayisi} hamlede tamamladınız.")

boyut = int(input("Tahtanın boyutunu girin (örn. 4 için 4x4'lük bir tahta oluşturulur): "))
oyunu_oyna(boyut)
