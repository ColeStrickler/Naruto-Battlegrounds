import pygame
import random


class Ninja1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.idle1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/idle1.png")).convert_alpha()
        self.idle2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/idle2.png")).convert_alpha()
        self.idle3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/idle2.png")).convert_alpha()
        self.idle4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/idle4.png")).convert_alpha()
        self.idleL = [self.idle1, self.idle2, self.idle3, self.idle4]
        self.idleR = [pygame.transform.flip(image, True, False) for image in self.idleL]
        self.charge1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/charge1.png")).convert_alpha()
        self.charge2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/charge2.png")).convert_alpha()
        self.charge3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/charge3.png")).convert_alpha()
        self.chargeR = [self.charge1, self.charge2, self.charge3, self.charge1, self.charge2, self.charge3]
        self.chargeL = [pygame.transform.flip(image, True, False) for image in self.chargeR]
        self.attack1 = False
        self.chargeCheck = 0
        self.charge_cooldown = 1200
        self.attack1_damage = 1200
        self.punch1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/punch1.png")).convert_alpha()
        self.punch2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/punch2.png")).convert_alpha()
        self.punch3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/punch3.png")).convert_alpha()
        self.punch4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/punch4.png")).convert_alpha()
        self.punchL = [self.punch1, self.punch2, self.punch3, self.punch4]
        self.punchR = [pygame.transform.flip(image, True, False) for image in self.punchL]
        self.attack2 = False
        self.punchCheck = 0
        self.punch_cooldown = 600
        self.attack2_damage = 450
        self.teleport1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/teleport1.png")).convert_alpha()
        self.teleport2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/teleport2.png")).convert_alpha()
        self.teleportRtoL = [self.teleport1, self.teleport2, pygame.transform.flip(self.teleport2, True, False), pygame.transform.flip(self.teleport1, True, False)]
        self.teleportLtoR = [pygame.transform.flip(self.teleport1, True, False), pygame.transform.flip(self.teleport2, True, False), self.teleport2, self.teleport1]
        self.attack3 = False
        self.attack3_damage = 0
        self.teleportCheck = 0
        self.teleport_cooldown = 2000
        self.throw1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/throw1.png")).convert_alpha()
        self.throw2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/throw2.png")).convert_alpha()
        self.throw3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/throw3.png")).convert_alpha()
        self.throwR = [self.throw1, self.throw2, self.throw3]
        self.throwL = [pygame.transform.flip(image, True, False) for image in self.throwR]
        self.attack4 = False # always make kunai throws attack4
        self.throwCheck = 0
        self.throw_cooldown = 1000
        self.attack4_damage = 800
        self.kunaiL = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/kunai.png").convert_alpha())
        self.kunai_rect_L = self.kunaiL.get_rect(midbottom = (-20, 0))
        self.kunaiR = pygame.transform.flip(self.kunaiL, True, False)
        self.kunai_rect_R = self.kunaiR.get_rect(midbottom=(-20, 0))
        self.kunaiLbool = False
        self.kunaiRbool = False
        self.damage1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/damage1.png").convert_alpha())
        self.damage2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/damage2.png").convert_alpha())
        self.damage3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/damage3.png").convert_alpha())
        self.damage4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/damage4.png").convert_alpha())
        self.damage5 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja1/damage5.png").convert_alpha())
        self.damageR = [self.damage1, self.damage2, self.damage3, self.damage4, self.damage5]
        self.damageL = [pygame.transform.flip(image, True, False) for image in self.damageR]
        self.takingDamage = False
        self.x = -40
        self.y = 300
        self.speed = 3
        self.health = 20000
        self.Index = 0
        self.image = self.idle1
        self.rect = self.image.get_rect(midbottom = (self.x,self.y))
        self.facing_left = True
        self.currentAnimation = self.idleL
        self.move_chosen = False
        self.moveCheck = 0
        self.moveTimer = 1400

    def ai(self, player):
        self.move_chosen = False
        if (int(pygame.time.get_ticks()) - self.moveCheck) > self.moveTimer and not self.takingDamage:
            self.moveCheck = int(pygame.time.get_ticks() / 1000)
            if player.x > self.x:
                if not self.attack2 and not self.attack3 and not self.attack1 and not self.attack4:
                    self.facing_left = False
                distance = player.x - self.x
            else:
                self.facing_left = True
                distance = self.x - player.x
            myInt = random.randint(0, 100)
            secondInt = random.randint(0, 100)
            if distance > 300:
                if myInt <= 2 and secondInt <= 25:
                    self.throw()
                elif myInt >= 5 and secondInt >= 95:
                    self.teleport()
                elif myInt <= 2 and secondInt >= 9:
                    self.charge()
            elif 300 >= distance > 80:
                if myInt <= 10 and secondInt <= 5:
                    self.teleport()
                if myInt == 0 and secondInt <= 3:
                    self.charge()
            else:
                if myInt <= 5:
                    self.teleport()
                elif 5 < myInt <= 10:
                    self.charge()
                elif 15 < myInt <= 18:
                    self.throw()
                elif myInt == 19:
                    self.punch()

    def animation_state(self):
        if self.move_chosen:
            self.Index = 0
        self.move_chosen = False
        if not self.takingDamage:
            self.Index += 0.15
        elif self.takingDamage:
            self.Index += 0.08

        if self.Index > len(self.currentAnimation):
            self.Index = 0
            if self.currentAnimation == self.throwR or self.currentAnimation == self.throwL:
                if self.facing_left:
                    self.kunaiLbool = True
                    self.kunai_rect_L.x = self.x + 3
                    self.kunai_rect_L.y = self.y - 45
                else:
                    self.kunaiRbool = True
                    self.kunai_rect_R.x = self.x - 3
                    self.kunai_rect_R.y = self.y - 45
            if self.facing_left:
                self.currentAnimation = self.idleL
            else:
                self.currentAnimation = self.idleR
            self.attack4 = False
            self.attack2 = False
            self.attack3 = False
            self.attack1 = False
            self.takingDamage = False
        if self.kunaiRbool:
            self.kunai_rect_R.x += 14
            if self.kunai_rect_R.x > 1430:
                self.kunaiRbool = False
                self.kunai_rect_R.x = -20
        if self.kunaiLbool:
            self.kunai_rect_L.x -= 14
            if self.kunai_rect_L.x < 0:
                self.kunaiLbool = False
                self.kunai_rect_L.x = 1450
        if self.attack3:
            if self.facing_left and int(self.Index) == 3:
                self.x -= 55
            elif not self.facing_left and int(self.Index) == 3:
                self.x += 55
        if self.attack1:
            if self.facing_left:
                self.x -= 4
            else:
                self.x += 4


        self.image = self.currentAnimation[int(self.Index)]
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))

    def takeHit(self, player):
        if player.attack1 and not self.takingDamage:
            self.takingDamage = True
            self.health -= player.attack1_damage
        elif player.attack4 and not self.takingDamage:
            self.health -= player.attack4_damage
            self.takingDamage = True
        elif player.attack2 and not self.takingDamage:
            self.health -= player.attack2_damage
            self.takingDamage = True
        elif player.attack3 and not self.takingDamage:
            self.health -= player.attack3_damage
            self.takingDamage = True
        if self.takingDamage:
            if self.facing_left:
                self.currentAnimation = self.damageR
            else:
                self.currentAnimation = self.damageL
        if self.health <= 0:
            self.image = 0

    def charge(self):
        if not self.attack4 and not self.attack3 and not self.attack2 and not self.takingDamage and (pygame.time.get_ticks() - self.chargeCheck) > self.charge_cooldown:
            self.attack1 = True
            self.chargeCheck = pygame.time.get_ticks()
            if self.facing_left:
                self.currentAnimation = self.chargeL
            else:
                self.currentAnimation = self.chargeR
            self.move_chosen = True
    def punch(self):
        if not self.attack4 and not self.attack3 and not self.attack1 and not self.takingDamage and (pygame.time.get_ticks() - self.punchCheck) > self.punch_cooldown:
            self.attack2 = True
            self.punchCheck = pygame.time.get_ticks()
            if self.facing_left:
                self.currentAnimation = self.punchL
            else:
                self.currentAnimation = self.punchR
            self.move_chosen = True
    def teleport(self):
        if not self.attack4 and not self.attack1 and not self.attack2 and not self.takingDamage and (pygame.time.get_ticks() - self.teleportCheck) > self.teleport_cooldown:
            self.attack3 = True
            self.teleportCheck = pygame.time.get_ticks()
            if self.facing_left:
                self.currentAnimation = self.teleportRtoL
            else:
                self.currentAnimation = self.teleportLtoR
            self.move_chosen = True
    def throw(self):
        if not self.attack3 and not self.attack1 and not self.attack2 and not self.takingDamage and (pygame.time.get_ticks() - self.throwCheck) > self.throw_cooldown:
            self.attack4 = True
            self.throwCheck = pygame.time.get_ticks()
            if self.facing_left:
                self.currentAnimation = self.throwL
                self.kunaiLbool = True
            else:
                self.currentAnimation = self.throwR
                self.kunaiRbool = True
            self.move_chosen = True
    def update(self, player):
        self.ai(player)
        self.animation_state()

