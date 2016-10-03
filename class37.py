import random as r

class Turtle:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
        self.stamina = 1000

    def move(self):
        self.x_move = r.choice([1, -1, 2, -2])
        self.y_move = r.choice([1, -1, 2, -2])

        self.x = self.x + self.x_move
        self.y = self.y + self.y_move

        if self.x < 0:
            self.x = -self.x
        elif self.x > 10:
            self.x = 10 - (self.x - 10)

        if self.y < 0:
            self.y = -self.y
        elif self.y > 10:
            self.y = 10 - (self.y - 10)

        self.stamina -= 1

        return (self.x, self.y)

    def eat(self):
        self.stamina += 20
        if self.stamina > 1000:
            self.stamina = 1000

        return(self.stamina)

    def getInfo(self):
        print('The location of the turtle is {0}'.format([self.x, self.y]))
        print('The stamina of the turtle is {0}'.format(self.stamina))

class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        self.x_move = r.choice([1, -1])
        self.y_move = r.choice([1, -1])

        self.x = self.x + self.x_move
        self.y = self.y + self.y_move

        if self.x < 0:
            self.x = -self.x
        elif self.x > 10:
            self.x = 10 - (self.x - 10)

        if self.y < 0:
            self.y = -self.y
        elif self.y > 10:
            self.y = 10 - (self.y - 10)

        return (self.x, self.y)

def game():
    turtle = Turtle()
    fish = []
    for i in range(10):
        new_fish = Fish()
        fish.append(new_fish)

    control = 0
    while(control == 0):
        
        if len(fish) == 0:
            print("Fish have been all eaten, game over, turtle wins.")
            control = 1
            
        if turtle.stamina < 0:
            print("Turtle is out of stamina, game over, fish win.")
            control = 2
        
        turtle.move()
        for i in fish[:]:
            if i.move() == turtle.move():
                turtle.eat()
                print("A fish is eaten.")
                turtle.getInfo()
                fish.remove(i)
    return(control)
                
    

def simulation():
    count = 0
    for i in range(30):
        if(game() == 1):
            count += 1
    turtle_win_rate = count/30
    print('Turtle has a {0} winning rate'.format(turtle_win_rate))


        
        
        
        
    
