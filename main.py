import pygame
from sys import exit
from ninja2 import Ninja2
from ninja2 import Zabuza
from ninja2 import Sasuke
from ninja2 import Ninja1
from ninja2 import Ninja3
import random
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load("narutotheme.mp3")
pygame.mixer.music.set_volume(0.4)
screen = pygame.display.set_mode((1024,462))
pygame.display.set_caption("Naruto Battlegrounds")
font = pygame.font.Font("njnaruto.ttf", 55)
text = pygame.font.Font("njnaruto.ttf", 22)
text2 = pygame.font.Font("njnaruto.ttf", 27)
healthtext = pygame.font.Font("njnaruto.ttf", 20)
icon = pygame.image.load("images/shuriken.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

firstEnemy = Ninja2()
firstEnemy.x = 30
secondEnemy = Ninja2()
secondEnemy.x = 1000
killCount = 0

entityList = [firstEnemy, secondEnemy]
timer = 0

load_screen = True
game_started = False
character_select = False

# load screen
loadbackground = pygame.image.load("images/loadscreen/background.jpg").convert()
naruto_logo = pygame.image.load("images/loadscreen/naruto.png").convert_alpha()
naruto_rect = naruto_logo.get_rect(midbottom = (530, 270))
battlegrounds = font.render("Battlegrounds", False, (3,3,3))
battlegrounds_rect = battlegrounds.get_rect(midbottom = (530, 335))
space_to_continue = text.render("Press space to continue", False, (0,0,0))
space_to_continue_rect = space_to_continue.get_rect(midbottom = (530, 400))

# character select
sasuke_name = text2.render("Sasuke", False, (0,0,0))
sasuke_name_rect = sasuke_name.get_rect(midbottom = (100, 300))
sasuke_profile = pygame.image.load("images/ninjas/Sasuke/profilepicture.png").convert_alpha()
sasuke_profile = pygame.transform.scale(sasuke_profile, (110, 75))
sasuke_profile_rect = sasuke_profile.get_rect(midbottom = (100, 265))
zabuza_name = text2.render("Zabuza", False, (0,0,0))
zabuza_name_rect = zabuza_name.get_rect(midbottom = (250, 300))
zabuza_profile = pygame.image.load("images/ninjas/Zabuza/profilepicture.png").convert_alpha()
zabuza_profile = pygame.transform.scale(zabuza_profile, (110, 75))
zabuza_profile_rect = zabuza_profile.get_rect(midbottom = (250, 265))

# healthbar and killcount and death text
death_text = text2.render("People  only  share  one  common  fate,  death.  -  Neji  Hyuga", False, (0,0,0))
death_text_rect = death_text.get_rect(midbottom = (530, 150))
restart_text = text.render("Press space to restart", False, (0,0,0))
restart_text_rect = restart_text.get_rect(midbottom = (530, 400))
kill_count_text = text.render(f"Killcount:  {killCount}", False, (0,0,0))
kill_count_text_rect = kill_count_text.get_rect(midbottom = (530, 200))

def draw_healthbar():
    health_text = healthtext.render(f"HEALTH: {str(int(player.health))}", False, (22, 253, 0))
    health_text_rect = health_text.get_rect(midleft = (0,25))
    screen.blit(health_text, health_text_rect)



def drawLoadScreen():
    screen.blit(loadbackground, (0,0))
    screen.blit(naruto_logo, naruto_rect)
    screen.blit(battlegrounds, battlegrounds_rect)
    screen.blit(space_to_continue, space_to_continue_rect)

def drawCharacterSelect():
    screen.blit(loadbackground, (0,0))
    screen.blit(sasuke_name, sasuke_name_rect)
    screen.blit(zabuza_name, zabuza_name_rect)
    screen.blit(zabuza_profile, zabuza_profile_rect)
    screen.blit(sasuke_profile, sasuke_profile_rect)

def drawDeathScreen():
    screen.fill((234,152,40))
    screen.blit(death_text, death_text_rect)
    screen.blit(restart_text, restart_text_rect)
    screen.blit(kill_count_text, kill_count_text_rect)

def spawnEnemy(time):
    time = pygame.time.get_ticks()
    if time % 350 == 0:
        entityList.append(Ninja2())
        myInt = random.randint(0,1)
        if myInt == 0:
            entityList[-1].x = 1000
        else:
            entityList[-1].x = 30
        print("ENEMY SPAWNED")
    elif time % 1250 == 0:
        entityList.append(Ninja1())
        myInt = random.randint(0, 1)
        if myInt == 0:
            entityList[-1].x = 1000
        else:
            entityList[-1].x = 30
    elif time % 2000 == 0:
        entityList.append(Ninja3())
        myInt = random.randint(0, 1)
        if myInt == 0:
            entityList[-1].x = 1000
        else:
            entityList[-1].x = 30








mapSurface = pygame.image.load("images/maps/hiddensandvillage.png").convert()

pygame.mixer.music.play()
while True:


    if load_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT is the X button event
                pygame.quit()
                exit()  # from sys module
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            load_screen = False
            character_select = True
            time.sleep(0.25)
        drawLoadScreen()
    elif character_select:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT is the X button event
                pygame.quit()
                exit()  # from sys module
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if sasuke_profile_rect.collidepoint(mouse_pos):
                    player = Sasuke()
                    character_select = False
                    game_started = True
                    time.sleep(0.25)
                elif zabuza_profile_rect.collidepoint(mouse_pos):
                    player = Zabuza()
                    character_select = False
                    game_started = True
                    time.sleep(0.25)
        drawCharacterSelect()
    elif game_started:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT is the X button event
                pygame.quit()
                exit()  # from sys module
        if len(entityList) < 6:
            spawnEnemy(timer)
        # actual game sequence
        screen.blit(mapSurface, (0, 0))
        player.update()
        screen.blit(player.image, player.rect)
        for entity in entityList:
            if entity.image != 0:
                entity.update(player)
                screen.blit(entity.image, entity.rect)
                if entity.kunaiLbool:
                    screen.blit(entity.kunaiL, entity.kunai_rect_L)
                if entity.kunaiRbool:
                    screen.blit(entity.kunaiR, entity.kunai_rect_R)
                if entity.rect.colliderect(player.rect):
                    entity.takeHit(player)
                    player.takeHit(entity)
                    if entity.image == 0:
                        entityList.remove(entity)
                        killCount += 1
                    if player.death:
                        game_started = False
                        kill_count_text = text.render(f"Killcount:  {killCount}", False, (0, 0, 0))
                        kill_count_text_rect = kill_count_text.get_rect(midbottom=(530, 200))
                if entity.kunaiLbool or entity.kunaiRbool:
                    if entity.kunai_rect_L.colliderect(player.rect) or entity.kunai_rect_R.colliderect(player.rect):
                        player.takeHit(entity)

        # update healthbar
        draw_healthbar()

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT is the X button event
                pygame.quit()
                exit()  # from sys module
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            killcount = 0
            load_screen = True
            time.sleep(0.25)
        drawDeathScreen()
    pygame.display.update()  # update everything
    clock.tick(60)  # set frame rate






