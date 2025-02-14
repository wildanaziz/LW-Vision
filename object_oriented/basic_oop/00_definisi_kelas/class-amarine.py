## Class

# class Amarine2:
#     def __init__(self, name, color, year):
#         self.name = name
#         self.color = color
#         self.year = year
    
#     def serang(self, target):
#         self.target = print(self.name + " Menyerang " + target)
    
#     def diserang(self, targetDiserang):
#         self.targetDiserang = print(self.name + " Diserang " + targetDiserang)
    
    
# # vanderwijk = Amarine2("paijo", "black", "2021")
# # print(vanderwijk.getInfo())

# submarine2 = Amarine2("yamato", "Black", "2021")
# submarine3 = Amarine2("mahareksa", "blue", "2022")

# submarine2.serang(submarine3.name)
# submarine3.diserang(submarine2.name)

## access modifier dan encapsulation

# class AccessModifier:
#     def __init__(self, name, color, year):
#         self.__name = name
#         self.__color = color
#         self._year = year

#     @property
#     def name(self):
#         return self.__name
    
#     @property
#     def color(self):
#         return self.__color
    
#     @color.setter
#     def color(self, color):
#         self.__color = color
       


# yamato = AccessModifier("yamato", "black", "2021")
# print(yamato.color)
# yamato.color = "blue"
# print(yamato.color)

## Inheritance

class Inheritance:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class subInheritance(Inheritance):
    pass
    
ayah = Inheritance("Dad", 50)
print(ayah.name)
anak = subInheritance("Son", 20)
print(anak.__dict__)

