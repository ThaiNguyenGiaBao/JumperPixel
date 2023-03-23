import pygame as pg
from sys import exit
import random
from pygame import mixer

def display_score():
    ctime=(pg.time.get_ticks()-timebefore)/150
    num_score=font.render(f'Score: {int(ctime)}',False,"red")
    num_score_rect=num_score.get_rect(topleft=(500+110 ,10))
    screen.blit(num_score,num_score_rect)
    return ctime
def display_begin():
    screen.fill((94,129,164))
    screen.blit(player_stand,player_stand_rect)
    screen.blit(title,title_rect)
    screen.blit(start,start_rect)
    screen.blit(instrucstion,instrucstion_rect)
def display_end(Score):
    screen.fill((94,129,164))
    screen.blit(player_stand,player_stand_rect)
    screen.blit(title,title_rect)
    screen.blit(instrucstion,instrucstion_rect)
    num_score=font.render(f'Score: {int(Score)}',False,"red")
    num_score_rect=num_score.get_rect(center=(400,300))
    screen.blit(num_score,num_score_rect)
def playeranimation():
    global p_index, player
    if player_rect.bottom<300:
        player=player_jump
    else:
        p_index+=0.1
        player=player_walk[int(p_index)%2]
def flyanimation():
    global f_index, fly
    f_index+=0.1
    fly=flyi[int(f_index)%2]
def snailanimation():
    global s_index, snail
    s_index+=0.05
    snail=Snail[int(s_index)%2]
def snail1animation():
    global s1_index, snail1
    s1_index+=0.05
    snail1=Snail1[int(s_index)%2]
def snail2animation():
    global s2_index, snail2
    s2_index+=0.05
    snail2=Snail2[int(s_index)%2]      
pg.init()
#sound background
mixer.music.load('audio/music.wav')
mixer.music.play(-1)
screen=pg.display.set_mode((800,400))
pg.display.set_caption("JUMPER")
clock=pg.time.Clock()
#declare variables
pos=600
pos_player=305
pos_fly=2000
gravity=13
jump=False
gameactive=False
start1=True
timebefore=0
Score=0
speedgame=5
press_space=0
gravity2=10
#import the asset to python
font=pg.font.Font('font/Pixeltype.ttf',40)

ground=pg.image.load('graphics/planet.jpg')
UFO=pg.image.load('graphics/UFO.png')
UFO=pg.transform.rotozoom(UFO,-10,0.05)
UFO_rect=UFO.get_rect(center=(50,300))
#For player animation
player_walk_1=pg.image.load('graphics/Player/player_walk_1a.png')
player_walk_2=pg.image.load('graphics/Player/player_walk_2a.png')
player_jump=pg.image.load('graphics/Player/jumpa.png')
p_index=0
player_walk=[player_walk_1, player_walk_2]
player=player_walk[p_index]
player_rect=player.get_rect(midbottom=(150,pos_player))
#
player_stand=pg.image.load('graphics/Player/player_stand.png')
player_stand=pg.transform.rotozoom(player_stand,0,2)
player_stand_rect=player_stand.get_rect(center=(400,170))
gameover=pg.image.load('graphics/gameover.png')
gameover=pg.transform.rotozoom(gameover,0,2)
gameover_rect=gameover.get_rect(center=(400,430))
#For fly animation
fly1=pg.image.load('graphics/Fly/Fly1.png')
fly1=pg.transform.rotozoom(fly1,0,0.5)
fly2=pg.image.load('graphics/Fly/Fly2.png')
fly2=pg.transform.rotozoom(fly2,0,0.5)
flyi=[fly1,fly2]
f_index=0
fly=flyi[f_index]
fly_rect=fly.get_rect(center=(pos_fly,150))

#Swamp snails
snaila=pg.image.load('graphics/snail/snail2.png').convert_alpha()
snailb=pg.image.load('graphics/snail/snail1.png').convert_alpha()
Snail=[snaila,snailb]
s_index=0
snail=Snail[s_index]
snail_rect=snail.get_rect(midbottom=(pos,300))

snail1a=pg.image.load('graphics/snail/snail2.png').convert_alpha()
snail1b=pg.image.load('graphics/snail/snail1.png').convert_alpha()
Snail1=[snail1a,snail1b]
s1_index=0
snail1=Snail1[s1_index]
snail1_rect=snail1.get_rect(midbottom=(pos,315))

