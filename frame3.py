import pygame, sys, drawTree
from pygame.locals import *

class frameDs:
    pygame.init()
    myfont = pygame.font.SysFont("Times New Roman", 30)
    def Action(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    import drawTree
                    drawTree.MainFrame()

    def drawBackground(self):
        bg = pygame.image.load("sadness.png")
        pygame.display.set_icon(bg)
        self.DIS.blit(pygame.transform.scale(bg, (200, 350)), (500, 350))

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
        label = self.myfont.render("ArrayList",10,(255, 255,255))
        self.DIS.blit(label, (110,180))
        label = self.myfont.render("ArrayListType",10,(255, 255,255))
        self.DIS.blit(label, (40,240))
        label = self.myfont.render("<",10,(255, 0,0))
        self.DIS.blit(label, (230,240))
        label = self.myfont.render("NonPrimitive",10,(255, 255,255))
        self.DIS.blit(label, (260,240))
        label = self.myfont.render(">",10,(255, 0,0))
        self.DIS.blit(label, (430,240))
        label = self.myfont.render("Name",10,(255, 255,255))
        self.DIS.blit(label, (460,240))
        label = self.myfont.render("String",10,(255, 0,0))
        self.DIS.blit(label, (290,300))
        label = self.myfont.render("X",10,(255, 0,0))
        self.DIS.blit(label, (490,300))
        label = self.myfont.render("ArrayList",10,(255, 0,0))
        self.DIS.blit(label, (60,300))
        label = self.myfont.render("Statement",10,(255, 255,255))
        self.DIS.blit(label, (950,180))
        label = self.myfont.render("DataStructure",10,(255, 255,255))
        self.DIS.blit(label, (900,240))

        label = self.myfont.render("DataStructureType",10,(255, 255,255))
        self.DIS.blit(label, (750,300))
        label = self.myfont.render("HashMap",10,(255, 0,0))
        self.DIS.blit(label, (800,360))
        label = self.myfont.render("Name",10,(255, 255,255))
        self.DIS.blit(label, (1000,300))
        label = self.myfont.render("Hash",10,(255, 0,0))
        self.DIS.blit(label, (1020,360))
        label = self.myfont.render("(",10,(255, 0,0))
        self.DIS.blit(label, (1080,300))
        label = self.myfont.render("10",10,(255, 0,0))
        self.DIS.blit(label, (1120,360))
        label = self.myfont.render("const",10,(255, 255,255))
        self.DIS.blit(label, (1100,300))
        label = self.myfont.render(")",10,(255, 0,0))
        self.DIS.blit(label, (1180,300))

        label = self.myfont.render("EndOfStatement",10,(255, 255,255))
        self.DIS.blit(label, (1150,180))
        label = self.myfont.render(".",10,(255, 0, 0))
        self.DIS.blit(label, (1250,240))



    # constructor class start from here
    def __init__(self):
        self.DIS = pygame.display.set_mode((1400, 900), pygame.RESIZABLE, 32)
        pygame.display.set_caption("Primitive&NonPrimitive")
        while True:
            self.drawTree()
            self.Action()
            self.drawBackground()
            pygame.display.update()

