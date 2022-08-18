from xmlrpc.client import boolean
import pygame
import random

pygame.init()

xbound = 1100
ybound = 1100
dis = pygame.display.set_mode((xbound,ybound))

pygame.display.update()

pygame.display.set_caption('Snake by Ford')

blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)

game_over = False

x1 = 500
y1 = 500

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

class Direction:
    def __init__(self):
        self.direction = "none"
        self.chanelist = {"none": (0,0), "right": (1, 0), "left": (-1,0), "down": (0,1), "up":(0,-1)}
    def set_direction(self, string): 
        if string == self.direction:
            return
        if (string == "right") & (self.direction == "left"):
            return
        if (string == "left") & (self.direction == "right"):
            return
        if (string == "up") & (self.direction == "down"):
            return       
        if (string == "down") & (self.direction == "up"):
            return
        self.direction = string
    def get_direction(self):
        return self.direction
    def get_change(self):
        return self.chanelist.get(self.direction)

class Snake:
    def __init__(self):
        self.position = [(5,5)]
        self.dir = Direction()
        self.rear = (5,5)
        self.chanelist = {"none": (0,0), "right": (1, 0), "left": (-1,0), "down": (0,1), "up":(0,-1)}

    def update_state(self , foodCoords):
        head = self.position[0]
        change = self.dir.get_change()
        x = head[0] + change[0]
        y = head[1] + change[1]
        if x > 10:
            x = 0
        elif x < 0:
            x = 10
        elif y > 10:
            y = 0
        elif y < 0:
            y = 10
        self.position.insert(0,(x,y))
        if self.position[0] != foodCoords:
            self.rear = self.position.pop()
            return True
        return False
        
    def get_head(self):
        return self.position[0]

    def get_rear(self):
        return self.rear

    def get_position(self):
        return self.position

class Food:
    def __init__(self):
        self.count = 0
        self.food = (int(random.random()*10),int(random.random()*10))

    #def create_new(self, snake : Snake):
    def get_food(self):
        return self.food
        
direction = Direction()

snake = Snake()

foodAvailable = False

dis.fill(white)
head = snake.get_head()
pygame.draw.rect(dis,blue,[head[0]*100,head[1]*100,100,100])

while not game_over:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.dir.set_direction("left")
            elif event.key == pygame.K_RIGHT:
                snake.dir.set_direction("right")
            elif event.key == pygame.K_DOWN:
                snake.dir.set_direction("down")
            elif event.key == pygame.K_UP:
                snake.dir.set_direction("up")
        
    #if there is no food add one!
    if foodAvailable == False:
        cur_food = Food().get_food()
        pygame.draw.circle(dis,black,[cur_food[0]*100 + 50,cur_food[1]*100 + 50],50)
        foodAvailable = True

    #draw a rectangle at the front of the snake
    head = snake.get_head()
    rear = snake.get_rear()
    positionlist = snake.get_position()
    if snake.dir.get_direction() !=  "none":
        foodAvailable = snake.update_state(cur_food)
        pygame.draw.rect(dis,blue,[head[0]*100,head[1]*100,100,100])
        #remove the end of the snake
        pygame.draw.rect(dis,white,[rear[0]*100,rear[1]*100,100,100])

    pygame.display.update()
    clock.tick(5)

pygame.quit()
quit()

