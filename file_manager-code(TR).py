import os
import shutil

pr = print
AnaDizin = "C:\\Users\\admin\\Desktop\\python"

pr("Otomatik dosya yöneticisine hoş geldiniz!")

while True:
    pr("Mevcut dizin:", os.getcwd())
    işlem = input("Bir işlem seçin. (X = yeni dosya, Y = yeni klasör, Q = silme, HELP = diğer işlemler, EXIT = çıkış): ").strip().lower()

    if işlem == "exit":
        pr("Program sonlandırıldı. Görüşmek üzere!")
        break

    elif işlem == "x":
        dosya_adı = input("Yeni dosyanın adını (tam ad + uzantı) girin: ").strip()
        içerik_var_mı = input("İçerik eklemek istiyorsanız 1, istemiyorsanız 0 yazın: ").strip()

        if içerik_var_mı == "1":
            içerik = input("Dosya içeriğini girin: ")
            with open(dosya_adı, "w", encoding="utf-8") as f:
                f.write(içerik)
            pr(f"Dosya '{dosya_adı}' oluşturuldu (içerikli).")
        else:
            with open(dosya_adı, "w", encoding="utf-8") as f:
                f.write("")
            pr(f"Dosya '{dosya_adı}' oluşturuldu.")

    elif işlem == "y":
        klasor_adı = input("Yeni klasörün adını girin: ").strip()
        içerik_var_mı = input("Klasöre dosya oluşturmak istiyorsanız 1, istemiyorsanız 0 yazın: ").strip()

        os.mkdir(klasor_adı)
        pr(f"Klasör '{klasor_adı}' oluşturuldu.")

        if içerik_var_mı == "1":
            yeni_dizin = os.path.join(AnaDizin, klasor_adı)
            os.chdir(yeni_dizin)
            pr("Yeni dizine geçildi:", os.getcwd())

            dosya_adı = input("Yeni dosyanın adını (tam ad + uzantı) girin: ").strip()
            içerik_var_mı2 = input("İçerik eklemek istiyorsanız 1, istemiyorsanız 0 yazın: ").strip()

            if içerik_var_mı2 == "1":
                içerik = input("Dosya içeriğini girin: ")
                with open(dosya_adı, "w", encoding="utf-8") as f:
                    f.write(içerik)
                pr(f"Dosya '{dosya_adı}' oluşturuldu (içerikli).")
            else:
                with open(dosya_adı, "w", encoding="utf-8") as f:
                    f.write("")
                pr(f"Dosya '{dosya_adı}' oluşturuldu.")

    elif işlem == "q":
        hedef_türü = input("Dosya silmek için 1, klasör silmek için 2 yazın: ").strip()

        if hedef_türü == "1":
            dosya_adı = input("Silmek istediğiniz dosyanın tam ad + uzantısını girin: ").strip()
            os.remove(dosya_adı)
            pr(f"Dosya '{dosya_adı}' silindi.")

        elif hedef_türü == "2":
            klasor_adı = input("Silmek istediğiniz klasörün adını girin: ").strip()
            if os.path.isdir(klasor_adı):
                shutil.rmtree(klasor_adı)
                pr(f"Klasör '{klasor_adı}' ve içeriği silindi.")
            else:
                pr("Klasör bulunamadı veya zaten silinmiş.")

    elif işlem == "help":
        help_secim = input(
            "(1) Dosya ismi değiştirme\n"
            "(2) Mevcut dizini göster\n"
            "(3) Dosya aç\n"
            "(4) C:\\ kök dizine dön\n"
            "(5) Dosya var mı kontrol et\n"
            "(6) Dosya uzantısı değiştir\n"
            "(7) Dosya boyutu öğren\n"
            "(8) Kopyala ve yapıştır (yeniden adlandırma opsiyonlu)\n"
            "(9) Kes ve yapıştır\nSeçiminiz: "
        ).strip()

        if help_secim == "1":
            eski_ad = input("Dosyanın şu anki adını girin: ").strip()
            yeni_ad = input("Yeni adını (tam ad + uzantı) girin: ").strip()
            os.rename(eski_ad, yeni_ad)
            pr(f"Dosya adı '{eski_ad}' → '{yeni_ad}' olarak değiştirildi.")

        elif help_secim == "2":
            pr("Mevcut dizin:", os.getcwd())

        elif help_secim == "3":
            hedef_dosya = input("Açılacak dosyanın adını girin: ").strip()
            os.startfile(hedef_dosya)

        elif help_secim == "4":
            os.chdir("C:\\")
            pr("C:\\ kök dizinine dönüldü.")

        elif help_secim == "5":
            kontrol_dosya = input("Kontrol edilecek dosyanın adını girin: ").strip()
            if os.path.exists(kontrol_dosya):
                pr(f"Dosya '{kontrol_dosya}' mevcut.")
            else:
                pr("Dosya bulunamadı.")

        elif help_secim == "6":
            dosya_adı = input("Uzantısını değiştirmek istediğiniz dosyanın adını girin: ").strip()
            yeni_uzanti = input("Yeni uzantıyı girin (ör: .txt): ").strip()
            base = os.path.splitext(dosya_adı)[0]
            os.rename(dosya_adı, base + yeni_uzanti)
            pr(f"Dosya yeni adı: {base + yeni_uzanti}")

        elif help_secim == "7":
            dosya_adı = input("Boyutunu öğrenmek istediğiniz dosyanın adını girin: ").strip()
            boyut = os.path.getsize(dosya_adı)
            pr(f"Dosya boyutu: {boyut} bayt ({boyut / 1024:.2f} KB)")

        elif help_secim == "8":
            kaynak_dosya = input("Kopyalanacak dosyanın adını girin: ").strip()
            hedef_dizin = input("Hedef dizin (boş bırakılırsa mevcut dizin): ").strip()
            if not hedef_dizin:
                hedef_dizin = os.getcwd()
            yeni_ad = input("Yeni ad (aynı bırakmak için boş bırak): ").strip()
            if yeni_ad:
                hedef_yol = os.path.join(hedef_dizin, yeni_ad)
            else:
                hedef_yol = os.path.join(hedef_dizin, os.path.basename(kaynak_dosya))
            shutil.copy2(kaynak_dosya, hedef_yol)
            pr(f"Dosya '{kaynak_dosya}' '{hedef_yol}' konumuna kopyalandı.")

        elif help_secim == "9":
            kaynak_dosya = input("Taşınacak dosyanın adını girin: ").strip()
            hedef_dizin = input("Hedef dizin (boş bırakılırsa mevcut dizin): ").strip()
            if not hedef_dizin:
                hedef_dizin = os.getcwd()
            hedef_yol = os.path.join(hedef_dizin, os.path.basename(kaynak_dosya))
            shutil.move(kaynak_dosya, hedef_yol)
            pr(f"Dosya '{kaynak_dosya}' '{hedef_yol}' konumuna taşındı.")

        else:
            pr("Geçersiz seçim.")

    else:
        pr("Geçersiz işlem. Lütfen tekrar deneyin.")
