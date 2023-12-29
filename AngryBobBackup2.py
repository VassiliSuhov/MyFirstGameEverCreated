import pygame
import random
pygame.init()

maincharimg = pygame.image.load("C:/Users/Intel/Desktop/Susan.png")
GameDisplay = pygame.display.set_mode((1900 ,900))
pygame.display.set_caption("Angry Bob")
clock = pygame.time.Clock()



Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Blue = (0,0,255)






def Gameloop():
    
    
    left = False
    y = 300
    x = 400
    respawnx = 400
    respawny = 300
    x_change = 0
    y_change = 0
    speed = 10 # speed of the player
    jumpspeed = 40
    gravityforce = 5
    blocksw = (70,400)
    blocksh = (800,760)
    Jumps = 0
    UseGravity = True
    IsGrounded = False
    DashTime = 10
    DashSpeed = 50
    Dashs = 0
    SpaceKey = False
    CameraMoveX = 400
    CameraMoveY = 0
    CameraChangeX = 0
    blockadded = 100
    addt = 1
    
   
   
    
    
    while blockadded != 0:
        blockadded -= 1
        xrand = random.randrange(300,400)
        yrand = random.randrange(100,200)
        upordown = random.randrange(1,3)
        if(blocksh[addt] > 80 and blocksh[addt] < 750):
            if(upordown == 1 ):
                blocksw = blocksw + (blocksw[addt] + xrand,)
                blocksh = blocksh + (blocksh[addt] + -yrand,)
            else:
                blocksw = blocksw + (blocksw[addt] + xrand * 1.5 ,)
                blocksh = blocksh + (blocksh[addt] + (yrand * 1.2),)
        if(blocksh[addt] < 80):
            blocksw = blocksw + (blocksw[addt] + xrand * 1.5,)
            blocksh = blocksh + (blocksh[addt] + (yrand * 2),)
        if blocksh[addt] > 750:
            blocksw = blocksw + (blocksw[addt] + xrand,)
            blocksh = blocksh + (blocksh[addt] + -yrand,)
        addt += 1      
    
    
    
    while not left:
        SpaceKey = False
        DashSpeed = 200
        for event in pygame.event.get():#the codes here are for Input
            
            if event.type == pygame.QUIT:
                left = True
            if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_a:
                   
                   CameraChangeX = 20
               if event.key == pygame.K_d:
                   
                   CameraChangeX = -20
               if event.key == pygame.K_w and Jumps > 0:
                   y_change = -jumpspeed
                   Jumps -= 1
               if  event.key == pygame.K_SPACE:
                   SpaceKey = True  
                   
                   
            if event.type == pygame.KEYUP:
               if event.key == pygame.K_a:
                   CameraChangeX = 0
               if event.key == pygame.K_d:
                   CameraChangeX = 0
        if(SpaceKey  and Dashs == 1 and not IsGrounded):
            DashSpeed = (CameraChangeX) / speed * 100
            DashTime = 1
            Dashs -= 1
        UseGravity = True
        if(DashTime > 0):
            UseGravity = False
            DashTime -= 1
            CameraMoveX += DashSpeed
        if(y_change < 20 and UseGravity == True):
          y_change += gravityforce           
        pos = 0
        IsGrounded = False
        x_change = CameraChangeX
        for clx in blocksw:
            if(clx-120+CameraMoveX < (x + -x_change) and (clx + 15 + CameraMoveX) > (x + -x_change) and y > blocksh[pos] - 51 + CameraMoveY and y < blocksh[pos] + CameraMoveY):
                CameraChangeX = 0
            if(clx-120+CameraMoveX < x and (clx + 15+CameraMoveX) > x  and (y + y_change) > blocksh[pos] - 61 + CameraMoveY and (y + y_change) < blocksh[pos] + CameraMoveY):
                y_change = 0
                Jumps = 2
                IsGrounded = True
                Dashs = 1
            
            pos += 1
        if y > 900:
            y = respawny
            x = respawnx
            CameraMoveX = 400
        y = y + y_change        
        
        CameraMoveX += CameraChangeX
        
            
        
       
        GameDisplay.fill(Black)
        pos = 0
        for bx in blocksw:
                 pygame.draw.rect(GameDisplay,Blue,[bx-100 + CameraMoveX,blocksh[pos]-50,120,50])
                 pos += 1      
        GameDisplay.blit(maincharimg,(x,y))
        pygame.display.update()
        clock.tick(30)
        
        
Gameloop()
pygame.quit()
quit()