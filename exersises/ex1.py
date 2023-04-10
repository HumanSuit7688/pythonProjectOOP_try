# Газировка

class Soda:
    def __init__(self, option):
        self.option = option

    def show_my_drink(self):
        if self.option:
            print(f'Газировка и {self.option}')
        else:
            print('Обычная газировка')

soda = Soda('Лимон')

soda.show_my_drink()

