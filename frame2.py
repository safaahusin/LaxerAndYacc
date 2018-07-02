import pygame, sys
from pygame.locals import *

class frame:
    pygame.init()
    myfont = pygame.font.SysFont("Times New Roman", 30)
    def Action(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    import frame3
                    frame3.frameDs()

    def drawBackground(self):
        bg = pygame.image.load("characters-right.png")  # ellsa
        pygame.display.set_icon(bg)
        self.DIS.blit(pygame.transform.scale(bg, (200, 350)), (300,370))

    def drawTree(self):
        label = self.myfont.render("Pointer And Array",10,(255, 255, 0))
        self.DIS.blit(label, (580,60))
        label = self.myfont.render("Statement", 10, (255, 255, 255))
        self.DIS.blit(label,(130,120))
        label = self.myfont.render("EndOfStatement",10,(255, 255,255))
        self.DIS.blit(label, (580,120))
        label = self.myfont.render("Expression",10,(255, 255,255))
        self.DIS.blit(label, (1100,120))
        label = self.myfont.render(".",10,(255,0,0))
        self.DIS.blit(label, (630,180))
        label = self.myfont.render("Array",10,(255, 255,255))
        self.DIS.blit(label, (150,180))
        label = self.myfont.render("DateType",10,(255, 255,255))
        self.DIS.blit(label, (40,240))
        label = self.myfont.render("Name",10,(255, 255,255))
        self.DIS.blit(label, (200,240))
        label = self.myfont.render("[",10,(255,0,0))
        self.DIS.blit(label, (320,240))
        label = self.myfont.render("]",10,(255,0,0))
        self.DIS.blit(label, (450,240))
        label = self.myfont.render("const",10,(255, 255,255))
        self.DIS.blit(label, (360,240))
        label = self.myfont.render("10",10,(255,0,0))
        self.DIS.blit(label, (370,300))
        label = self.myfont.render("X",10,(255,0,0))
        self.DIS.blit(label, (230,300))
        label = self.myfont.render("NonPrimitive",10,(255, 255,255))
        self.DIS.blit(label, (40,300))
        label = self.myfont.render("Integer",10,(255,0,0))
        self.DIS.blit(label, (40,360))
        label = self.myfont.render("Statement",10,(255, 255,255))
        self.DIS.blit(label, (950,180))
        label = self.myfont.render("EndOfStatement",10,(255, 255,255))
        self.DIS.blit(label, (1150,180))
        label = self.myfont.render(".",10,(255, 0, 0))
        self.DIS.blit(label, (1250,240))
        label = self.myfont.render("Pointer",10,(255, 255,255))
        self.DIS.blit(label, (950,240))
        label = self.myfont.render("DataType",10,(255, 255,255))
        self.DIS.blit(label, (800,300))
        label = self.myfont.render("PointerChar",10,(255, 255,255))
        self.DIS.blit(label, (950,300))
        label = self.myfont.render("Name",10,(255, 255,255))
        self.DIS.blit(label, (1130,300))
        label = self.myfont.render("St",10,(255, 0, 0))
        self.DIS.blit(label, (1130,360))
        label = self.myfont.render("#",10,(255, 0, 0))
        self.DIS.blit(label, (1000,360))
        label = self.myfont.render("Oop",10,(255, 255,255))
        self.DIS.blit(label, (820,360))
        label = self.myfont.render("OopType",10,(255, 255,255))
        self.DIS.blit(label, (750,420))
        label = self.myfont.render("Name",10,(255, 255,255))
        self.DIS.blit(label, (890,420))
        label = self.myfont.render("Student",10,(255, 0, 0))
        self.DIS.blit(label, (890,480))
        label = self.myfont.render("Class",10,(255, 0, 0))
        self.DIS.blit(label, (750,480))


    # constructor class start from here
    def __init__(self):
        self.DIS = pygame.display.set_mode((1400, 900), pygame.RESIZABLE, 32)
        pygame.display.set_caption("Primitive&NonPrimitive")
        while True:

            self.drawTree()
            self.Action()
            self.drawBackground()
            pygame.display.update()