class Ninja2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.idle1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/idle1.png").convert_alpha())
        self.idle2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/idle2.png").convert_alpha())
        self.idle3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/idle3.png").convert_alpha())
        self.idle = [self.idle1, self.idle2, self.idle3]
        self.idleR = [pygame.transform.flip(image, True, False) for image in self.idle]
        self.crawl1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/crawl1.png").convert_alpha())
        self.crawl2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/crawl2.png").convert_alpha())
        self.crawl3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/crawl3.png").convert_alpha())
        self.crawl4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/crawl4.png").convert_alpha())
        self.crawl5 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/crawl5.png").convert_alpha())
        self.crawlR = [self.crawl1, self.crawl2, self.crawl3, self.crawl4, self.crawl5]
        self.crawlL = [pygame.transform.flip(image, True, False) for image in self.crawlR]
        self.crawling = False
        self.punch1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/punch1.png").convert_alpha())
        self.punch2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/punch2.png").convert_alpha())
        self.punch3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/punch2.png").convert_alpha())
        self.punchL = [self.punch1, self.punch2, self.punch3]
        self.punchR = [pygame.transform.flip(image, True, False) for image in self.punchL]
        self.attack1 = False
        self.punch_cooldown = 350
        self.punchCheck = 0
        self.attack1_damage = 700
        self.roll1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/roll1.png").convert_alpha())
        self.roll2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/roll2.png").convert_alpha())
        self.roll = [self.roll1, self.roll2]
        self.attack2 = False
        self.attack2_damage = 400
        self.throw1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/throwing1.png").convert_alpha())
        self.throw2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/throwing2.png").convert_alpha())
        self.throw3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/throwing3.png").convert_alpha())
        self.throw4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/throwing4.png").convert_alpha())
        self.throwL = [self.throw1, self.throw2, self.throw3, self.throw4]
        self.throwR = [pygame.transform.flip(image, True, False) for image in self.throwL]
        self.attack4 = False
        self.throw_cooldown = 1000
        self.throwCheck = 0
        self.attack4_damage = 800
        self.kunaiL = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/kunai.png").convert_alpha())
        self.kunai_rect_L = self.kunaiL.get_rect(midbottom = (-20, 0))
        self.kunaiR = pygame.transform.flip(self.kunaiL, True, False)
        self.kunai_rect_R = self.kunaiR.get_rect(midbottom=(-20, 0))
        self.kunaiLbool = False
        self.kunaiRbool = False
        self.jump = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/jump.png").convert_alpha())
        self.jumpR = [self.jump, self.jump, self.jump, self.jump, self.jump,]
        self.jumpL = [pygame.transform.flip(self.jumpR[0], True, False)]
        self.jumping = False
        self.gravity = 0
        self.jumpkick1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/jumpkick1.png").convert_alpha())
        self.jumpkick2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/jumpkick2.png").convert_alpha())
        self.jumpkick3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/jumpkick3.png").convert_alpha())
        self.jumpkick4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/jumpkick4.png").convert_alpha())
        self.jumpkickR = [self.jumpkick1, self.jumpkick2, self.jumpkick3, self.jumpkick4]
        self.jumpkickL = [pygame.transform.flip(image, True, False) for image in self.jumpkickR]
        self.attack3 = False
        self.kickCheck = 0
        self.kick_cooldown = 1200
        self.attack3_damage = 1000
        self.damage1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/damage1.png").convert_alpha())
        self.damage2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/damage2.png").convert_alpha())
        self.damage3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/damage3.png").convert_alpha())
        self.damage4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/damage4.png").convert_alpha())
        self.damage5 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/damage5.png").convert_alpha())
        self.takedamageR = [self.damage1, self.damage2, self.damage3, self.damage4, self.damage5]
        self.takedamageL = [pygame.transform.flip(image, True, False) for image in self.takedamageR]
        self.takingDamage = False
        self.Index = 0
        self.image = self.idle1
        self.x = 20
        self.y = 300
        self.speed = 3
        self.health = 16000
        self.rect = self.image.get_rect(midbottom = (self.x,self.y))
        self.facing_left = True
        self.currentAnimation = self.idle
        self.move_chosen = False
        self.moveCheck = 0
        self.moveTimer = 1100

    def animation_state(self):
        if self.move_chosen:
            self.Index = 0
        self.move_chosen = False
        if not self.jumping:
            self.Index += 0.15
        elif self.attack3:
            self.Index += 0.18
        elif self.takingDamage:
            self.Index += 0.08
        if self.y < 300:
            self.y -= 10
            self.y += self.gravity
            self.gravity += 0.5
            if self.y > 300:
                self.gravity = 0
                self.y = 300
                self.jumping = False
                if self.facing_left:
                    self.currentAnimation = self.idle
                else:
                    self.currentAnimation = self.idleR

        if self.Index > len(self.currentAnimation):
            self.Index = 0
            if self.currentAnimation == self.throwR or self.currentAnimation == self.throwL:
                if self.facing_left:
                    self.kunaiLbool = True
                    self.kunai_rect_L.x = self.x + 3
                    self.kunai_rect_L.y = self.y - 45
                else:
                    self.kunaiRbool = True
                    self.kunai_rect_R.x = self.x - 3
                    self.kunai_rect_R.y = self.y - 45
            if not self.crawling:
                if self.facing_left:
                    self.currentAnimation = self.idle
                else:
                    self.currentAnimation = self.idleR
            self.crawling = False
            self.attack4 = False
            self.attack1 = False
            self.attack2 = False
            self.attack3 = False
            self.takingDamage = False
        if self.kunaiRbool:
            self.kunai_rect_R.x += 14
            if self.kunai_rect_R.x > 1430:
                self.kunaiRbool = False
                self.kunai_rect_R.x = -20
        if self.kunaiLbool:
            self.kunai_rect_L.x -= 14
            if self.kunai_rect_L.x < 0:
                self.kunaiLbool = False
                self.kunai_rect_L.x = 1450


        self.image = self.currentAnimation[int(self.Index)]
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))

    def ai(self, player):
        self.move_chosen = False
        if (int(pygame.time.get_ticks()) - self.moveCheck) > self.moveTimer and not self.takingDamage:
            self.moveCheck = int(pygame.time.get_ticks() / 1000)
            if player.x > self.x:
                if not self.attack1 and not self.attack3 and not self.attack4:
                    self.facing_left = False
                distance = player.x - self.x
            else:
                self.facing_left = True
                distance = self.x - player.x
            if distance > 80:
                myInt = random.randint(0,100)
                secondInt = random.randint(0, 100)
                if myInt == 0 and secondInt <= 25:
                    self.throwattack()
                elif myInt >= 1 and myInt <= 50:
                    self.moveAction()
            else:
                myInt = random.randint(0, 100)
                if myInt <= 5:
                    self.rollattack()
                elif 5 < myInt <= 10:
                    self.punchattack()
                elif 15 < myInt <= 18:
                    self.kickattack()
                elif myInt == 19:
                    self.jumpSelf()

    def takeHit(self, player):
        if player.attack1 and not self.takingDamage:
            self.takingDamage = True
            self.health -= player.attack1_damage
        elif player.attack4 and not self.takingDamage:
            self.health -= player.attack4_damage
            self.takingDamage = True
        elif player.attack2 and not self.takingDamage:
            self.health -= player.attack2_damage
            self.takingDamage = True
        elif player.attack3 and not self.takingDamage:
            self.health -= player.attack3_damage
            self.takingDamage = True
        if self.takingDamage:
            if self.facing_left:
                self.currentAnimation = self.takedamageR
            else:
                self.currentAnimation = self.takedamageL
        if self.health <= 0:
            self.image = 0

    def punchattack(self):
        if not self.attack4 and not self.attack2 and not self.jumping and not self.takingDamage and (pygame.time.get_ticks() - self.punchCheck) > self.punch_cooldown: # punch
            self.attack1 = True
            self.punchCheck = pygame.time.get_ticks()
            if self.facing_left:
                self.currentAnimation = self.punchL
            else:
                self.currentAnimation = self.punchR
            self.move_chosen = True

    def rollattack(self):
        if not self.attack4 and not self.attack1 and not self.takingDamage and not self.attack3: # roll
            self.attack2 = True
            self.currentAnimation = self.roll
            if self.facing_left:
                self.x -= 7
            else:
                self.x += 7
            self.move_chosen = True

    def throwattack(self):
        if not self.attack1 and not self.attack2 and not self.takingDamage and not self.jumping and (pygame.time.get_ticks() - self.throwCheck) > self.throw_cooldown: # throw
            self.throwCheck = pygame.time.get_ticks()
            self.attack4 = True
            if self.facing_left:
                self.currentAnimation = self.throwL
            else:
                self.currentAnimation = self.throwR
            self.move_chosen = True

    def jumpSelf(self):
        if self.rect.bottom == 300: # jump
            self.jumping = True
            if self.facing_left:
                self.currentAnimation = self.jumpL
            else:
                self.currentAnimation = self.jumpR
            self.move_chosen = True
            self.y -= 10

    def kickattack(self):
        if not self.takingDamage and (pygame.time.get_ticks() - self.kickCheck) > self.kick_cooldown: # jumpkick
            self.attack3 = True
            self.kickCheck = pygame.time.get_ticks()
            if self.facing_left:
                self.currentAnimation = self.jumpkickL
            else:
                self.currentAnimation = self.jumpkickR
            self.move_chosen = True

    def moveright(self):
        if not self.takingDamage: # move right
            self.crawling = True
            if not self.attack3 and not self.attack4 and not self.attack1:
                self.facing_left = False
                if not self.jumping and not self.attack2:
                    self.currentAnimation = self.crawlR
            self.x += self.speed

    def moveleft(self):
        if not self.takingDamage:  # move left
            self.crawling = True
            if not self.attack3 and not self.attack4 and not self.attack1:
                self.facing_left = True
                if not self.jumping and not self.attack2:
                    self.currentAnimation = self.crawlL
            self.x -= self.speed

    def moveAction(self):
        if self.facing_left:
            self.moveleft()
        else:
            self.moveright()

    def update(self, player):
        self.ai(player)
        self.animation_state()

