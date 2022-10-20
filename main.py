#添加血条，随机出现的怪兽
import sys,time,random,math,pygame
from pygame.locals import*
from pygame import mixer
import os
from start import startInterface,Button
from library import*

filepath = 'moonlight.wav'
mixer.init()
mixer.music.load(filepath)
mixer.music.play(start=0.0)

green = (144,201,120)
white = (255,255,255)
tile_size =100
#loading images
stone_img = pygame.image.load('stone.png')
grass_img = pygame.image.load('grass.jpg')
key_img = pygame.image.load("key.png")
enemy_img  = pygame.image.load("monster.png")
med_img = pygame.image.load('potion.png')


#创建空瓷砖列表 row 行
world_data = []
for row in range(8):
    r = [0]*12
    world_data.append(r)
#map
map =[
0,0,0,0,0,0,0,0,0,0,
1,1,1,1,1,1,1,1,0,0,
0,0,0,0,0,0,0,1,0,0,
0,1,1,1,0,1,0,0,0,0,
0,0,0,0,0,1,0,0,0,0,
0,0,1,1,1,1,1,1,1,1,
0,0,1,0,0,0,0,0,0,0,
0,0,1,1,1,1,1,1,0,0,
0,0,0,0,0,0,0,0,0,0]

clock=pygame.time.Clock()



#画格子
def draw_grid():
        for c in range(12):
            # 垂直线
            pygame.draw.line(screen, green, (c * tile_size, 0), (c * tile_size, 800))
        for c in range(10):
            # 水平线
            pygame.draw.line(screen, white, (0, c * tile_size), (1200, c * tile_size))
def draw_world():

            # width
            w = 100
            for g in range(8):  # row
                for h in range(12):
                   if world_data[g][h]>0:
                       if world_data[g][h]==0:
                          skin = pygame.transform.scale(grass_img, (tile_size, tile_size))
                          screen.blit(skin, (h * tile_size, row * tile_size))
                       elif world_data[g][h]== 1:  # stone
                           skin = pygame.transform.scale(stone_img, (tile_size, tile_size))
                           screen.blit(skin, (h * tile_size, row * tile_size))



def text_objects(font, x, y, text, color=(255, 255,255), shadow=True):
    textSurface = font.render(text, True, white)
    screen = pygame.display.get_surface()
    screen.blit(textSurface, (x, y))

def game_clock():
    clock_ = 60

def calc_velocity(direction, vel=1.0):
    velocity = Point(0, 0)
    # 上
    if direction == 0:
        velocity.y = -vel
    # 右
    elif direction == 2:
        velocity.x = vel
    # 下
    elif direction == 4:
        velocity.y = vel
    # 左
    elif direction == 6:
        velocity.x = -vel
    return velocity



# turning
def reverse_direction(sprite):
    if sprite.direction == 0:
        sprite.direction = 4
    elif sprite.direction == 2:
        sprite.direction = 6
    elif sprite.direction == 4:
        sprite.direction = 0
    elif sprite.direction == 6:
        sprite.direction = 2



if __name__ == "__main__" :
#initiallize
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("random monster&blood")
    font = pygame.font.Font(None,25)
    framerate = pygame.time.Clock()

    #creat sprite groups
    player_group = pygame.sprite.Group()
    monster_group = pygame.sprite.Group()
    health_group = pygame.sprite.Group ()


    #create monster sprite
   #monster_image = pygame.image.load("monster.png").convert_alpha()
    for n in range(0,14): #create 5 monsters
       monster = MySprite('monster.png')
       monster.load('monster.png',135,135,8)
       monster.position = random.randint(100,1100),random.randint(100,600)
       monster.direction = random.randint(0,3)*2
       monster_group.add(monster)

