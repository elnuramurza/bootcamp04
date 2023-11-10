class Dog:  # roditel # pretki
    tail = 1
    paws = 4
    size = 0.5
    def talk(self):
        print("gaf")
class Wolf(Dog):     #docerny   # poditel
    tail = 1
    paws = 4
    size = 1.5
    def talk(self):
        print('Auuu')
class  PolarWolf(Wolf):  #docerny potomok
    color = 'white' 
    def run (self):
        super() .run ()  
        self.run_distance = 50
akela = PolarWolf()
akela.run()
print(akela.run)        
