import pygame
import sys

pygame.init()

W, H = 900, 700
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("2")
map_image = pygame.image.load("map.png")
scale_factor = 1
min_scale = 0.5
max_scale = 3.0

map_x, map_y = (W - map_image.get_width()) // 2, (H - map_image.get_height()) // 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                scale_factor = min(scale_factor + 0.1, max_scale)
            elif event.key == pygame.K_PAGEDOWN:
                scale_factor = max(scale_factor - 0.1, min_scale)
    scaled_map_image = pygame.transform.scale(map_image, (int(map_image.get_width() * scale_factor),
                                                          int(map_image.get_height() * scale_factor)))

    map_x, map_y = (W - scaled_map_image.get_width()) // 2, (H - scaled_map_image.get_height()) // 2

    screen.fill((255, 255, 255))
    screen.blit(scaled_map_image, (map_x, map_y))
    pygame.display.flip()