class Ninja3(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.reappear1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/reappear1.png").convert_alpha())
        self.reappear2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/reappear2.png").convert_alpha())
        self.reappear3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/reappear3.png").convert_alpha())
        self.reappear4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/reappear4.png").convert_alpha())
        self.idleL = [self.reappear3, self.reappear4]
        self.idleR = [pygame.transform.flip(image, True, False) for image in self.idleL]
        self.reappearL = [self.reappear1, self.reappear2, self.reappear3, self.reappear4]
        self.reappearR = [pygame.transform.flip(image, True, False) for image in self.reappearL]
        self.attack4 = False
        self.reappear_check = 0
        self.reappear_cooldown = 0
        self.attack4_damage = 0
        self.charge1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/charge1.png").convert_alpha())
        self.charge2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/charge2.png").convert_alpha())
        self.charge3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/charge3.png").convert_alpha())
        self.chargeL = [self.charge1, self.charge2, self.charge3]
        self.chargeR = [pygame.transform.flip(image, True, False) for image in self.chargeL]
        self.attack1 = False
        self.chargeCheck = 0
        self.charge_cooldown = 0
        self.attack1_damage = 0
        self.kick1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/kick1.png").convert_alpha())
        self.kick2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/kick2.png").convert_alpha())
        self.kick3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/kick3.png").convert_alpha())
        self.kick4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/kick4.png").convert_alpha())
        self.kick5 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/kick5.png").convert_alpha())
        self.kick6 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/kick6.png").convert_alpha())
        self.kickL = [self.kick1, self.kick2, self.kick3, self.kick4, self.kick5, self.kick6]
        self.kickR = [pygame.transform.flip(image, True, False) for image in self.kickL]
        self.attack2 = False
        self.kickCheck = 0
        self.kick_cooldown = 0
        self.attack2_damage = 2200
        self.teleport1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/teleport1.png").convert_alpha())
        self.teleport2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/teleport2.png").convert_alpha())
        self.teleport3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/teleport3.png").convert_alpha())
        self.teleport4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/teleport4.png").convert_alpha())
        self.teleport5 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/teleport5.png").convert_alpha())
        self.teleportL = [self.teleport1, self.teleport2, self.teleport3, self.teleport4, self.teleport5]
        self.teleportR = [pygame.transform.flip(image, True, False) for image in self.teleportL]
        self.attack3 = False
        self.teleportCheck = 0
        self.teleport_cooldown = 0
        self.attack3_damage = 0
        self.damage1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/damage1.png").convert_alpha())
        self.damage2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/damage2.png").convert_alpha())
        self.damage3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja3/damage3.png").convert_alpha())
        self.damageL = [self.damage1, self.damage2, self.damage3]
        self.damageR = [pygame.transform.flip(image, True, False) for image in self.damageL]
        self.takingDamage = False
        self.Index = 0
        self.image = self.reappear3
        self.x = 20
        self.y = 300
        self.speed = 6
        self.health = 10000
        self.rect = self.image.get_rect(midbottom = (self.x,self.y))
        self.facing_left = True
        self.currentAnimation = self.idleL
        self.move_chosen = False
        self.moveCheck = 0
        self.kunaiLbool = False
        self.kunaiRbool = False
        self.kunaiL = pygame.transform.scale2x(pygame.image.load("images/ninjas/ninja2/kunai.png").convert_alpha())
        self.kunai_rect_L = self.kunaiL.get_rect(midbottom = (-20, 0))
        self.kunaiR = pygame.transform.flip(self.kunaiL, True, False)
        self.kunai_rect_R = self.kunaiR.get_rect(midbottom=(-20, 0))
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))
        self.seq1 = True
        self.seq2 = False
        self.seq3 = False
        self.seq4 = False
        self.distance = 2000
        self.attacksequence = False

    def animation_state(self):
        self.move_chosen = False
        if not self.takingDamage:
            self.Index += 0.20
        elif self.takingDamage:
            self.Index += 0.08

        if self.Index > len(self.currentAnimation):
            self.Index = 0
            if not self.attack1 and not self.attack2 and not self.attack3 and not self.attack4:
                if self.facing_left:
                    self.currentAnimation = self.idleL
                else:
                    self.currentAnimation = self.idleR
            if self.distance < 70 and self.seq1:
                self.seq1 = False
                self.seq2 = True
            elif self.seq2:
                self.seq2 = False
                self.seq3 = True
            elif self.seq3:
                self.seq3 = False
                self.seq4 = True
            elif self.seq4:
                self.seq4 = False
                self.seq1 = True

            self.attack1 = False
            self.attack2 = False
            self.attack3 = False
            self.attack4 = False
            self.takingDamage = False
            self.Index = 0
        if self.attack4:
            if self.facing_left and int(self.Index) == 0:
                self.x += 55
            elif not self.facing_left and int(self.Index) == 0:
                self.x -= 55
        if self.attack1:
            if self.facing_left:
                self.x -= self.speed
            else:
                self.x += self.speed

        self.image = self.currentAnimation[int(self.Index)]
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))

    def ai(self, player):
        self.move_chosen = False
        if player.x > self.x:
            if not self.attack1 and not self.attack3 and not self.attack4:
                self.facing_left = False
            self.distance = player.x - self.x
        else:
            self.facing_left = True
            self.distance = self.x - player.x
        myInt = random.randint(0, 100)
        if myInt >= 95 and not self.attacksequence:
            self.attacksequence = True
        if self.attacksequence:
            if not self.seq2 and not self.seq3 and not self.seq4 and not self.seq1:
                self.seq1 = True
            if self.seq1 and self.distance > 70:
                self.charge()
            elif self.seq2:
                self.kick()
            elif self.seq3:
                self.teleport()
            elif self.seq4:
                self.reappear()
    def charge(self):
        self.attack1 = True
        self.seq1 = True
        if not self.attack2 or self.attack3 or self.attack4:
            if self.facing_left:
                self.currentAnimation = self.chargeL
            else:
                self.currentAnimation = self.chargeR

    def kick(self):
        self.attack2 = True
        if not self.attack3 and not self.attack4:
            if self.facing_left:
                self.currentAnimation = self.kickL
            else:
                self.currentAnimation = self.kickR
            self.move_chosen = True

    def teleport(self):
        self.attack3 = True
        if not self.attack1 and not self.attack2 and not self.attack4:
            if self.facing_left:
                self.currentAnimation = self.teleportL
            else:
                self.currentAnimation = self.teleportR
            self.move_chosen = True

    def reappear(self):
        self.attack4 = True
        if not self.attack1 and not self.attack2 and not self.attack3:
            if self.facing_left:
                self.currentAnimation = self.reappearL
            else:
                self.currentAnimation = self.reappearR
            self.move_chosen = True

    def takeHit(self, player):
        if player.attack1 and not self.takingDamage:
            self.takingDamage = True
            self.health -= player.attack1_damage
        elif player.attack4 and not self.takingDamage:
            self.health -= player.attack4_damage
            self.takingDamage = True
        elif player.attack2 and not self.takingDamage:
            self.health -= player.attack2_damage
            self.takingDamage = True
        elif player.attack3 and not self.takingDamage:
            self.health -= player.attack3_damage
            self.takingDamage = True
        if self.takingDamage:
            if self.facing_left:
                self.currentAnimation = self.damageR
            else:
                self.currentAnimation = self.damageL
        if self.health <= 0:
            self.image = 0


    def update(self, player):
        self.ai(player)
        self.animation_state()