snail2a=pg.image.load('graphics/snail/snail2.png').convert_alpha()
snail2b=pg.image.load('graphics/snail/snail1.png').convert_alpha()
Snail2=[snail2a,snail2b]
s2_index=0
snail2=Snail2[s2_index]
snail2_rect=snail2.get_rect(midbottom=(pos,310))

#For Starting menu
instrucstion=font.render('Press SPACE to run',False,'black')
instrucstion_rect=instrucstion.get_rect(center=(400,340))
title=font.render('PIXEL JUMPER',False,(111,196,169))
title_rect=title.get_rect(center=(400,70))
start=font.render('START',False,'red')
start_rect=start.get_rect(center=(400,300))

while True:
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            exit()   
        if gameactive: 
            if event.type==pg.KEYDOWN:# Using this method to avoid repetitions of getting key 
                if event.key==pg.K_SPACE :
                    jumpsound=mixer.Sound('audio/jump.mp3')
                    jumpsound.play()
                    jump=True 
                    press_space+=1
        else:
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_SPACE:
                    timebefore=pg.time.get_ticks()
                    gameactive=True
                    #initialize the position for snails
                    snail_rect.x=800
                    snail1_rect.x=1100
                    snail2_rect.x=1500
                    fly_rect.x=2000
                    gameover_rect.y=400
                    speedgame=5
                    start1=False
        
    if gameactive:      
        if int(Score)==50: speedgame=6
        if int(Score)==150: speedgame=7
        if int(Score)==300: speedgame=8
        if int(Score)==500: speedgame=10
        #screen.blit(sky,(0,-95)) #the order of layer:1
        screen.blit(ground,(0,-175)) #the order of layer:2 Note that the layer has higher order override the lower layer
        snailanimation()    
        screen.blit(snail,snail_rect)
        snail1animation()
        screen.blit(snail1,snail1_rect)
        snail2animation()
        screen.blit(snail2,snail2_rect)
        playeranimation()
        screen.blit(player,player_rect)
        flyanimation()
        screen.blit(fly,fly_rect)
        #screen.blit(UFO,UFO_rect)
        #using function to print out the score 
        display_score()   
        Score=display_score()
        if jump and press_space!=2:
            player_rect.bottom-=gravity
            gravity-=0.65
        if player_rect.bottom>302:
            jump=False
            player_rect.bottom=300
            gravity=13
            press_space=0
            gravity2=10
        if press_space==2:
            player_rect.bottom-=gravity2
            gravity2-=0.65
#make ostacels move
        snail_rect.left= snail_rect.left-speedgame
        if  snail_rect.left<=-100:
            snail_rect.left=random.randint(900,1200)
        snail1_rect.left= snail1_rect.left-speedgame
        if  snail1_rect.left<=-100:
            snail1_rect.left=random.randint(1100,1300)
        snail2_rect.left= snail2_rect.left-speedgame
        if  snail2_rect.left<=-100:
            snail2_rect.left=random.randint(1000,1300)
        fly_rect.x-=speedgame+1
        if fly_rect.x<-100:
            fly_rect.x=2000+random.randint(0,500)
        if(fly_rect.colliderect(player_rect) or snail_rect.colliderect(player_rect)or snail1_rect.colliderect(player_rect)or snail2_rect.colliderect(player_rect)):
            gameactive=False
            hit=mixer.Sound('audio/hit.ogg')    
            hit.play()
    else:
        
        key=pg.key.get_pressed()
        if start1:
            display_begin() 
            
        else:
            player_rect.bottom+=5
            gameover_rect.y-=6.5
            #screen.blit(sky,(0,-95)) #the order of layer:1
            screen.blit(ground,(0,-175)) #the order of layer:2 Note that the layer has higher order override the lower layer
            screen.blit(snail,snail_rect)
            screen.blit(snail1,snail1_rect)
            screen.blit(snail2,snail2_rect)
            screen.blit(fly,fly_rect)
            screen.blit(player,player_rect)
            screen.blit(gameover,gameover_rect)
            #                            screen.blit(UFO,UFO_rect)
            if player_rect.bottom>500:
                pg.time.delay(500)
                display_end(Score)
                pg.time.delay(1000)
    pg.display.update()
    clock.tick(60)