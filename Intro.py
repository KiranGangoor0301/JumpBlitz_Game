import pygame
from sys import exit

def calculateTime():
    currentTime=pygame.time.get_ticks()- startTime
    text_surface=text_font.render('Score : {}'.format(int(currentTime/1000)),False,'Black')
    text_rect=text_surface.get_rect(midtop=(400,30))
    screen.blit(text_surface,text_rect)

pygame.init()
screen=pygame.display.set_mode((800,400))
pygame.display.set_caption("Fighter")
clock=pygame.time.Clock()
text_font=pygame.font.Font('font/Pixeltype.ttf',50)

global score
sky_image=pygame.image.load('graphics/Sky.png')
ground_image=pygame.image.load('graphics/ground.png')

score=1


snail_surface=pygame.image.load('graphics/snail/snail1.png')
snail_X_pos=700
snail_rect=snail_surface.get_rect(topright=(snail_X_pos,270))

player_surf=pygame.image.load('graphics/Player/player_walk_1.png')
player_rect=player_surf.get_rect(midbottom=(80,300))
player_gravity=0

game_active=True
startTime=0

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
                pygame.quit()
                exit()
        # if events.type == pygame.MOUSEMOTION:
        #      if player_rect.collidepoint(events.pos):
        #           print("Collision")
        if game_active:
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    if player_rect.bottom >= 300:
                        player_gravity=-21
                        
                        
            if events.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(events.pos):
                    if player_rect.bottom >= 300:
                        player_gravity=-20
        else:
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_SPACE:
                    game_active=True
                    snail_rect.right=900
                    startTime=pygame.time.get_ticks()
    # pygame.draw.line(screen,'Black',(0,0),(800,400),5)
    if game_active:
        screen.blit(sky_image,(0,0))
        screen.blit(ground_image,(0,300))
        calculateTime()
        snail_rect.right=snail_rect.right-4
        if snail_rect.left < -100:
            screen.blit(snail_surface,snail_rect)
            snail_X_pos=900
            snail_rect=snail_surface.get_rect(topright=(snail_X_pos,270))
        else:
            screen.blit(snail_surface,snail_rect)
        player_gravity=player_gravity+1
        player_rect.y+=player_gravity
        if player_rect.bottom >=300:
            player_rect.bottom=300
        screen.blit(player_surf,player_rect)
        if snail_rect.colliderect(player_rect):
            game_active=False
    else:
        screen.fill('Yellow')

        returnGame=text_font.render("Press Space Bar",False,'Black')
        returnRect=returnGame.get_rect(midtop=(400,50))
        screen.blit(returnGame,returnRect)
        Game1=text_font.render("To",False,'Black')
        rect=Game1.get_rect(midtop=(400,100))
        screen.blit(Game1,rect)
        Game2=text_font.render("Restart the Game",False,'Black')
        rect1=Game2.get_rect(midtop=(400,150))
        screen.blit(Game2,rect1)
        Game2=text_font.render("Restart the Game",False,'Black')
        rect1=Game2.get_rect(midtop=(400,150))
        screen.blit(Game2,rect1)

    pygame.display.update()
    clock.tick(60)