class Zabuza(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.idle1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/idle1.png").convert_alpha())
        self.idleL = [self.idle1]
        self.idleR = [pygame.transform.flip(image, True, False) for image in self.idleL]
        self.walk1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/idle2.png").convert_alpha())
        self.walk2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/idle3.png").convert_alpha())
        self.walk3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/idle4.png").convert_alpha())
        self.walk4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/idle5.png").convert_alpha())
        self.walkL = [self.walk1, self.walk2, self.walk3, self.walk4]
        self.walkR = [pygame.transform.flip(image, True, False) for image in self.walkL]
        self.combo1 = self.idle1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/combo1.png").convert_alpha())
        self.combo2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/combo2.png").convert_alpha())
        self.combo3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/combo3.png").convert_alpha())
        self.combo4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/combo4.png").convert_alpha())
        self.combo5 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/combo5.png").convert_alpha())
        self.combo6 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/combo6.png").convert_alpha())
        self.combo7 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/combo7.png").convert_alpha())
        self.combo8 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/combo8.png").convert_alpha())
        self.combo9 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/combo9.png").convert_alpha())
        self.combo10 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/combo10.png").convert_alpha())
        self.combo11 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/combo11.png").convert_alpha())
        self.combo12 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/combo12.png").convert_alpha())
        self.combo13 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/combo13.png").convert_alpha())
        self.comboL = [self.combo1, self.combo2, self.combo3, self.combo4, self.combo5, self.combo7, self.combo8, self.combo9, self.combo10, self.combo11, self.combo12, self.combo13]
        self.comboR = [pygame.transform.flip(image, True, False) for image in self.comboL]
        self.comboCheck = 0
        self.combo_cooldown = 3000
        self.attack1 = False
        self.attack1_damage = 7000
        self.dash1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/dash1.png").convert_alpha())
        self.dash2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/dash2.png").convert_alpha())
        self.dash3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/dash3.png").convert_alpha())
        self.dash4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/dash4.png").convert_alpha())
        self.dash5 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/dash5.png").convert_alpha())
        self.dash6 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/dash6.png").convert_alpha())
        self.dash7 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/dash7.png").convert_alpha())
        self.dash8 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/dash8.png").convert_alpha())
        self.dashR = [self.dash1, self.dash2, self.dash3, self.dash4, self.dash5, self.dash6, self.dash7, self.dash8]
        self.dashL = [pygame.transform.flip(image, True, False) for image in self.dashR]
        self.attack2 = False
        self.dashCheck = 0
        self.dash_cooldown = 1200
        self.attack2_damage = 4500
        self.throw1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/throw1.png").convert_alpha())
        self.throw2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/throw2.png").convert_alpha())
        self.throw3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/throw3.png").convert_alpha())
        self.throw4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/throw4.png").convert_alpha())
        self.throw5 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/throw5.png").convert_alpha())
        self.throw6 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/throw4.png").convert_alpha())
        self.throw7 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/throw7.png").convert_alpha())
        self.throw8 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/throw8.png").convert_alpha())
        self.throw9 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/throw9.png").convert_alpha())
        self.throwL = [self.throw1, self.throw2, self.throw3, self.throw4, self.throw5, self.throw6, self.throw7, self.throw8, self.throw9]
        self.throwR =[pygame.transform.flip(image, True, False) for image in self.throwL]
        self.throwCheck = 0
        self.throw_coolDown = 2000
        self.throw_range = 350
        self.attack3_damage = 4500
        self.attack3 = False
        self.ultimate1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/ultimate1.png").convert_alpha())
        self.ultimate2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/ultimate2.png").convert_alpha())
        self.ultimate3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/ultimate3.png").convert_alpha())
        self.ultimate4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/ultimate4.png").convert_alpha())
        self.ultimate5 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/ultimate5.png").convert_alpha())
        self.ultimate6 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/ultimate6.png").convert_alpha())
        self.ultimate7 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/ultimate7.png").convert_alpha())
        self.ultimate8 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/ultimate8.png").convert_alpha())
        self.ultimate9 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/ultimate9.png").convert_alpha())
        self.ultimate10 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/ultimate10.png").convert_alpha())
        self.ultimate11 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/ultimate11.png").convert_alpha())
        self.ultimate12 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/ultimate12.png").convert_alpha())
        self.ultimate13 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/ultimate13.png").convert_alpha())
        self.ultimate14 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/ultimate14.png").convert_alpha())
        self.ultimate15 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/ultimate15.png").convert_alpha())
        self.ultimateL = [self.ultimate1, self.ultimate2, self.ultimate3, self.ultimate4, self.ultimate5, self.ultimate6, self.ultimate7, self.ultimate8, self.ultimate9, self.ultimate10, self.ultimate11, self.ultimate12, self.ultimate13, self.ultimate14, self.ultimate15]
        self.ultimateR = [pygame.transform.flip(image, True, False) for image in self.ultimateL]
        self.ultimateCheck = 0
        self.ultimate_cooldown = 5000
        self.attack4 = False
        self.attack4_damage = 25000
        self.damage1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/damage1.png").convert_alpha())
        self.damage2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/damage2.png").convert_alpha())
        self.damage3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/damage3.png").convert_alpha())
        self.damage4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Zabuza/damage4.png").convert_alpha())
        self.takeDamageL = [self.damage1, self.damage2, self.damage3, self.damage4]
        self.takeDamageR = [pygame.transform.flip(image, True, False) for image in self.takeDamageL]
        self.taking_damage = False
        self.damageCheck = 0
        self.damage_cooldown = 600
        self.jumpR = [self.dash7]
        self.jumpL = [pygame.transform.flip(self.dash7, True, False)]
        self.jumping = False
        self.gravity = 0
        self.Index = 0
        self.image = self.idle1
        self.x = 500
        self.y = 300
        self.speed = 6
        self.death = False
        self.health = 30000
        self.rect = self.image.get_rect(midbottom = (self.x,self.y))
        self.facing_left = True
        self.currentAnimation = self.idleL
        self.move_chosen = False
    def animation_state(self):
        if self.move_chosen:
            self.Index = 0
        self.move_chosen = False
        if self.taking_damage:
            self.Index += 0.12
        elif not self.jumping:
            self.Index += 0.18


        if self.y < 300: # jumping
            self.y -= 10
            self.y += self.gravity
            self.gravity += 0.5
            if self.y > 300:
                self.gravity = 0
                self.y = 300
                self.jumping = False
                if self.facing_left:
                    self.currentAnimation = self.idleL
                else:
                    self.currentAnimation = self.idleR

        if self.Index > len(self.currentAnimation):
            self.Index = 0
            if self.taking_damage and self.health <= 0:
                self.death = True
            if self.facing_left:
                self.currentAnimation = self.idleL
            else:
                self.currentAnimation = self.idleR

            self.attack3 = False
            self.attack2 = False
            self.attack1 = False
            self.attack4 = False
            self.taking_damage = False
        if self.attack2:
            if self.facing_left:
                self.x -= 3
            else:
                self.x += 3
        if self.attack1:
            if self.facing_left:
                self.x -= 2
            else:
                self.x += 2
        if self.attack4:
            if self.Index > 5 and self.Index < 8:
                if self.facing_left:
                    self.x -= 1
                else:
                    self.x += 1


        self.image = self.currentAnimation[int(self.Index)]
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))

    def takeHit(self, entity):
        if pygame.time.get_ticks() - self.damageCheck > self.damage_cooldown:
            if entity.attack1 and not self.taking_damage:
                self.taking_damage = True
                self.health -= entity.attack1_damage
            elif entity.attack2 and not self.taking_damage:
                self.health -= entity.attack2_damage
                self.taking_damage = True
            elif entity.attack3 and not self.taking_damage:
                self.health -= entity.attack3_damage
                if entity.attack3_damage !=0:
                    self.taking_damage = True
            elif not self.taking_damage:
                if self.rect.colliderect(entity.kunai_rect_R):
                    self.health -= entity.attack4_damage
                    self.taking_damage = True
                elif self.rect.colliderect(entity.kunai_rect_L):
                    self.health -= entity.attack4_damage
                    self.taking_damage = True
            if self.taking_damage:
                self.damageCheck = pygame.time.get_ticks()
                if self.facing_left:
                    self.currentAnimation = self.takeDamageL
                else:
                    self.currentAnimation = self.takeDamageR


    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1] and (pygame.time.get_ticks() - self.dashCheck) > self.dash_cooldown and not self.attack3 and not self.attack1 and not self.attack4 and not self.taking_damage: # dash
            self.dashCheck = pygame.time.get_ticks()
            self.attack2 = True
            if self.facing_left:
                self.currentAnimation = self.dashL
            else:
                self.currentAnimation = self.dashR
            self.move_chosen = True
        if keys[pygame.K_2] and (pygame.time.get_ticks() - self.throwCheck) > self.throw_coolDown and not self.attack2 and not self.attack1 and not self.attack4  and not self.taking_damage: # throw
            self.throwCheck = pygame.time.get_ticks()
            self.attack3 = True
            if self.facing_left:
                self.currentAnimation = self.throwL
            else:
                self.currentAnimation = self.throwR
            self.move_chosen = True
        if keys[pygame.K_3] and (pygame.time.get_ticks() - self.comboCheck) > self.combo_cooldown and not self.attack2 and not self.attack3 and not self.attack4 and not self.taking_damage: # combo
            self.comboCheck = pygame.time.get_ticks()
            self.attack1 = True
            if self.facing_left:
                self.currentAnimation = self.comboL
            else:
                self.currentAnimation = self.comboR
            self.move_chosen = True
        if keys[pygame.K_4] and (pygame.time.get_ticks() - self.ultimateCheck) > self.ultimate_cooldown and not self.attack2 and not self.attack3 and not self.attack1 and not self.taking_damage: # ultimate
            self.ultimateCheck = pygame.time.get_ticks()
            self.attack4 = True
            if self.facing_left:
                self.currentAnimation = self.ultimateL
            else:
                self.currentAnimation = self.ultimateR
            self.move_chosen = True
        if keys[pygame.K_a] and not self.attack1 and not self.attack3 and not self.attack4 and not self.attack2 and not self.taking_damage: # move left
            self.facing_left = True
            self.x -= self.speed
            if not self.jumping:
                self.currentAnimation = self.walkL
        if keys[pygame.K_d] and not self.attack1 and not self.attack3 and not self.attack4 and not self.attack2 and not self.taking_damage: # move right
            self.facing_left = False
            self.x += self.speed
            if not self.jumping:
                self.currentAnimation = self.walkR
        if keys[pygame.K_SPACE] and not self.attack1 and not self.attack3 and not self.attack4 and not self.attack2 and self.y == 300 and not self.taking_damage: # jump
            self.jumping = True
            if self.facing_left:
                self.currentAnimation = self.jumpL
            else:
                self.currentAnimation = self.jumpR
            self.move_chosen = True
            self.y -= 10

    def update(self):
        self.player_input()
        self.animation_state()

