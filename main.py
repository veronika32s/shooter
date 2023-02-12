import pygame
from data import*
from util import*
import time

pygame.init()

window = pygame.display.set_mode((setting_win["WIDTH"],setting_win["HEIGHT"]))

def run():

    game = True
    hero = Player(100,100,30,70,hero_image,7)
    bot = Bot(500,300,40,40,bot_stay,bot_animation_move,1)
    gift = Gift(400,480,gift_image,40,40)
    amount = 0
    respawn = 1
    clock = pygame.time.Clock()
    alian_show_key = 0
    create_wall("MAP1")

    while game:
        for wall in wall_list:
            window.blit(wall.IMAGE, (wall.x, wall.y))

        window.blit(hero.IMAGE_NOW,(hero.x,hero.y))
        for bot in bot_list:
            window.blit(bot.IMAGE_NOW,(bot.x,bot.y))
            bot.step(hero)
        window.blit(gift.IMAGE,(gift.x,gift.y))

        hero.move()
        if hero.SHOT == True:
            for bullet in hero.BULLET:
                bullet.x += bullet.X
                bullet.y += bullet.Y
                window.blit(bullet.IMAGE,(bullet.x,bullet.y))
                for bot in bot_list:
                    if bot.colliderect(bullet):
                        hero.BULLET.remove(bullet)
                        bot_list.remove(bot)
                        hero.SHOT = False
                        break
                if bullet.x > setting_win["WIDTH"] or bullet.y > setting_win["HEIGHT"] or bullet.x < 0 or bullet.y < 0:
                    hero.BULLET.remove(bullet)
                    hero.SHOT = False

        period_respawn = time.time()
        if hero.y > 200 and amount != 10 or alian_show_key and amount != 10 :
            alian_show_key = True
            if period_respawn - respawn > 1 or period_respawn // respawn == int(period_respawn):
                bot_list.append(Bot(100,600,40,40,bot_stay,bot_animation_move,1))
                bot_list.append(Bot(300, 40, 100, 700, bot_stay, bot_animation_move, 1))
                respawn = time.time()
                amount += 1


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero.MOVE["UP"] = True
                elif event.key == pygame.K_s:
                    hero.MOVE["DOWN"] = True
                elif event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = True
                elif event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    hero.MOVE["UP"] = False
                elif event.key == pygame.K_s:
                    hero.MOVE["DOWN"] = False
                elif event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = False
                elif event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not hero.SHOT:
                hero.SHOT = True
                hero.BULLET.append(Bullet(hero.x,hero.y,20,10))
                x,y = event.pos
                hero.BULLET[-1].make_angle(x,y,hero.x,hero.y)

            if hero.colliderect(bot):
                font = pygame.font.SysFont("Arial", 50).render("You lose!!!", True, (255, 0, 0))
                window.blit(font, (500, 350))
                pygame.display.flip()
                time.sleep(1)
                hero.x = 5
                hero.y = 5


        clock.tick(setting_win["FPS"])
        pygame.display.flip()

run()