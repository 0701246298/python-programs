class Ship:
    location=[]
    def getdata(self,name,load,location1,location2):
        Ship.name=name
        Ship.load=load
        Ship.location.append(location1)
        Ship.location.append(location2)
     def display(self):
         print("name",Ship.__name__)
         print("load",Ship.location)
         name=input("name")
         load=input("desc load")
         location1=input("location1")
         location2 = input("location2")
         MyShip=Ship()
         MyShip.getdata(name, load,location1,location2)
         MyShip.display()
