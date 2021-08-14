import pygame

import time

import math

from random import randrange

pygame.init()

WIDTH = 600
HEIGHT= 500


black= (0,0,0)
white= (255,255,255)
lightgreen = (200,255,255)

red= (255,0,0)
green= (0,255,0)
blue= (0,0,255)


show= pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('SNAKE(Ok4s 1st)')

clock= pygame.time.Clock()

show.fill(lightgreen)


    


global score
score = 0

global continuegame
continuegame= True

#global f
#f = open('highscore7.txt', 'a')

class box:
    def __init__(self,x,y):
        self.x= x
        self.y= y
        self.size= 20
        #self.boxlist = [box(x,20), box(x,20), box(x,20)]
        #x= (self.boxlist.index(b)+1)*i

    def draw(self):
        p= (self.x, self.y, self.size, self.size)
        pygame.draw.rect(show, blue, p)

    def isoutside(self):
        if self.x < 0:
            self.x = WIDTH
        if self.y < 0:
            self.y = HEIGHT
        if self.x > WIDTH:
            self.x = 0
        if self.y > HEIGHT:
            self.y = 0

    def getcenter(self):
        a= self.x + self.size/2
        b= self.y + self.size/2
        return a,b 

    def collide(self, x, y):
        cx,cy = self.getcenter()
        if (((x-(cx))**2 + (y-(cy))**2)**0.5) < (self.size):
            return True
        return False

    #def poss(b):
        #v= (self.boxlist.index(b)+1)*i
        #return v
    


class snake:
    def __init__(self, x,y,dx= 1, dy= 0):
        self.boxsize= 22
        self.x= x
        self.y= y
        self.dx =dx
        self.dy = dy
        self.poslistx= [20, 42, 64]
        self.boxlist = [box(64,20), box(42,20), box(20,20)]
        self.grow= False 
        #self.poss= b
        

        
    def move(self):
        fbox= self.boxlist[0]
        newx= fbox.x+ (self.dx * self.boxsize)
        newy= fbox.y+ (self.dy * self.boxsize)
        b= box(newx, newy)
        self.boxlist.insert(0, b)
        if self.grow == False:
            self.boxlist.remove(self.boxlist[-1])
        self.grow= False
        
        ##self.poslistx[-1]+=22
        #print(self.poslist)
        ##self.boxlist.insert(-1, box(self.poslistx[-1], 20))
        ##del self.boxlist[0]
        #for i in self.boxlist:
            #u= poss(i)
        #return u
        #self.x+= self.dx
        #self.y+= self.dy

    def draw(self):
        for i in self.boxlist:
            i.draw()
            i.isoutside()

    def gameover(self):
        global continuegame
        x,y= self.boxlist[0].getcenter()
        for i in self.boxlist[1:-1]:
            
            if i.collide(x,y):
                continuegame= False
                

       

    
class apple:
    def __init__ (self, x, y):
        self.box= box(x,y)
        self.box.size = 25
        
    def draw(self):
        a= (self.box.x, self.box.y)
        pygame.draw.circle(show, red, a, int(self.box.size/2))

    #def animate(self):  
       #self.size+=1
       #self.size-=1
        
   
    #def collide(self, spriteGroup):
        #if pygame.sprite.spritecollide(self, spriteGroup, False):
            #print('ok')
        
    def collide(self, x2,y2, s):
        global score
        if self.box.collide(x2,y2):
            self.box.x= randrange(50, WIDTH-50)
            self.box.y= randrange(50, HEIGHT-50)
            s.grow = True
            score= score + 1
            
        
def drawscore():
        font= pygame.font.SysFont(None, 25)
        text= font.render("Score:" + str(score), True, black)
        show.blit(text, (0,0))




    
   

def rungame():
    global score
    score= 0
    global continuegame
    continuegame = True
    
    a= apple(250,200)

    direction= 'left'

    s= snake(45,87)
    
    while continuegame:
        show.fill(lightgreen)
        drawscore()

        s.draw()
        s.move()

        a.draw()
        i= s.boxlist[0]
        x,y= i.getcenter()
        a.collide(x, y, s)
        #a.size+= 1
        #time.sleep(1)
        #a.size-= 1
        #a.animate()
        s.gameover()
        #gethighscore()
        #print(hi)




        

       
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        
            

            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_UP or event.key == ord('w'):
                     if direction != "down":
                         s.dx = 0
                         s.dy = -1
                         direction = 'up'

                 if event.key == pygame.K_DOWN or event.key == ord('s'):
                     if direction != "up":
                         s.dx = 0
                         s.dy = 1
                         direction = 'down'

                 if event.key == pygame.K_RIGHT or event.key == ord('d'):
                     if direction != 'left':
                         s.dx = 1
                         s.dy = 0
                         direction = 'right'
                
                 if event.key == pygame.K_LEFT or event.key == ord('a'):
                     if direction != 'right':
                         s.dx = -1
                         s.dy = 0
                         direction = 'left'
                





        pygame.display.update()
        clock.tick(15)

                


    # GAme Over

#highscore = 0
#f = open('highscore8.txt', 'a')
#f.write(str(highscore))
        
#if score > highscore:
#    f = open('highscore8.txt', 'a')
#    f.truncate(0)
#    f.close()
#    highscore = score
#    f = open('highscore8.txt', 'a')
#    f.write(str(highscore))
#    f.close
#f = open('highscore8.txt', 'r')
#hi = f.read()
#print(hi)
    

def message_display():
    font= pygame.font.SysFont(None, 75)
    text= font.render("Game Over Bro", True, black)
    show.blit(text, (int(WIDTH/5),int(HEIGHT/3)))
    pygame.display.update()
    pygame.time.wait(10000)

def main():
    while True:
        rungame()
        message_display()
        #gethighscore()



main()




