import pygame
import math
#using elastic collision formulas only along x-axis
"""
v1 = ((m1-m2)*u1 + 2*m2*u2)/m1+m2
v2 = (2*m1*u1+(m2-m1)*u2)/m1+m2

"""
pygame.init()
width,height = 1000,1000
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Elastic collision")
font = pygame.font.SysFont("arial",20)
FONT_COLOUR = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
class Box:
    def __init__(self,m,v,x,y,w,h,color): #mass, velocity, initial velocity, coods, width,height, colour
        self.m = m
        self.v = v
        self.x = x
        self.init_x = x
        self.init_v = v
        self.y = y
        self.w = w
        self.h = h
        self.color = color

    def draw_rect(self,win):
        my_rect = pygame.Rect(self.x,self.y,self.w,self.h)
        pygame.draw.rect(win,(self.color),my_rect)
    def collision_calc(self,obj2):
        temp_v1 = self.v
        temp_v2 = obj2.v
        self.v = round(((self.m-obj2.m)*temp_v1 + 2*obj2.m*temp_v2)/(self.m+obj2.m)) # elastic collision eqns
        obj2.v = round((2*self.m*temp_v1+(obj2.m-self.m)*temp_v2)/(self.m+obj2.m))
    def update(self):
        self.x += self.v # updating position based on velocity
    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.w,self.h)

def main():
    run = True
    clock = pygame.time.Clock()
    inp_m1 = float(input("Enter the mass for object 1 : "))
    inp_m2 = float(input("Enter the mass for object 2 : "))
    inp_v1 = float(input("Enter the velocity for object 1 : "))
    inp_v2 = float(input("Enter the velocity for object 2 : "))
    b1 = Box(inp_m1,inp_v1,50,500,100,100,RED)
    b2 = Box(inp_m2,inp_v2,850,500,100,100,BLUE)
    collided = False
    while run:
        window.fill(WHITE)
        textm1 = font.render(f"m1 = {b1.m}, v1 = {b1.v}",True,FONT_COLOUR)
        textm2 = font.render(f"m2 = {b2.m}, v2 = {b2.v}",True,FONT_COLOUR)
        clock.tick(60)
        window.blit(textm1,(30,150))
        window.blit(textm2,(800,150))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r: # reset
                    b1.x = b1.init_x
                    b2.x = b2.init_x
                    b1.v = b1.init_v
                    b2.v = b2.init_v
                    collided = False
        b1.draw_rect(window)
        b2.draw_rect(window)
        b1.update()
        b2.update()
        if b1.get_rect().colliderect(b2.get_rect()): # if this is true
            if not collided: # if the objects have not alr collided
                b1.collision_calc(b2) # then calculate this
                collided = True # and then tell the system it has finally collided
            else:
                collided = False
        #collisions with the screen
        if b1.x <= 0:
            b1.v = abs(b1.v)
        if b2.x + b2.w > width:
            b2.v = -abs(b2.v)
        pygame.display.update()
    pygame.quit()
main()
    
        
            
        


    
