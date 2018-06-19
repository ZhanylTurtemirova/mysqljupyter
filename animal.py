class Animal:
    def __init__(self,name):
        self.name =name
        self.mood=10
        self.hunger=10
        self.health=10
        self.alive=True
        
    def feed(self):
        if  self.alive:
            if self.hunger<5:
                self.health=health-1
            self.hunger=self.hunger-1
            self.mood=self.mood+10/self.mood
        self.checklife()
        
    def exercise(self):
        if  self.alive:
            if self.hunger>10:
                self.mood=self.mood-1
            else:
                self.mood= self.mood+1
            self.health=self.health+1;
        self.checklife()
    
    def check(self):
        if self.alive:
            if self.health>5:
                print(self.name + " is healthy")
            else:
                print(self.name + " is sick")
        else:
            print(self.name +" is dead")
        self.checklife()
        
#     def check(self):
#          if self.alive:
#                 if self.health>5:
#                     print(self.name+ " is healthy")
#                 else:
#                     print(self.name+ " is sick")
#         else:
#             print(self.name+ " is dead")
#         self.checklife()       
        
    def checklife(self):    
        if self.health<=0:
            self.alive=False
                
                