#create player sprite

    player=MySprite('player.png')
    player.load('player.png',100,100,8)
    player.position = 80,80
    player.direction= 4
    player_group.add(player)


     #health sprite created
    health = MySprite('potion.png')
    health.load('potion.png',146,146,1)
    health.position = 400,300
    health_group.add(health)

    game_over = False
    player_moving =  False
    player_health = 90
    player_stamina = 150
    monster_health = 50
    stamina_punish = False


      #loop
    run=True
    while True:
        framerate.tick(60)
        ticks = pygame.time.get_ticks()
        pygame.time.get_ticks()



        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               sys.exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_ESCAPE]:sys.exit()

        # player moving
        elif stamina_punish == True: 
            player_stamina += 0.6
            if player_stamina>=150:
                stamina_punish=False   
        
        elif player_stamina <=0 :
            player_moving = False
            stamina_punish = True

        elif   key[K_w] or key[K_UP]:
                player.direction = 0
                player_moving = True
                player_stamina-=2
        elif    key[K_d] or key[K_RIGHT]:
                player.direction = 2
                player_moving = True
                player_stamina-=2
        elif    key[K_s] or key[K_DOWN]:
                player.direction = 4
                player_moving = True
                player_stamina-=2
        elif key[K_a] or key[K_LEFT]:
                player.direction = 6
                player_moving = True
                player_stamina-=2

        else:
                player_moving = False
                if player_stamina < 150:
                    player_stamina += 0.6
              

            
        if not game_over:
            pass

            if not player_moving:
             # if player didn't press, he won't move
                   player.frame = player.first_frame = player.last_frame
            else:
             # moving speed
                  player.velocity = calc_velocity(player.direction, 2.25)
                  player.velocity.x *= 2.25
                  player.velocity.y *= 2.25


    # player updated
        player_group.update(ticks, 50)
     # moving(player)
        if player_moving:
           player.X += player.velocity.x
           player.Y += player.velocity.y
           if player.X < 0:
               player.X = 0
           elif player.X > 1100:
                player.X = 1100
           if player.Y < 0:
                player.Y = 0
           elif player.Y > 600:
               player.Y = 600
        # monsters updated

        # deal with the monster
        for z in monster_group:
            z.first_frame = z.direction * z.columns
            z.last_frame = z.first_frame + z.columns - 1
            if z.frame < z.first_frame:
                z.frame = z.first_frame
            z.velocity = calc_velocity(z.direction)
            z.X += z.velocity.x
            z.Y += z.velocity.y
            if z.X < 0 or z.X > 1100 or z.Y < 0 or z.Y > 600:
              reverse_direction(z)
            # 检测玩家是否与monster发生碰撞
        attacker = None
        attacker = pygame.sprite.spritecollideany(player, monster_group)
        if attacker is not None:
        # 若碰撞，检测
            if pygame.sprite.collide_rect_ratio(0.5)(player, attacker):
                player_health -= 30
                if  attacker.X < player.X:
                    attacker.X -= 40
                elif attacker.X > player.X:
                    attacker.X += 40
                if  attacker.Y < player.Y:
                    attacker.Y -= 40
                elif  attacker.Y > player.Y:
                    attacker.Y += 40
            else:
                attacker = None
        # health group updated
        health_group.update(ticks, 50)
        # player pick up the blood
        if pygame.sprite.collide_rect_ratio(0.5)(player, health):
           player_health += 30
           if player_health > 90:
               player_health = 90
           health.position = random.randint(0, 700), random.randint(0, 500)
    # player dead
        if player_health <= 0:
            game_over = True


        image = ("background.png")
        background_img = pygame.image.load(image).convert()
        screen.blit(background_img,(0,0))
        monster_group.draw(screen)
        player_group.draw(screen)
        health_group.draw(screen)


        game_clock()


        # draw the blood of the player
        pygame.draw.rect(screen, (255,0,0), Rect(10, 720, player_health * 2, 25))
        pygame.draw.rect(screen, (255,255,255), Rect(10, 720, 180, 25), 2)
        
        #draw the stamina of the player
        pygame.draw.rect(screen, (50, 150, 50, 180), Rect(10, 750, player_stamina * 2, 25))
        pygame.draw.rect(screen, (255,255,255), Rect(10, 750, 300, 25), 2)
        
        print_text(font,200,725,'blood')
        print_text(font,320,760,'stamina')
        print_text(font,250,725,'(You can recover your life with medicine)')
        print_text(font,400,760,"attention: player can't move when stamina is depleted")
        print_text(font,0,0,"your position"+str(player))
        print_text(font, 1000, 0, '   Please try your best to')
        print_text(font, 1100, 25, ' Stay Alive!')
        draw_world()
        if game_over:
            screen.fill((0,0,0))
            gameover_img = pygame.image.load('gameover.png')
            gameover_img = pygame.transform.scale(gameover_img,(400,200))


            screen.blit(gameover_img,(370,290))
            print_text(font,9,0,"you're dead!")
        pygame.display.update()