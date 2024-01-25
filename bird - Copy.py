class bird:
    def __int__(self,name,legs,color):
        self.name=name
        self.legs=legs
        self.color=color


    def print_infor(self):
            print(f"name:{self.name}")
            print(f"color:{self.color}")
            print(f"number of legs:{self.legs}")

            class fly(bird):
                  def __init__(self,name,color,legs,wing):
                     super().__init__(name,color,legs)
                     self.wing=wing

    def print_infor(self):
        super().print_infor()
        print(f"the number of wings is:{self.wing}")

        class swim(bird):
            def __init__(self, name, color, legs, fins):
                super().__init__(name, color, legs)
                self.fins = fins

    def print_infor(self):
        super().print_infor()
        print(f"no of fins:{self.fins}")


        issubclass(fly,bird)
        issubclass(swim,bird)

# tesing the code.
name=input("enter your name:")
color=input("enter your color:")
legs=input("enter no of legs:")

type_bird=input("enter the bird type:")
if type_bird=="fly":
     wings=input("Enter the number of wings:")
     fly = fly(name,color,legs,wings)
     fly. print_infor()
else:
     fins=input("enter number of fins:")
     swim=swim(name,color,legs,fins)
     swim.print_infor()











