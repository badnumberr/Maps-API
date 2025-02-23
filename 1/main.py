import pygame
import sys

pygame.init()

width, height = 900, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("1")
map_image = pygame.image.load("map.png")
scale_factor = 1

map_image = pygame.transform.scale(map_image, (int(map_image.get_width() * scale_factor),
                                               int(map_image.get_height() * scale_factor)))
map_x, map_y = (width - map_image.get_width()) // 2, (height - map_image.get_height()) // 2


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    screen.blit(map_image, (map_x, map_y))
    pygame.display.flip()
