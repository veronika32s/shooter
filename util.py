import math
import pygame
from data import*
from math import*

class Gift(pygame.Rect):
    def __init__(self,x,y,image,width,height):
        super().__init__(x,y,width,height)
        self.IMAGE = image

class Sprite(pygame.Rect):
   def __init__(self,x,y,width,height,image,step):
       super().__init__(x,y,width,height)
       self.X = x
       self.Y = y
       self.IMAGE = image
       self.STEP = step
       self.IMAGE_NOW = 0



class Bot(Sprite):
    def __init__(self,x,y,width,height,image1,image2,speed):
        super().__init__(x,y,width,height,image1,speed)
        self.IMAGE1 = image1
        self.IMAGE_NOW = self.IMAGE1
        self.IMAGE_LIST_BOT = [image1,image2]
        self.MOVE_IMAGE_BOT = 0
        self.SPEED = speed


    def moves(self, value, coff):
        if value % coff == 0:
            return 1
        return 0



    def angle(self,enemy):
        x = self.x - enemy.x
        d = (((abs(self.x - enemy.x)** 2) + (abs(self.y - enemy.y)**2 ))** 0.5)
        if d == 0:
            d = 0.01
        sin = abs(x)/d
        degree = asin(sin) / 3.1415 * 180
        triang_x = enemy.x - self.x
        triang_y = enemy.y - self.y


        if triang_x < 0 and triang_y <= 0:
            self.IMAGE_NOW = pygame.transform.rotate(self.IMAGE,270 + degree)
            return 180 + degree
        elif triang_x>= 0 and triang_y < 0:
            self.IMAGE_NOW = pygame.transform.rotate(self.IMAGE, 270 - degree)
            return 180 - (90 + degree) + 90
        elif triang_x > 0 and triang_y >= 0:
            self.IMAGE_NOW = pygame.transform.rotate(self.IMAGE, 90 + degree)
            return degree
        elif triang_x <= 0 and triang_y > 0 :
            self.IMAGE_NOW = pygame.transform.rotate(self.IMAGE,90 - degree)
            return 360 - (270 + degree) + 270
        return degree

    def step(self,enemy):
        degree = self.angle(enemy)
        y = cos(radians(degree)) * self.STEP
        x = cos(radians(90 - degree)) * self.STEP
        self.X += x
        self.Y += y
        self.x = self.X
        self.y = self.Y
        print(self.x,self.y)
        if self.collidelist(wall_list) != -1:
            self.X -= x
            self.Y -= y
            self.x = self.X
            self.y = self.Y
            if True :
                pass
        #self.MOVE_IMAGE_BOT += 1
        #if self.MOVE_IMAGE_BOT == 8:
            #self.MOVE_IMAGE_BOT = 0
        #self.IMAGE1 = self.IMAGE_LIST_BOT[self.move_bot(self.MOVE_IMAGE_BOT,7)]

class Player(Sprite):
    def __init__(self,x,y,width,height,image,step):
        super().__init__(x,y,width,height,image,step)
        self.MOVE = {"UP":False,"DOWN": False,"LEFT":False,"RIGHT":False}
        self.IMAGE_NOW = self.IMAGE
        self.TEST = [False,False,False,False]
        self.SHOT = False
        self.BULLET = []


    def move(self):
        if self.MOVE["UP"]:
            self.y -= self.STEP
            if not self.TEST[0]:
                self.IMAGE_NOW =  pygame.transform.rotate(self.IMAGE,90)
                self.TEST = [True,False,False,False]
                if self.collidelist(wall_list) != -1:
                    self.y += self.STEP
                    if True:
                        pass

        elif self.MOVE["DOWN"] and self.y < setting_win["HEIGHT"] - self.height:
            self.y += self.STEP
            if not self.TEST[1]:
                self.IMAGE_NOW =  pygame.transform.rotate(self.IMAGE,270)
                self.TEST = [False,True,False,False]
                if self.collidelist(wall_list) != -1:
                    self.y -= self.STEP
                    if True:
                        pass

        elif self.MOVE["LEFT"]:
            self.x -= self.STEP
            if not self.TEST[2]:
                self.IMAGE_NOW =  pygame.transform.rotate(self.IMAGE,180)
                self.TEST = [False,False,True,False]
            if self.collidelist(wall_list) != -1:
                self.x += self.STEP
                if True:
                    pass


        elif self.MOVE["RIGHT"] and self.x < setting_win["WIDTH"] - self.width:
            self.x += self.STEP
            if not self.TEST[3]:
                self.IMAGE_NOW =  pygame.transform.rotate(self.IMAGE,0)
                self.TEST = [False,False,False,True]
        if self.collidelist(wall_list) != -1:
            self.x -= self.STEP
            if True :
                pass


class Shot(pygame.Rect):
    def __init__(self):
        pass

class Bullet(pygame.Rect):
    def __init__(self,x,y,w,h):
        super().__init__(x,y,w,h)
        self.IMAGE = bullet_image
        self.X = 0
        self.Y = 0
        self.STEP = 8

    def make_angle(self,x,y,heroX,heroY):
        leg = abs(x - heroX)
        hypotenuse = (leg ** 2 + abs(y - heroY)** 2) ** 0.5
        sin = leg / hypotenuse
        degree = asin(sin) / 3.1415 * 180
        triang_x = heroX - x
        triang_y = heroY - y

        if triang_x < 0 and triang_y <= 0:
            self.X = cos(radians(180 - 90 - degree)) * self.STEP
            self.Y = cos(radians(degree)) * self.STEP
            degree = 270 + degree

        elif triang_x >= 0 and triang_y < 0:
            self.X = cos(radians(180 - 90 - degree)) * self.STEP * -1
            self.Y = cos(radians(degree)) * self.STEP
            degree = 180 + (90 - degree)

        elif triang_x > 0 and triang_y >= 0:
            self.X = cos(radians(180 - 90 - degree)) * self.STEP * -1
            self.Y = cos(radians(degree)) * self.STEP * -1
            degree = 90 + degree

        elif triang_x <= 0 and triang_y > 0:
            self.X = cos(radians(180 - 90 - degree)) * self.STEP
            self.Y = cos(radians(degree)) * self.STEP * -1
            degree = 90 - degree
        self.IMAGE = pygame.transform.rotate(self.IMAGE, degree)

class Wall(pygame.Rect):
    def __init__(self,x,y,image,width = 20,height= 100):
        super().__init__(x,y,width,height)
        self.IMAGE = image
def create_wall(present_map):
    x, y = 0, 0

    for string in maps[present_map]:
        for element in string:
            if element == "1":
                wall_list.append(Wall(x, y, wall_image))
            elif element == "2":
                wall_list.append(Wall(x, y + 30, pygame.transform.rotate(wall_image, 90), width=100, height=20))
            elif element == "3":
                wall_list.append(Wall(x, y + 30, pygame.transform.rotate(wall_image, 180)))
            x += 50
        x = 0
        y += 50
