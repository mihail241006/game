'''# Разработай свою игру в этом файл
import pygame
from pygame import *

back = (50, 50, 50)
mw = pygame.display.set_mode((700, 500))
display.set_caption('Снюс')
run = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__ (self, picture, w, h, x, y):
        super().__init__()
        self.image=transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        mw.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        if player.rect.x <= 700-50 and player.x_speed > 0 or player.rect.x >= 0 and player.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.right, p.rect.left)
        if player.rect.y <= 500-65 and player.y_speed > 0 or player.rect.y >= 0 and player.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self,barriers,False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.button = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def fire(self):
        bullet = Bullet('bullet.png', 15,20,self.rect.right, self.rect.centery,15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def __init__(self, picture, w, h, x, y, speed):
        super().__init__(picture, w, h, x, y)
        self.speed = speed
        self.direction = 'left'
    def update(self):
        if self.rect.x <= 400:
            self.direction = 'right'
        if self.rect.y >= 650:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Bullet(sprite.Sprite):
    def __init__(self, picture, w, h, x, y, speed):
        super().__init__(picture, w, h, x, y)
        self.speed = speed
    def update (self):
        self.rect.x += self.speed
        if self.rect.x > 700 + 10:
            self.kill()


wall_1 = GameSprite('294wabk65pwb.png', 350,50,175,220)
wall_2 = GameSprite('294wabk65pwb.png', 50,350,330,70)
player = Player('pngwing.com.png',50,65,70,210,0,0)
final = GameSprite('egggg.png',50,65,550,210)
enemy = Enemy('pngegg.png',50,65,570,410,5)
win = transform.scale(image.load('340ada26-49f7-48f1-a572-b27dd6ec766b.jpg'),(700,500))
lose = transform.scale(image.load('EGS_DOOM3_idSoftwarePanicButton_S1_2560x1440-e29ea97ef0c5689b6ee1b5ae12d9a1bb.jpg'),(700,500))

barriers = sprite.Group()
barriers.add(wall_1)
barriers.add(wall_2)

bullets = sprite.Group()

enemies = sprite.Group()
enemies.add(enemy)

while run:
    time.delay(50)
    
    for e in event.get():
        if e.type == QUIT: 
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                player.y_speed = -5
            elif e.key == K_DOWN:
                player.y_speed = +5
            elif e.key == K_LEFT:
                player.x_speed = -5
            elif e.key == K_RIGHT:
                player.x_speed = +5
            elif e.key == K_SPACE:
                player.fire()
        elif e.type == KEYUP:
            if e.key == K_UP:
                player.y_speed = 0
            elif e.key == K_DOWN:
                player.y_speed = 0
            elif e.key == K_LEFT:
                player.x_speed = 0
            elif e.key == K_RIGHT:
                player.x_speed = 0



    if finish != True:
        mw.fill(back)
        player.update()
        bullets.update()
        player.reset()
        bullets.draw(mw)
        barriers.draw(mw)
        final.reset()
        sprite.groupcollide(bullets,enemies,True,True)
        enemies.update()
        enemies.draw(mw)
        sprite.groupcollide(bullets,barriers,True,False)
        if sprite.collide_rect(player, final):
            finish = True
            mw.blit(win,(0,0))
        elif sprite.spritecollide(player, enemies, False):
            finish = True
            mw.blit(lose,(0,0))

    
    display.update()'''
#bnjkuhtmtfckhcfr

from pygame import *

back = (50, 50, 50)
mw = display.set_mode((700, 500))
display.set_caption('Снюс')
run = True
finish = False

class GameSprite(sprite.Sprite):
    def __init__ (self, picture, w, h, x, y):
        super().__init__()
        self.image=transform.scale(image.load(picture),(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        mw.blit(self.image, (self.rect.x,self.rect.y))

class Player(GameSprite):
    def __init__(self, picture, w, h, x, y, x_speed, y_speed):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.x_speed = x_speed
        self.y_speed = y_speed
    def update(self):
        if player.rect.x <= 700-50 and player.x_speed > 0 or player.rect.x >= 0 and player.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0:
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.x_speed < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right)
        if player.rect.y <= 500-65 and player.y_speed > 0 or player.rect.y >= 0 and player.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self,barriers,False)
        if self.y_speed > 0:
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def fire(self):
        bullet = Bullet('bullet.png',15,20,self.rect.right, self.rect.centery,15)
        bullets.add(bullet)

class Enemy(GameSprite):
    def __init__(self, picture, w, h, x, y, speed):
        super().__init__(picture, w, h, x, y)
        self.speed = speed
        self.direction = 'left'
    def update(self):
        if self.rect.x <= 400:
            self.direction = 'right'
        if self.rect.x >= 650:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Bullet(GameSprite):
    def __init__(self, picture, w, h, x, y, speed):
        super().__init__(picture, w, h, x, y)
        self.speed = speed
    def update (self):
        self.rect.x += self.speed
        if self.rect.x > 700 + 10:
            self.kill()


wall_1 = GameSprite('294wabk65pwb.png', 350,50,175,220)
wall_2 = GameSprite('294wabk65pwb.png', 50,350,330,70)
player = Player('pngwing.com.png',50,65,70,210,0,0)
final = GameSprite('egggg.png',50,65,550,210)
enemy = Enemy('pngegg.png',50,65,570,410, 5)
win = transform.scale(image.load('340ada26-49f7-48f1-a572-b27dd6ec766b.jpg'),(700,500))
lose = transform.scale(image.load('EGS_DOOM3_idSoftwarePanicButton_S1_2560x1440-e29ea97ef0c5689b6ee1b5ae12d9a1bb.jpg'),(700,500))

barriers = sprite.Group()
barriers.add(wall_1)
barriers.add(wall_2)

bullets = sprite.Group()

enemies = sprite.Group()
enemies.add(enemy)

while run:
    time.delay(50)
    for e in event.get():
        if e.type == QUIT: 
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_UP:
                player.y_speed = -5
            elif e.key == K_DOWN:
                player.y_speed = 5
            elif e.key == K_LEFT:
                player.x_speed = -5
            elif e.key == K_RIGHT:
                player.x_speed = 5
            elif e.key == K_SPACE:
                player.fire()
        elif e.type == KEYUP:
            if e.key == K_UP:
                player.y_speed = 0
            elif e.key == K_DOWN:
                player.y_speed = 0
            elif e.key == K_LEFT:
                player.x_speed = 0
            elif e.key == K_RIGHT:
                player.x_speed = 0



    if finish != True:
        mw.fill(back)
        player.update()
        bullets.update()
        player.reset()
        bullets.draw(mw)
        barriers.draw(mw)
        final.reset()
        sprite.groupcollide(bullets,enemies,True,True)
        enemies.update()
        enemies.draw(mw)
        sprite.groupcollide(bullets,barriers,True,False)

        if sprite.collide_rect(player, final):
            finish = True
            mw.blit(win,(0,0))
        elif sprite.spritecollide(player, enemies, False):
            finish = True
            mw.blit(lose,(0,0))
        
        
    display.update()

