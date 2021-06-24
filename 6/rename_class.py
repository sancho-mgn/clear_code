"""было"""
from typing import List


class Sport:
    def __init__(self, number=0, name="E", surname="D", country="F", weidth=100, types="G"):
        self.number = number
        self.name = name
        self.surname = surname
        self.country = country
        self.weidth = weidth
        self.types = types

    def set_number(self, new_number):
        self.number = new_number

    def get_number(self):
        return self.number

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_surname(self, new_surname):
        self.surname = new_surname

    def get_surname(self):
        return self.surname

    def set_country(self, new_country):
        self.country = new_country

    def get_country(self):
        return self.country

    def set_weidth(self, new_weidth):
        self.weidth = new_weidth

    def get_weidth(self):
        return self.weidth

    def set_type(self, new_type):
        self.types = new_type

    def get_type(self):
        return self.types

#list_s = [[1, "Ivan", "Ivanov", "Russia", 180, "Foot"],[2, "Igor", "Fedin", "India", 199, "Basket"]]
#x = Sport(*list_s)
def autofill(files):
    lst_x = []
    with open(files, "rt") as sp:
        list_s = [line.split() for line in sp]
        print(list_s)
        for j in range(len(list_s)):
            x = Sport()
            for i in range(len(list_s[j])):
                if i == 0:
                    try:
                        x.set_number(list_s[j][i])
                    except ValueError:
                        raise ValueError("В строке № " + str(i) + " не верно введен аргемунт № " + str(j) + " номер игрока!")
                elif i == 1:
                    try:
                        x.set_name(list_s[j][i])
                    except ValueError:
                        raise ValueError("В строке №" + str(i) + "не верно введен аргемунт № " + str(j) +  " имя игрока!")
                elif i == 2:
                    try:
                        x.set_surname(list_s[j][i])
                    except ValueError:
                        raise ValueError("В строке №" + str(i) + "не верно введен аргемунт № " + str(j) +  " фамилия игрока!")
                elif i == 3:
                    try:
                        x.set_country(list_s[j][i])
                    except ValueError:
                        raise ValueError("В строке №" + str(i) + "не верно введен аргемунт № " + str(j) + " страна игрока!")
                elif i == 4:
                    try:
                        x.set_weidth(list_s[j][i])
                    except ValueError:
                        raise ValueError("В строке №" + str(i) + "не верно введен аргемунт № " + str(j) +  " рост игрока!")
                elif i == 5:
                    try:
                        x.set_type(list_s[j][i])
                    except ValueError:
                        raise ValueError("В строке №" + str(i) + "не верно введен аргемунт № " + str(j) +  " тип игрока!")
            lst_x.append(x)
        return lst_x
c = autofill("sportsmen.txt")

"""стало"""
from typing import List


class Sportsmen:
    def __init__(self, number=0, name="E", surname="D", country="F", weidth=100, types="G"):
        self.number = number
        self.name = name
        self.surname = surname
        self.country = country
        self.weidth = weidth
        self.types = types

    def set_sportsmen_number(self, new_number):
        self.number = new_number

    def get_sportsmen_number(self):
        return self.number

    def set_sportsmen_name(self, new_name):
        self.name = new_name

    def get_sportsmen_name(self):
        return self.name

    def set_sportsmen_surname(self, new_surname):
        self.surname = new_surname

    def get_sportsmen_surname(self):
        return self.surname

    def set_sportsmen_country(self, new_country):
        self.country = new_country

    def get_sportsmen_country(self):
        return self.country

    def set_sportsmen_weidth(self, new_weidth):
        self.weidth = new_weidth

    def get_sportsmen_weidth(self):
        return self.weidth

    def set_sportsmen_type(self, new_type):
        self.types = new_type

    def get_sportsmen_type(self):
        return self.types

#list_s = [[1, "Ivan", "Ivanov", "Russia", 180, "Foot"],[2, "Igor", "Fedin", "India", 199, "Basket"]]
#x = Sport(*list_s)
def autofill_info_about_sportsmen(files):
    lst_x = []
    with open(files, "rt") as sp:
        list_info_sportsmen = [line.split() for line in sp]
        print(list_info_sportsmen)
        for j in range(len(list_info_sportsmen)):
            sportsmen = Sportsmen()
            for i in range(len(list_info_sportsmen[j])):
                if i == 0:
                    try:
                        sportsmen.set_sportsmen_number(list_info_sportsmen[j][i])
                    except ValueError:
                        raise ValueError("В строке № " + str(i) + " не верно введен аргемунт № " + str(j) + " номер игрока!")
                elif i == 1:
                    try:
                        sportsmen.set_sportsmen_name(list_info_sportsmen[j][i])
                    except ValueError:
                        raise ValueError("В строке №" + str(i) + "не верно введен аргемунт № " + str(j) +  " имя игрока!")
                elif i == 2:
                    try:
                        sportsmen.set_sportsmen_surname(list_info_sportsmen[j][i])
                    except ValueError:
                        raise ValueError("В строке №" + str(i) + "не верно введен аргемунт № " + str(j) +  " фамилия игрока!")
                elif i == 3:
                    try:
                        sportsmen.set_sportsmen_country(list_info_sportsmen[j][i])
                    except ValueError:
                        raise ValueError("В строке №" + str(i) + "не верно введен аргемунт № " + str(j) + " страна игрока!")
                elif i == 4:
                    try:
                        sportsmen.set_sportsmen_weidth(list_info_sportsmen[j][i])
                    except ValueError:
                        raise ValueError("В строке №" + str(i) + "не верно введен аргемунт № " + str(j) +  " рост игрока!")
                elif i == 5:
                    try:
                        sportsmen.set_sportsmen_type(list_info_sportsmen[j][i])
                    except ValueError:
                        raise ValueError("В строке №" + str(i) + "не верно введен аргемунт № " + str(j) +  " тип игрока!")
            lst_x.append(sportsmen)
        return lst_x
c = autofill_info_about_sportsmen("sportsmen.txt")