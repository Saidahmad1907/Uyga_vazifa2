class Soda:
    def __init__(self, fruit=None):
        self.fruit = fruit

    def show_my_drink(self):
        if self.fruit:
            print(f"Gazli suvga qo'shilgan meva: {self.fruit}")
        else:
            print("Oddiy gazli suv")


soda_with_lemon = Soda("Apelsin")
soda_with_lemon.show_my_drink()  

plain_soda = Soda()
plain_soda.show_my_drink()  