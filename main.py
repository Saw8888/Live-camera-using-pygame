import pygame
from pygame.locals import *
import pygame.camera
import pygame.image

pygame.init()
pygame.camera.init()
pygame.display.set_caption("Game")

cameras = pygame.camera.list_cameras()

print("Using camera %s ..." % cameras[0])

cam1 = pygame.camera.Camera(cameras[0])
cam1.start()

img1 = cam1.get_image()

flags = DOUBLEBUF
screen = pygame.display.set_mode((100,100), flags, 4)

while 1:
    for event in pygame.event.get():
        pygame.event.set_allowed(KEYDOWN)
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            pygame.camera.quit()

    img1 = cam1.get_image().convert()
    screen.blit(img1, (0, 0))
    pygame.display.update()
