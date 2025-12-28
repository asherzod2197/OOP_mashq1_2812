class Talaba:
    def __init__(self, ism, yosh, baho):
        self.ism = ism
        self.yosh = yosh
        self.baho = baho

    def malumot(self):
        return f"{self.ism} | Yosh: {self.yosh} | Baho: {self.baho}"


class TalabalarRoyxati:
    def __init__(self):
        self.talabalar = []

    def qoshish(self, talaba):
        self.talabalar.append(talaba)

    def chiqarish(self):
        for t in self.talabalar:
            print(t.malumot())

    def faylga_saqlash(self, nom="talabalar.txt"):
        with open(nom, "w", encoding="utf-8") as f:
            for t in self.talabalar:
                f.write(t.malumot() + "\n")

    def fayldan_oqish(self, nom="talabalar.txt"):
        try:
            with open(nom, "r", encoding="utf-8") as f:
                for qator in f:
                    print(qator.strip())
        except FileNotFoundError:
            print("Fayl topilmadi!")


royxat = TalabalarRoyxati()

royxat.qoshish(Talaba("Ali", 20, 85))
royxat.qoshish(Talaba("Vali", 22, 90))
royxat.qoshish(Talaba("Sardor", 19, 78))

print("Talabalar ro'yxati:")
royxat.chiqarish()

print("Faylga saqlandi.")
royxat.faylga_saqlash()

print("Fayldan o‘qildi:")
royxat.fayldan_oqish()
