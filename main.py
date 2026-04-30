

class Avtomobil:
    def __init__(self, model, rang, yil, narx):
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx

    def get_age(self, current_year):
        return current_year - self.yil

    def get_info(self):
        return f"Model: {self.model}, Rang: {self.rang}, Yil: {self.yil}, Narx: {self.narx}"



car1 = Avtomobil("Chevrolet Malibu", "Qora", 2020, 25000)

print(car1.get_info())
print(car1.get_age(2025))






class Kitob:
    def __init__(self, nomi, muallif, sahifa_soni, narxi):
        self.nomi = nomi
        self.muallif = muallif
        self.sahifa_soni = sahifa_soni
        self.narxi = narxi

    def get_summary(self):
        return f"Kitob nomi: {self.nomi}, muallifi: {self.muallif}, {self.sahifa_soni} sahifadan iborat."

    def is_expensive(self, limit):
        if self.narxi > limit:
            return "Qimmat"
        else:
            return "Arzon"


kitob1 = Kitob("O‘tkan kunlar", "Abdulla Qodiriy", 300, 50000)

print(kitob1.get_summary())
print(kitob1.is_expensive(40000))
