import random

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from kivy.clock import Clock


# =========================================================
# PENCERE
# =========================================================

Window.clearcolor = (0.94, 0.97, 1, 1)


# =========================================================
# KONULAR
# =========================================================

KONULAR = [
    "Toplama İşlemi Problemleri",
    "Çıkarma İşlemi Problemleri",
    "Toplama ve Çıkarma İşlemi Problemleri",
    "Toplama İşleminin Sonucunu Tahmin Etme",
    "Çıkarma İşleminin Sonucunu Tahmin Etme",
    "Toplama ve Çıkarma Sonuçlarını Tahmin Etme",
    "Zihinden Toplama ve Çıkarma İşlemleri",
    "Toplama ve Çıkarma İşlemlerinin İlişkisi",
    "Çarpma İşlemi Problemleri",
    "Bölme İşlemi Problemleri",
    "Çarpma ve Bölme Sonuçlarını Muhakeme Etme",
    "Zihinden Çarpma ve Bölme İşlemleri",
    "Eşitlik ile İlgili Problemler",
    "Dört İşlem Problemleri"
]


# =========================================================
# BUTON
# =========================================================

class RenkliButon(Button):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.background_normal = ""
        self.background_down = ""

        self.background_color = (
            0.12, 0.55, 0.88, 1
        )

        self.color = (
            1, 1, 1, 1
        )

        self.font_size = "18sp"
        self.bold = True

        self.size_hint_y = None
        self.height = 65


# =========================================================
# SORU KARTI
# =========================================================

class SoruKarti(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.padding = 20

        with self.canvas.before:
            Color(
                0.88, 0.94, 1, 1
            )

            self.arka_plan = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[18]
            )

        self.bind(
            pos=self.guncelle,
            size=self.guncelle
        )

    def guncelle(self, *args):
        self.arka_plan.pos = self.pos
        self.arka_plan.size = self.size


# =========================================================
# ANA SAYFA
# =========================================================

