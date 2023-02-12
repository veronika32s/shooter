import os
import pygame


setting_win = {
    "WIDTH": 1000,
    "HEIGHT": 700,
    "FPS": 60
}


maps = {
    "MAP1":[
                "00000000000000000000000000000",
                "00000000000000000000000000000",
                "00000000303030300000000000000",
                "00000000303030300000000000000",
                "00000022222222223000000000000",
                "00010010000000003000000000000",
                "00010010000000003000000000000",
                "00010010000000003000000000000",
                "00010012222000003000000000000",
                "00010010000100003000000000000",
                "00010010000100000000000000000",
                "00010010000100000000000000000",
                "00010010000000000000000000000",
                "00010010000000000000000000000",
            ]
}
#read_json("maps.json")

wall_list = list()

image_list = list()

bot_list = list()

abs_path = os.path.abspath(__file__ + "/..") + "\\image\\"

wall_image = pygame.image.load(abs_path + "wall_image.png")
hero_image = pygame.image.load(abs_path +"\\Player\\" + "hero.png")
#wall = pygame.image.load(abs_path + )
hero_animation = pygame.image.load(abs_path +"\\Player\\"+ "hero.animation.png")
hero_animation1 = pygame.image.load(abs_path +"\\Player\\"+ "hero.animation1.png")
hero_animation2 = pygame.image.load(abs_path +"\\Player\\"+ "hero.animation2.png")
hero_animation3 = pygame.image.load(abs_path +"\\Player\\"+ "hero.animation3.png")
hero_animation4 = pygame.image.load(abs_path +"\\Player\\"+ "hero.animation4.png")
hero_animation5 = pygame.image.load(abs_path +"\\Player\\"+ "hero.animation5.png")


bot_stay = pygame.image.load(abs_path + "bot.png")
bot_animation_move = pygame.image.load(abs_path + "bot.animation1.png")
bullet_image = pygame.image.load(abs_path + "bullet..png")
gift_image = pygame.image.load(abs_path + "flower.png")

