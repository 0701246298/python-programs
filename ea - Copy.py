def addition(a,b):
    x=a+b
    print(x)
   def addition(a,b,c):
       x=a+b+c
       print(x)
       addition(7,2)
       addition(7,2,1)
       print((3+2)
       print("Preston"+"Simiyu")
       print(3*2)

       class Animalia:
           def __init__(self, species):
               self.species = species

           def eat(self):
               pass  # This is a placeholder for the eat method

       class Herbivore(Animalia):
           def __init__(self, species):
               super().__init__(species)

           def eat(self):
               return f"{self.species} is a herbivore and eats plants."

       class Carnivore(Animalia):
           def __init__(self, species):
               super().__init__(species)

           def eat(self):
               return f"{self.species} is a carnivore and hunts other animals."

       class Omnivore(Herbivore, Carnivore):
           def __init__(self, species):
               super().__init__(species)

           def eat(self):
               return f"{self.species} is an omnivore and eats both plants and other animals."

       # Example usage
       herbivore_animal = Herbivore("Deer")
       print(herbivore_animal.eat())

       carnivore_animal = Carnivore("Lion")
       print(carnivore_animal.eat())

       omnivore_animal = Omnivore("Bear")
       print(omnivore_animal.eat())