class AnaSayfa(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        ana = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        baslik = Label(
            text="MATEMATİK MACERASI",
            font_size="32sp",
            bold=True,
            color=(0.05, 0.30, 0.65, 1),
            size_hint_y=None,
            height=60
        )

        ana.add_widget(baslik)

        alt = Label(
            text="2. Sınıf Matematik Testleri",
            font_size="21sp",
            color=(0.15, 0.20, 0.30, 1),
            size_hint_y=None,
            height=40
        )

        ana.add_widget(alt)

        bilgi = Label(
            text="Bir konu seç ve matematik macerana başla!",
            font_size="17sp",
            color=(0.25, 0.30, 0.40, 1),
            size_hint_y=None,
            height=40
        )

        ana.add_widget(bilgi)

        scroll = ScrollView(
            do_scroll_x=False
        )

        liste = GridLayout(
            cols=1,
            spacing=9,
            padding=5,
            size_hint_y=None
        )

        liste.bind(
            minimum_height=liste.setter("height")
        )

        for i, konu in enumerate(KONULAR):

            buton = RenkliButon(
                text=f"{i + 1}. {konu}"
            )

            buton.bind(
                on_press=lambda instance,
                num=i: self.konu_sec(num)
            )

            liste.add_widget(buton)

        scroll.add_widget(liste)

        ana.add_widget(scroll)

        self.add_widget(ana)

    def konu_sec(self, numara):

        konu_ekrani = self.manager.get_screen(
            "konu"
        )

        konu_ekrani.konu_goster(numara)

        self.manager.current = "konu"


# =========================================================
# KONU EKRANI
# =========================================================

class KonuSayfasi(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.konu_numarasi = 0

        ana = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=20
        )

        self.baslik = Label(
            text="",
            font_size="28sp",
            bold=True,
            color=(0.05, 0.30, 0.65, 1),
            size_hint_y=None,
            height=100
        )

        ana.add_widget(self.baslik)

        self.bilgi = Label(
            text="",
            font_size="20sp",
            color=(0.15, 0.20, 0.30, 1)
        )

        ana.add_widget(self.bilgi)

        basla = RenkliButon(
            text="TESTE BAŞLA"
        )

        basla.background_color = (
            0.08, 0.65, 0.35, 1
        )

        basla.bind(
            on_press=self.test_baslat
        )

        ana.add_widget(basla)

        geri = RenkliButon(
            text="ANA SAYFAYA DÖN"
        )

        geri.background_color = (
            0.45, 0.50, 0.55, 1
        )

        geri.bind(
            on_press=lambda x:
            setattr(
                self.manager,
                "current",
                "ana"
            )
        )

        ana.add_widget(geri)

        self.add_widget(ana)

    def konu_goster(self, numara):

        self.konu_numarasi = numara

        self.baslik.text = (
            f"{numara + 1}. {KONULAR[numara]}"
        )

        self.bilgi.text = (
            "10 soruluk test\n\n"
            "Her testte sorular ve sayılar "
            "yeniden oluşturulur."
        )

    def test_baslat(self, instance):

        test = self.manager.get_screen(
            "test"
        )

        test.test_baslat(
            self.konu_numarasi
        )

        self.manager.current = "test"


# =========================================================
# TEST EKRANI
# =========================================================

class TestEkrani(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.konu = 0
        self.sorular = []
        self.soru_no = 0
        self.dogru = 0
        self.cevaplar = []

        ana = BoxLayout(
            orientation="vertical",
            padding=25,
            spacing=12
        )

        self.baslik = Label(
            text="",
            font_size="24sp",
            bold=True,
            color=(0.05, 0.30, 0.65, 1),
            size_hint_y=None,
            height=45
        )

        ana.add_widget(self.baslik)

        self.soru_sayaci = Label(
            text="",
            font_size="22sp",
            bold=True,
            color=(0.05, 0.35, 0.75, 1),
            size_hint_y=None,
            height=45
        )

        ana.add_widget(self.soru_sayaci)

        self.soru_karti = SoruKarti(
            orientation="vertical",
            size_hint_y=None,
            height=190
        )

        self.soru_metni = Label(
            text="",
            font_size="22sp",
            bold=True,
            color=(0.05, 0.12, 0.25, 1),
            halign="center",
            valign="middle"
        )

        self.soru_metni.bind(
            size=lambda instance, value:
            setattr(
                instance,
                "text_size",
                value
            )
        )

        self.soru_karti.add_widget(
            self.soru_metni
        )

        ana.add_widget(
            self.soru_karti
        )

        self.secenekler = GridLayout(
            cols=1,
            spacing=10,
            size_hint_y=None
        )

        self.secenekler.bind(
            minimum_height=
            self.secenekler.setter("height")
        )

        ana.add_widget(
            self.secenekler
        )

        self.sonuc = Label(
            text="",
            font_size="20sp",
            bold=True,
            size_hint_y=None,
            height=40
        )

        ana.add_widget(self.sonuc)

        self.add_widget(ana)

    # =====================================================
    # TEST BAŞLAT
    # =====================================================

    def test_baslat(self, konu):

        self.konu = konu
        self.soru_no = 0
        self.dogru = 0
        self.cevaplar = []

        self.baslik.text = (
            KONULAR[konu]
        )

        self.sorular = []

        kullanilan = set()

        while len(self.sorular) < 10:

            soru = self.soru_uret(konu)

            if soru["soru"] not in kullanilan:

                kullanilan.add(
                    soru["soru"]
                )

                self.sorular.append(
                    soru
                )

        self.soru_goster()

    # =====================================================
    # SORU ÜRETİCİ
    # =====================================================

    def soru_uret(self, konu):

        if konu == 0:
            return self.toplama_problemi()

        if konu == 1:
            return self.cikarma_problemi()

        if konu == 2:
            return self.toplama_cikarma()

        if konu == 3:
            return self.toplama_tahmin()

        if konu == 4:
            return self.cikarma_tahmin()

        if konu == 5:
            return self.toplama_cikarma_tahmin()

        if konu == 6:
            return self.zihinden_toplama_cikarma()

        if konu == 7:
            return self.islem_iliskisi()

        if konu == 8:
            return self.carpma_problemi()

        if konu == 9:
            return self.bolme_problemi()

        if konu == 10:
            return self.carpma_bolme_muhakeme()

        if konu == 11:
            return self.zihinden_carpma_bolme()

        if konu == 12:
            return self.esitlik()

        if konu == 13:
            return self.dort_islem()

    # =====================================================
    # SEÇENEK OLUŞTUR
    # =====================================================

    def secenek_olustur(self, dogru):

        secenekler = {dogru}

        while len(secenekler) < 4:

            fark = random.randint(1, 10)

            if random.choice([True, False]):
                yeni = dogru + fark
            else:
                yeni = dogru - fark

            if yeni >= 0:
                secenekler.add(yeni)

        secenekler = list(secenekler)

        random.shuffle(secenekler)

        dogru_index = secenekler.index(
            dogru
        )

        return secenekler, dogru_index

    # =====================================================
    # 1 - TOPLAMA
    # =====================================================

    def toplama_problemi(self):

        a = random.randint(15, 70)
        b = random.randint(10, 29)

        cevap = a + b

        soru = (
            f"Ali'nin {a} tane bilyesi vardı. "
            f"Babası ona {b} bilye daha verdi. "
            f"Ali'nin kaç bilyesi oldu?"
        )

        secenek, dogru = self.secenek_olustur(
            cevap
        )

        return {
            "soru": soru,
            "secenekler": secenek,
            "cevap": dogru
        }

    # =====================================================
    # 2 - ÇIKARMA
    # =====================================================

    def cikarma_problemi(self):

        a = random.randint(30, 90)
        b = random.randint(10, a - 5)

        cevap = a - b

        soru = (
            f"Zeynep'in {a} tane kalemi vardı. "
            f"{b} tanesini arkadaşına verdi. "
            f"Kaç kalemi kaldı?"
        )

        secenek, dogru = self.secenek_olustur(
            cevap
        )

        return {
            "soru": soru,
            "secenekler": secenek,
            "cevap": dogru
        }

    # =====================================================
    # 3 - TOPLAMA VE ÇIKARMA
    # =====================================================

    def toplama_cikarma(self):

        a = random.randint(30, 70)
        b = random.randint(10, 25)
        c = random.randint(5, 20)

        cevap = a + b - c

        soru = (
            f"Bir sepette {a} elma vardı. "
            f"Sepete {b} elma daha konuldu. "
            f"Sonra {c} elma alındı. "
            f"Sepette kaç elma kaldı?"
        )

        secenek, dogru = self.secenek_olustur(
            cevap
        )

        return {
            "soru": soru,
            "secenekler": secenek,
            "cevap": dogru
        }

    # =====================================================
    # 4 - TOPLAMA TAHMİN
    # =====================================================

    def toplama_tahmin(self):

        a = random.randrange(10, 91, 10) + random.randint(0, 9)
        b = random.randrange(10, 91, 10) + random.randint(0, 9)

        tahmin = (
            round(a / 10) * 10 +
            round(b / 10) * 10
        )

        soru = (
            f"{a} + {b} işleminin sonucunu "
            f"en yakın onluğa yuvarlayarak "
            f"tahmin edersek kaç buluruz?"
        )

        secenek, dogru = self.secenek_olustur(
            tahmin
        )

        return {
            "soru": soru,
            "secenekler": secenek,
            "cevap": dogru
        }

    # =====================================================
    # 5 - ÇIKARMA TAHMİN
    # =====================================================

    def cikarma_tahmin(self):

        a = random.randrange(30, 100, 10) + random.randint(0, 9)
        b = random.randrange(10, a, 10) + random.randint(0, 9)

        if b >= a:
            b = a - 5

        tahmin = (
            round(a / 10) * 10 -
            round(b / 10) * 10
        )

        soru = (
            f"{a} - {b} işleminin sonucunu "
            f"en yakın onluğa yuvarlayarak "
            f"tahmin edersek kaç buluruz?"
        )

        secenek, dogru = self.secenek_olustur(
            tahmin
        )

        return {
            "soru": soru,
            "secenekler": secenek,
            "cevap": dogru
        }

    # =====================================================
    # 6 - TOPLAMA + ÇIKARMA TAHMİN
    # =====================================================

    def toplama_cikarma_tahmin(self):

        a = random.randint(20, 60)
        b = random.randint(10, 30)
        c = random.randint(5, 20)

        tahmin = (
            round(a / 10) * 10 +
            round(b / 10) * 10 -
            round(c / 10) * 10
        )

        soru = (
            f"{a} + {b} - {c} işleminin "
            f"sonucunu en yakın onluğa "
            f"yuvarlayarak tahmin edersek "
            f"kaç buluruz?"
        )

        secenek, dogru = self.secenek_olustur(
            tahmin
        )

        return {
            "soru": soru,
            "secenekler": secenek,
            "cevap": dogru
        }

    # =====================================================
    # 7 - ZİHİNDEN TOPLAMA / ÇIKARMA
    # =====================================================

    def zihinden_toplama_cikarma(self):

        a = random.choice(
            [20, 30, 40, 50, 60, 70]
        )

        b = random.choice(
            [5, 10, 15, 20]
        )

        if random.choice([True, False]):

            cevap = a + b

            soru = (
                f"Zihinden {a} + {b} işlemini "
                f"yaparsak sonuç kaç olur?"
            )

        else:

            cevap = a - b

            soru = (
                f"Zihinden {a} - {b} işlemini "
                f"yaparsak sonuç kaç olur?"
            )

        secenek, dogru = self.secenek_olustur(
            cevap
        )

        return {
            "soru": soru,
            "secenekler": secenek,
            "cevap": dogru
        }

    # =====================================================
    # 8 - İŞLEMLERİN İLİŞKİSİ
    # =====================================================

    def islem_iliskisi(self):

        a = random.randint(20, 70)
        b = random.randint(5, 20)

        toplam = a + b

        soru = (
            f"{a} + {b} = {toplam} olduğuna göre "
            f"{toplam} - {b} işleminin sonucu kaçtır?"
        )

        cevap = a

        secenek, dogru = self.secenek_olustur(
            cevap
        )

        return {
            "soru": soru,
            "secenekler": secenek,
            "cevap": dogru
        }

    # =====================================================
    # 9 - ÇARPMA
    # =====================================================

    def carpma_problemi(self):

        grup = random.randint(2, 8)
        adet = random.randint(2, 10)

        cevap = grup * adet

        soru = (
            f"Her kutuda {adet} kalem vardır. "
            f"{grup} kutuda toplam kaç kalem vardır?"
        )

        secenek, dogru = self.secenek_olustur(
            cevap
        )

        return {
            "soru": soru,
            "secenekler": secenek,
            "cevap": dogru
        }

    # =====================================================
    # 10 - BÖLME
    # =====================================================

    def bolme_problemi(self):

        grup = random.randint(2, 9)
        kisi = random.randint(2, 6)

        toplam = grup * kisi

        soru = (
            f"{toplam} şeker {kisi} çocuğa "
            f"eşit olarak paylaştırılıyor. "
            f"Her çocuk kaç şeker alır?"
        )

        cevap = grup

        secenek, dogru = self.secenek_olustur(
            cevap
        )

        return {
            "soru": soru,
            "secenekler": secenek,
            "cevap": dogru
        }

    # =====================================================
    # 11 - ÇARPMA / BÖLME MUHAKEME
    # =====================================================

    def carpma_bolme_muhakeme(self):

        adet = random.randint(2, 8)
        grup = random.randint(2, 6)

        toplam = adet * grup

        if random.choice([True, False]):

            soru = (
                f"{grup} grubun her birinde "
                f"{adet} çocuk vardır. "
                f"Toplam kaç çocuk vardır?"
            )

            cevap = toplam

        else:

            soru = (
                f"{toplam} top, {grup} kutuya "
                f"eşit olarak konuluyor. "
                f"Her kutuya kaç top konur?"
            )

            cevap = adet

        secenek, dogru = self.secenek_olustur(
            cevap
        )

        return {
            "soru": soru,
            "secenekler": secenek,
            "cevap": dogru
        }

    # =====================================================
    # 12 - ZİHİNDEN ÇARPMA / BÖLME
    # =====================================================

    def zihinden_carpma_bolme(self):

        sayi = random.randint(2, 9)
        katsayi = random.choice(
            [2, 3, 4, 5, 10]
        )

        toplam = sayi * katsayi

        if random.choice([True, False]):

            soru = (
                f"Zihinden {sayi} x {katsayi} "
                f"işlemini yaparsak sonuç kaç olur?"
            )

            cevap = toplam

        else:

            soru = (
                f"Zihinden {toplam} ÷ {katsayi} "
                f"işlemini yaparsak sonuç kaç olur?"
            )

            cevap = sayi

        secenek, dogru = self.secenek_olustur(
            cevap
        )

        return {
            "soru": soru,
            "secenekler": secenek,
            "cevap": dogru
        }

    # =====================================================
    # 13 - EŞİTLİK
    # =====================================================

    def esitlik(self):

        a = random.randint(10, 40)
        b = random.randint(5, 20)

        cevap = a - b

        soru = (
            f"{b} + □ = {a} "
            f"eşitliğinde □ yerine hangi sayı "
            f"gelmelidir?"
        )

        secenek, dogru = self.secenek_olustur(
            cevap
        )

        return {
            "soru": soru,
            "secenekler": secenek,
            "cevap": dogru
        }

    # =====================================================
    # 14 - DÖRT İŞLEM
    # =====================================================

    def dort_islem(self):

        secim = random.randint(1, 4)

        if secim == 1:

            a = random.randint(20, 60)
            b = random.randint(10, 30)

            cevap = a + b

            soru = (
                f"{a} + {b} işleminin sonucu kaçtır?"
            )

        elif secim == 2:

            a = random.randint(30, 90)
            b = random.randint(10, a - 5)

            cevap = a - b

            soru = (
                f"{a} - {b} işleminin sonucu kaçtır?"
            )

        elif secim == 3:

            a = random.randint(2, 8)
            b = random.randint(2, 6)

            cevap = a * b

            soru = (
                f"{a} x {b} işleminin sonucu kaçtır?"
            )

        else:

            b = random.randint(2, 6)
            cevap = random.randint(2, 9)
            a = b * cevap

            soru = (
                f"{a} ÷ {b} işleminin sonucu kaçtır?"
            )

        secenek, dogru = self.secenek_olustur(
            cevap
        )

        return {
            "soru": soru,
            "secenekler": secenek,
            "cevap": dogru
        }

    # =====================================================
    # SORUYU GÖSTER
    # =====================================================

    def soru_goster(self):

        soru = self.sorular[
            self.soru_no
        ]

        self.soru_sayaci.text = (
            f"Soru {self.soru_no + 1} / 10"
        )

        self.soru_metni.text = soru["soru"]

        self.sonuc.text = ""

        self.secenekler.clear_widgets()

        harfler = ["A", "B", "C", "D"]

        for i, secenek in enumerate(
            soru["secenekler"]
        ):

            buton = RenkliButon(
                text=f"{harfler[i]}) {secenek}"
            )

            buton.bind(
                on_press=lambda instance,
                num=i:
                self.cevap_ver(num)
            )

            self.secenekler.add_widget(
                buton
            )

    # =====================================================
    # CEVAP VER
    # =====================================================

    def cevap_ver(self, secenek):

        soru = self.sorular[
            self.soru_no
        ]

        dogru = soru["cevap"]

        self.cevaplar.append(
            secenek
        )

        if secenek == dogru:

            self.dogru += 1

            self.sonuc.text = "✅ DOĞRU!"

            self.sonuc.color = (
                0.05, 0.60, 0.25, 1
            )

        else:

            self.sonuc.text = "❌ YANLIŞ!"

            self.sonuc.color = (
                0.85, 0.12, 0.12, 1
            )

        for buton in self.secenekler.children:
            buton.disabled = True

        Clock.schedule_once(
            self.sonraki,
            0.7
        )

    # =====================================================
    # SONRAKİ SORU
    # =====================================================

    def sonraki(self, dt):

        self.soru_no += 1

        if self.soru_no >= 10:

            sonuc = self.manager.get_screen(
                "sonuc"
            )

            sonuc.sonuc_goster(
                self.dogru,
                self.sorular,
                self.cevaplar
            )

            self.manager.current = "sonuc"

        else:

            self.soru_goster()


# =========================================================
# SONUÇ EKRANI
# =========================================================

class SonucEkrani(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.sorular = []
        self.cevaplar = []
        self.dogru = 0

        ana = BoxLayout(
            orientation="vertical",
            padding=30,
            spacing=20
        )

        baslik = Label(
            text="🎉 TEST TAMAMLANDI!",
            font_size="30sp",
            bold=True,
            color=(0.05, 0.55, 0.30, 1),
            size_hint_y=None,
            height=70
        )

        ana.add_widget(baslik)

        self.puan = Label(
            text="",
            font_size="28sp",
            bold=True,
            color=(0.05, 0.30, 0.65, 1)
        )

        ana.add_widget(self.puan)

        self.mesaj = Label(
            text="",
            font_size="21sp",
            color=(0.15, 0.20, 0.30, 1)
        )

        ana.add_widget(self.mesaj)

        cevap = RenkliButon(
            text="🔐 CEVAP ANAHTARI"
        )

        cevap.background_color = (
            0.60, 0.35, 0.75, 1
        )

        cevap.bind(
            on_press=self.sifre_sor
        )

        ana.add_widget(cevap)

        tekrar = RenkliButon(
            text="🔄 AYNI KONUYU TEKRAR ÇÖZ"
        )

        tekrar.background_color = (
            0.08, 0.65, 0.35, 1
        )

        tekrar.bind(
            on_press=self.tekrar
        )

        ana.add_widget(tekrar)

        menu = RenkliButon(
            text="ANA MENÜYE DÖN"
        )

        menu.background_color = (
            0.45, 0.50, 0.55, 1
        )

        menu.bind(
            on_press=lambda x:
            setattr(
                self.manager,
                "current",
                "ana"
            )
        )

        ana.add_widget(menu)

        self.add_widget(ana)

    # =====================================================
    # SONUÇ
    # =====================================================

    def sonuc_goster(
        self,
        dogru,
        sorular,
        cevaplar
    ):

        self.dogru = dogru
        self.sorular = sorular
        self.cevaplar = cevaplar

        puan = dogru * 10

        self.puan.text = (
            f"{dogru} / 10 DOĞRU\n"
            f"PUAN: {puan}"
        )

        if dogru == 10:

            self.mesaj.text = (
                "🏆 MÜKEMMEL!\n"
                "Bütün soruları doğru yaptın!"
            )

        elif dogru >= 8:

            self.mesaj.text = (
                "⭐ ÇOK İYİ!\n"
                "Harika gidiyorsun!"
            )

        elif dogru >= 5:

            self.mesaj.text = (
                "👍 GÜZEL!\n"
                "Biraz daha çalışırsan daha iyi olacak."
            )

        else:

            self.mesaj.text = (
                "💪 TEKRAR DENE!\n"
                "Pes etme, tekrar başarabilirsin!"
            )

    # =====================================================
    # TEKRAR
    # =====================================================

    def tekrar(self, instance):

        test = self.manager.get_screen(
            "test"
        )

        test.test_baslat(
            test.konu
        )

        self.manager.current = "test"

    # =====================================================
    # ŞİFRE
    # =====================================================

    def sifre_sor(self, instance):

        kutu = BoxLayout(
            orientation="vertical",
            padding=15,
            spacing=15
        )

        bilgi = Label(
            text="Cevap anahtarını görmek için şifreyi girin.",
            font_size="17sp"
        )

        kutu.add_widget(bilgi)

        sifre = TextInput(
            password=True,
            multiline=False,
            font_size="20sp",
            size_hint_y=None,
            height=50
        )

        kutu.add_widget(sifre)

        kontrol = RenkliButon(
            text="GÖSTER"
        )

        kutu.add_widget(kontrol)

        popup = Popup(
            title="🔐 Cevap Anahtarı",
            content=kutu,
            size_hint=(0.85, 0.55)
        )

        def kontrol_et(instance):

            # ŞİFRE BURADA
            if sifre.text == "2026":

                popup.dismiss()

                self.cevap_anahtarini_goster()

            else:

                bilgi.text = (
                    "❌ Şifre yanlış. Tekrar deneyin."
                )

        kontrol.bind(
            on_press=kontrol_et
        )

        popup.open()

    # =====================================================
    # CEVAP ANAHTARI
    # =====================================================

    def cevap_anahtarini_goster(self):

        harfler = [
            "A",
            "B",
            "C",
            "D"
        ]

        metin = ""

        for i, soru in enumerate(
            self.sorular
        ):

            dogru = soru["cevap"]
            verilen = self.cevaplar[i]

            metin += (
                f"{i + 1}. soru → "
                f"Doğru: {harfler[dogru]}"
            )

            if verilen == dogru:

                metin += "  ✅"

            else:

                metin += (
                    f"  ❌ Senin cevabın: "
                    f"{harfler[verilen]}"
                )

            metin += "\n\n"

        kutu = BoxLayout(
            orientation="vertical",
            padding=15
        )

        scroll = ScrollView(
            do_scroll_x=False
        )

        cevap_label = Label(
            text=metin,
            font_size="17sp",
            halign="left",
            valign="top",
            size_hint_y=None
        )

        cevap_label.bind(
            texture_size=lambda instance, value:
            setattr(
                instance,
                "height",
                value[1]
            )
        )

        scroll.add_widget(
            cevap_label
        )

        kutu.add_widget(scroll)

        kapat = RenkliButon(
            text="KAPAT"
        )

        kutu.add_widget(kapat)

        popup = Popup(
            title="🔐 Cevap Anahtarı",
            content=kutu,
            size_hint=(0.9, 0.85)
        )

        kapat.bind(
            on_press=popup.dismiss
        )

        popup.open()


# =========================================================
# UYGULAMA
# =========================================================

class MatematikMacerasi(App):

    def build(self):

        self.title = "Matematik Macerası"

        ekranlar = ScreenManager()

        ekranlar.add_widget(
            AnaSayfa(name="ana")
        )

        ekranlar.add_widget(
            KonuSayfasi(name="konu")
        )

        ekranlar.add_widget(
            TestEkrani(name="test")
        )

        ekranlar.add_widget(
            SonucEkrani(name="sonuc")
        )

        return ekranlar


# =========================================================
# BAŞLAT
# =========================================================

if __name__ == "__main__":
    MatematikMacerasi().run()