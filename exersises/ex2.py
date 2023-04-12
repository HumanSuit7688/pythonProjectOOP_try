class Triang:

    def __init__(self, a, b, c):
        self.first_site = a
        self.second_site = b
        self.third_site = c

    def is_Triang(self):
        result = ''
        if (type(self.first_site) == float or type(self.first_site) == int) and (type(self.second_site) == float or type(self.second_site) == int) and (type(self.third_site) == float or type(self.third_site) == int):
            if self.first_site != 0 and self.second_site != 0 and self.third_site != 0:
                sum12 = self.first_site + self.second_site
                sum23 = self.second_site + self.third_site
                sum13 = self.first_site + self.third_site
                if sum12 > self.third_site and sum23 > self.first_site and sum13 > self.second_site:
                    result = 'Ура можно построить треугольник!'
                else:
                    result = 'Нет, ты по моему перепутал, из этого треугольник не построить'
            else:
                result = 'Увы, но с отрицательными числами ничего не выйдет!'
        else:
            result = 'Нужно писать только цифы!!!'
        return result


Tr = Triang(5, 10, 12)
print(Tr.is_Triang())