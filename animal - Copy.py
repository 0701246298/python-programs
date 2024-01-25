
class Animal:
    def __init__(self,legs,feeding,name):
        self.legs=legs
        self.feeding=feeding
        self.name=name
    def print_infor(self):
        print(f"legs,{self.legs}")
        print(f"feeding,{self.feeding}")
        print(f"name,{self.name}")

        class Harbivore(Animal):
            def __init__(self,legs,feeding,name,vegetables):
                super().__init__(legs,feeding,name)
                self.vegetables=vegetables

    def print_infor(self):
        super().print_infor()
        print(f"type of vegetable eaten:{self.vegetable}")

        class carnivore(Animal):
            def __init__(self,legs,feeding,name,flesh):
                super.__init__(legs,feeding,name)
                self.flesh=flesh

    def print_infor(self):
        super().print_infor()
        print(f"type of Flesh eaten:{self.flesh}")

        class Omnivore(Harbivore,carnivore):
            def __init__(self,legs,feeding,name,vegetables,flesh):
                super().__init__(self,legs,feeding,name,vegetables)
                super().__init__(self,legs,feeding,name,flesh)
                self.vegetable,flesh=vegetables,flesh

        def print_infor(self):
            super().print_infor()
            print(f"The omnivore species::{self.vegetables,flesh}")

            issubclass(Harbivore, Animal)
            issubclass(carnivore, Animal)
            issubclass(Omnivore, Harbivore,carnivore)
legs=input("enter the no of legs :")
feeding=input("Type of feeding habit used :")
name=input("The name of the animal :")

type_Animal=input("Specify the type of the Animal:")

if type_Animal=="Herbivore":
    vegetables=input("Type of greens eaten:")
    Herbivore=Herbivore(legs,feeding,name,vegetables)

elif type_Animal == "Carnivore":
    flesh = input("Type of flesh feeds on: ")
    carnivore = Carnivore(legs, feeding, name, flesh)
    carnivore.print_info()

else:
    type_Animal=="Omnivore"
    vegetables = input("Type of greens eaten: ")
    flesh = input("Type of flesh feeds on: ")
    omnivore = Omnivore(legs, feeding, name, vegetables, flesh)
    omnivore.print_info()