class Sasuke(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.idle1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/idle1.png").convert_alpha())
        self.idle2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/idle2.png").convert_alpha())
        self.idle3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/idle3.png").convert_alpha())
        self.idle4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/idle4.png").convert_alpha())
        self.idleR = [self.idle1, self.idle2, self.idle3, self.idle4]
        self.idleL = [pygame.transform.flip(image, True, False) for image in self.idleR]
        self.run1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/run1.png").convert_alpha())
        self.run2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/run2.png").convert_alpha())
        self.runR = [self.run1, self.run2]
        self.runL = [pygame.transform.flip(image, True, False) for image in self.runR]
        self.running = False
        self.combo1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/combo1.png").convert_alpha())
        self.combo2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/combo2.png").convert_alpha())
        self.combo3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/combo3.png").convert_alpha())
        self.combo4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/combo4.png").convert_alpha())
        self.combo5 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/combo5.png").convert_alpha())
        self.combo6 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/combo6.png").convert_alpha())
        self.combo7 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/combo7.png").convert_alpha())
        self.combo8 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/combo8.png").convert_alpha())
        self.combo9 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/combo9.png").convert_alpha())
        self.combo10 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/combo10.png").convert_alpha())
        self.comboR = [self.combo1, self.combo2, self.combo3, self.combo4, self.combo5, self.combo6, self.combo7, self.combo8, self.combo9, self.combo10]
        self.comboL = [pygame.transform.flip(image, True, False) for image in self.comboR]
        self.attack1 = False
        self.attack1_damage = 4500
        self.combo_cooldown = 900
        self.comboCheck = 0
        self.kick1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/kick1.png").convert_alpha())
        self.kick2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/kick2.png").convert_alpha())
        self.kick3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/kick3.png").convert_alpha())
        self.kick4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/kick4.png").convert_alpha())
        self.kick5 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/kick5.png").convert_alpha())
        self.kick6 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/kick6.png").convert_alpha())
        self.kickR = [self.kick1, self.kick2, self.kick3, self.kick4, self.kick5, self.kick6]
        self.kickL = [pygame.transform.flip(image, True, False) for image in self.kickR]
        self.attack2 = False
        self.attack2_damage = 3000
        self.kick_cooldown = 400
        self.kickCheck = 0
        self.chidori1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/chidori1.png").convert_alpha())
        self.chidori2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/chidori2.png").convert_alpha())
        self.chidori3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/chidori3.png").convert_alpha())
        self.chidori4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/chidori4.png").convert_alpha())
        self.chidori5 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/chidori5.png").convert_alpha())
        self.chidori6 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/chidori6.png").convert_alpha())
        self.chidori7 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/chidori7.png").convert_alpha())
        self.chidori8 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/chidori8.png").convert_alpha())
        self.chidori9 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/chidori9.png").convert_alpha())
        self.chidori10 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/chidori10.png").convert_alpha())
        self.chidori11 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/chidori11.png").convert_alpha())
        self.chidoriR = [self.chidori1, self.chidori2, self.chidori3, self.chidori4, self.chidori5, self.chidori6, self.chidori7, self.chidori8, self.chidori9, self.chidori10, self.chidori11]
        self.chidoriL = [pygame.transform.flip(image, True, False) for image in self.chidoriR]
        self.attack3 = False
        self.attack3_damage = 12000
        self.chidori_cooldown = 1250
        self.chidoriCheck = 0
        self.ultimate1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/ultimate1.png").convert_alpha())
        self.ultimate2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/ultimate2.png").convert_alpha())
        self.ultimate3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/ultimate3.png").convert_alpha())
        self.ultimate4 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/ultimate4.png").convert_alpha())
        self.ultimate5 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/ultimate5.png").convert_alpha())
        self.ultimate6 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/ultimate6.png").convert_alpha())
        self.ultimate7 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/ultimate7.png").convert_alpha())
        self.ultimate8 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/ultimate8.png").convert_alpha())
        self.ultimate9 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/ultimate9.png").convert_alpha())
        self.ultimate10 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/ultimate10.png").convert_alpha())
        self.ultimate11 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/ultimate11.png").convert_alpha())
        self.ultimate12 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/ultimate12.png").convert_alpha())
        self.ultimate13 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/ultimate13.png").convert_alpha())
        self.ultimate14 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/ultimate14.png").convert_alpha())
        self.ultimate15 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/ultimate15.png").convert_alpha())
        self.ultimateR = [self.ultimate1, self.ultimate2, self.ultimate3, self.ultimate4, self.ultimate5, self.ultimate6, self.ultimate7, self.ultimate8, self.ultimate9, self.ultimate10, self.ultimate11, self.ultimate12, self.ultimate13, self.ultimate14, self.ultimate15]
        self.ultimateL = [pygame.transform.flip(image, True, False) for image in self.ultimateR]
        self.attack4 = False
        self.attack4_damage = 25000
        self.ultimate_cooldown = 4000
        self.ultimateCheck = 0
        self.jump = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/jump.png").convert_alpha())
        self.jumpR = [self.jump]
        self.jumpL = [pygame.transform.flip(self.jump, True, False)]
        self.jumping = False
        self.damage1 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/damage1.png").convert_alpha())
        self.damage2 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/damage2.png").convert_alpha())
        self.damage3 = pygame.transform.scale2x(pygame.image.load("images/ninjas/Sasuke/damage3.png").convert_alpha())
        self.takedamageR = [self.damage1, self.damage2, self.damage3]
        self.takedamageL = [pygame.transform.flip(image, True, False) for image in self.takedamageR]
        self.taking_damage = False
        self.damageCheck = 0
        self.damage_cooldown = 450
        self.gravity = 0
        self.Index = 0
        self.image = self.idle1
        self.x = 500
        self.y = 300
        self.speed = 7
        self.death = False
        self.health = 22500
        self.rect = self.image.get_rect(midbottom = (self.x,self.y))
        self.facing_left = True
        self.currentAnimation = self.idleL
        self.move_chosen = False

    def takeHit(self, entity):
        if pygame.time.get_ticks() - self.damageCheck > self.damage_cooldown:
            if entity.attack1 and not self.taking_damage:
                if entity.attack1_damage != 0:
                    self.taking_damage = True
                self.health -= entity.attack1_damage
            elif entity.attack2 and not self.taking_damage:
                self.health -= entity.attack2_damage
                if entity.attack2_damage != 0:
                    self.taking_damage = True
            elif entity.attack3 and not self.taking_damage:
                self.health -= entity.attack3_damage
                if entity.attack3_damage != 0:
                    self.taking_damage = True
            elif not self.taking_damage:
                if self.rect.colliderect(entity.kunai_rect_R):
                    self.health -= entity.attack4_damage
                    if entity.attack4_damage != 0:
                        self.taking_damage = True
                elif self.rect.colliderect(entity.kunai_rect_L):
                    self.health -= entity.attack4_damage
                    if entity.attack4_damage != 0:
                        self.taking_damage = True
            if self.taking_damage:
                self.damageCheck = pygame.time.get_ticks()
                if self.facing_left:
                    self.currentAnimation = self.takedamageL
                else:
                    self.currentAnimation = self.takedamageR

    def animation_state(self):
        if self.move_chosen:
            self.Index = 0
        self.move_chosen = False
        if self.taking_damage:
            self.Index += 0.09
        elif self.attack3:
            self.Index += 0.22
        elif not self.jumping:
            self.Index += 0.18

        if self.y < 300: # jumping
            self.y -= 11
            self.y += self.gravity
            self.gravity += 0.5
            if self.y > 300:
                self.gravity = 0
                self.y = 300
                self.jumping = False
                if self.facing_left:
                    self.currentAnimation = self.idleL
                else:
                    self.currentAnimation = self.idleR

        if self.Index > len(self.currentAnimation):
            self.Index = 0
            if self.taking_damage and self.health <= 0:
                self.death = True
            if not self.running:
                if self.facing_left:
                    self.currentAnimation = self.idleL
                else:
                    self.currentAnimation = self.idleR
            self.attack3 = False
            self.attack2 = False
            self.attack1 = False
            self.attack4 = False
            self.taking_damage = False

        if self.attack1:
            if self.facing_left:
                self.x -= 1
            else:
                self.x += 1
        if self.attack4:
            if self.facing_left:
                self.x -= 1
            else:
                self.x += 1
        if self.attack3:
            if self.Index >= 4:
                if self.facing_left:
                    self.x -= 5
                else:
                    self.x += 5
                if int(self.Index) == 7:
                    if self.facing_left:
                        self.x -= 15
                    else:
                        self.x += 15

        self.image = self.currentAnimation[int(self.Index)]
        self.rect = self.image.get_rect(midbottom=(self.x, self.y))

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_1] and (pygame.time.get_ticks() - self.comboCheck) > self.combo_cooldown and not self.attack3 and not self.attack2 and not self.attack4 and not self.taking_damage: # combo
            self.comboCheck = pygame.time.get_ticks()
            self.attack1 = True
            if self.facing_left:
                self.currentAnimation = self.comboL
            else:
                self.currentAnimation = self.comboR
            self.move_chosen = True

        if keys[pygame.K_2] and (pygame.time.get_ticks() - self.kickCheck) > self.kick_cooldown and not self.attack3 and not self.attack1 and not self.attack4 and not self.taking_damage: # kick
            self.kickCheck = pygame.time.get_ticks()
            self.attack2 = True
            if self.facing_left:
                self.currentAnimation = self.kickL
            else:
                self.currentAnimation = self.kickR
            self.move_chosen = True

        if keys[pygame.K_3] and (pygame.time.get_ticks() - self.chidoriCheck) > self.chidori_cooldown and not self.attack2 and not self.attack1 and not self.attack4 and not self.taking_damage: # chidori
            self.chidoriCheck = pygame.time.get_ticks()
            self.attack3 = True
            if self.facing_left:
                self.currentAnimation = self.chidoriL
            else:
                self.currentAnimation = self.chidoriR
            self.move_chosen = True

        if keys[pygame.K_4] and (pygame.time.get_ticks() - self.ultimateCheck) > self.ultimate_cooldown and not self.attack2 and not self.attack3 and not self.attack1 and not self.taking_damage: # ultimate
            self.ultimateCheck = pygame.time.get_ticks()
            self.attack4 = True
            if self.facing_left:
                self.currentAnimation = self.ultimateL
            else:
                self.currentAnimation = self.ultimateR
            self.move_chosen = True

        if keys[pygame.K_a] and not self.attack1 and not self.attack3 and not self.attack4 and not self.attack2 and not self.taking_damage: # move left
            self.running = True
            self.facing_left = True
            self.x -= self.speed
            if not self.jumping:
                self.currentAnimation = self.runL
        elif keys[pygame.K_d] and not self.attack1 and not self.attack3 and not self.attack4 and not self.attack2 and not self.taking_damage: # move right
            self.running = True
            self.facing_left = False
            self.x += self.speed
            if not self.jumping:
                self.currentAnimation = self.runR
        else:
            self.running = False

        if keys[pygame.K_SPACE] and not self.attack1 and not self.attack3 and not self.attack4 and not self.attack2 and self.y == 300 and not self.taking_damage: # jump
            self.jumping = True
            if self.facing_left:
                self.currentAnimation = self.jumpL
            else:
                self.currentAnimation = self.jumpR
            self.move_chosen = True
            self.y -= 10

    def update(self):
        self.player_input()
        self.animation_state()