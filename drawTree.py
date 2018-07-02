import pygame, sys
from pygame.locals import *

class MainFrame:
    pygame.init()
    myfont = pygame.font.SysFont("Times New Roman", 30)
    def Action(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    import frame2
                    frame2.frame()




    def drawBackground(self):
        bg = pygame.image.load("Joy.png")
        img = pygame.image.load('Joy_and_Sadness_Render.png')
        pygame.display.set_icon(bg)
        self.DIS.blit(pygame.transform.scale(bg, (300, 300)), (1100, 350))
        self.DIS.blit(pygame.transform.scale(img, (200, 350)), (100,350))

    def drawTree(self):
        label = self.myfont.render("Expression",10,(255, 255, 0))
        self.DIS.blit(label, (600,60))
        label = self.myfont.render("Statement", 10, (255, 255, 255))
        self.DIS.blit(label,(130,120))
        label = self.myfont.render("EndOfStatement",10,(255, 255,255))
        self.DIS.blit(label, (580,120))
        label = self.myfont.render("Expression",10,(255, 255,255))
        self.DIS.blit(label, (1100,120))
        label = self.myfont.render(".",10,(255,0,0))
        self.DIS.blit(label, (630,180))
        label = self.myfont.render("DataType",10,(255, 255,255))
        self.DIS.blit(label, (40,180))
        label = self.myfont.render("Name",10,(255, 255,255))
        self.DIS.blit(label, (220,180))
        label = self.myfont.render("X",10,(255, 0, 0))
        self.DIS.blit(label, (250,240))
        label = self.myfont.render("Primitive",10,(255, 255, 255))
        self.DIS.blit(label, (40,240))
        label = self.myfont.render("int",10,(255, 0, 0))
        self.DIS.blit(label, (50,300))
        label = self.myfont.render("Statement",10,(255, 255,255))
        self.DIS.blit(label, (950,180))
        label = self.myfont.render("EndOfStatement",10,(255, 255,255))
        self.DIS.blit(label, (1150,180))
        label = self.myfont.render("dataType",10,(255, 255, 255))
        self.DIS.blit(label, (890,240))
        label = self.myfont.render("Name",10,(255, 255, 255))
        self.DIS.blit(label, (1050,240))
        label = self.myfont.render(".",10,(255, 0, 0))
        self.DIS.blit(label, (1250,240))
        label = self.myfont.render("NonPrimitive",10,(255, 255,255))
        self.DIS.blit(label, (850,300))
        label = self.myfont.render("St",10,(255,0, 0))
        self.DIS.blit(label, (1080,300))
        label = self.myfont.render("Oop",10,(255, 255, 255))
        self.DIS.blit(label, (830,360))
        label = self.myfont.render("Name",10,(255, 255, 255))
        self.DIS.blit(label, (950,360))
        label = self.myfont.render("Student",10,(255, 0, 0))
        self.DIS.blit(label, (950,420))
        label = self.myfont.render("OopType",10,(255, 255,255))
        self.DIS.blit(label, (800,420))
        label = self.myfont.render("Struct",10,(255,0, 0))
        self.DIS.blit(label, (800,480))




    # constructor class start from here
    def __init__(self):
        self.DIS = pygame.display.set_mode((1400, 900), pygame.RESIZABLE, 32)
        pygame.display.set_caption("Primitive&NonPrimitive")
        while True:
            self.drawTree()
            self.Action()
            self.drawBackground()
            pygame.display.update()

MainFrame()