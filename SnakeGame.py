import pygame,sys,random,string,time

pygame.init()
screen = pygame.display.set_mode((800,600)) #CREATE WİNDOW 800px / 600px

xplus = 20
yplus = 0
snakebody = pygame.image.load("snakebody.png")

#NEW PARTS RANDOM NAME

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))

#FONTS
font = pygame.font.SysFont("comicsansms", 28)
font2 = pygame.font.SysFont("comicsansms", 70)
font3 = pygame.font.SysFont("comicsansms", 50)
point = 0 #Player Point

#CREATE SNAKE PARTS
class part:
    def __init__(self,color,x,y,u):
        self.color = color
        self.x = x
        self.y = y
        self.u = u
    def draw(self):
        screen.blit(snakebody,(self.x,self.y))
    def drawforhead(self):
        pygame.draw.rect(screen, (25, 25, 255), [self.x, self.y, self.u, self.u])

#CREATE FRUİT
class fruit:
    newFruitCordination_X = random.randint(1,35)*20 #random cordination
    NewFruitCordination_Y = random.randint(1,25)*20 #random cordination
    def __init__(self):
        self.x = self.newFruitCordination_X
        self.y = self.newFruitCordination_X
        self.u = 20
    def draw(self):
        pygame.draw.rect(screen,(255,255,255),[self.x,self.y,self.u,self.u])

#CREATE SNAKE START ELEMENTS
head = part((20,20,255),100,60,20)
body1 = part((30,50,100),80,60,20)
body2 = part((30,50,100),60,60,20)
body3 = part((30,50,100),40,60,20)
fruita = fruit()
partlist = [head,body1,body2,body3] #All parts in a list for controlled

fps = pygame.time.Clock() #timer
text2 = font2.render("GAME OVER",True,(255,0,0)) #game over text
textrestart = font.render("Press Any Arrow Keys to Restart",True,(100,0,255)) #Restart Game

while True:
    fps.tick(10)
    screen.fill((0,0,0))
    text3 = font3.render("Score = " + str(point), True, (200, 0, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and yplus!=+20:
                yplus=-20
                xplus = 0
                continue
            if event.key == pygame.K_DOWN and yplus!=-20:
                yplus = 20
                xplus = 0
                continue
            if event.key == pygame.K_LEFT and xplus!=20:
                xplus = -20
                yplus = 0
                continue
            if event.key == pygame.K_RIGHT and xplus!=-20:
                xplus = 20
                yplus = 0
                continue


    #Snake Parts Move Rules
    s1 = len(partlist)
    s2 = 1
    while s2<len(partlist):
        partlist[s1-1].x = partlist[s1-2].x
        partlist[s1-1].y = partlist[s1 - 2].y
        partlist[s1-1].draw()
        s1-=1
        s2+=1

    #DRAW AND MOVE HEAD!
    head.x += xplus
    head.y += yplus
    head.drawforhead()
    fruita.draw()

    # <- When Snake Eat Fruit Create New Snake Part ->
    if fruita.x == head.x  and fruita.y == head.y:
        randx = random.randint(1,39)
        randy = random.randint(1,29)
        fruita.x = randx*20
        fruita.y = randy*20
        newpart =  get_random_string(8)
        newpart = part((30,50,100),0,0,20)
        partlist.append(newpart)
        point += 1

    #sneake is die :(
    s3 = len(partlist)-1

    while True:
        if partlist[s3].x == head.x and partlist[s3].y == head.y:
            xplus = 0
            yplus = 0
            screen.blit(text2, (190, 150))
            screen.blit(text3,(270,230))
            partlist = [head,body1,body2,body3]
            s3 = 2
            screen.blit(textrestart,(175,300))
            time.sleep(2)



        if s3 > 2:
            s3 -= 1
        elif s3 < 3:
            break

     #WALL CONTROLS
    if head.x > 780 :
        head.x = 0
    if head.x < 0:
        head.x = 800


    if head.y > 580:
        head.y = 0
    if head.y < 0:
        head.y = 580

    #POİNT TEXT
    text = font.render(str(point), True, (10, 255, 0))
    screen.blit(text,(760,5))

    pygame.display.update()