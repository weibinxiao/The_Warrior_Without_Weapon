import random
import sys
import math
import pygame
from pygame.locals import *


# 精灵位置
class MySprite(pygame.sprite.Sprite):
    def __init__(self,image_file):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.master_image = None
        self.frame = 0
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.direction = 0
        self.velocity = Point(0.0,0.0)


    def getx(self):
        return self.rect.x

    def setx(self, value):
        self.rect.x = value
    X = property(getx, setx)

    def gety(self):
        return self.rect.y

    def sety(self, value):
        self.rect.y = value
    Y = property(gety, sety)

    def getpos(self):
        return self.rect.topleft

    def setpos(self, pos):
        self.rect.topleft = pos
    position = property(getpos, setpos)

    def load(self, filename, width, height, columns):
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width
        self.frame_height = height
        self.rect = Rect(0, 0, width, height)
        self.columns = columns
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=30):

        if current_time > self.last_time + rate:
            self.frame += 1
        if self.frame > self.last_frame:
            self.frame = self.first_frame
        self.last_time = current_time
        # 当帧变化时，修改
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)

            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

    def __str__(self):
        return str(self.frame) + "," + str(self.first_frame) + "," + str(self.last_frame) + \
               "," + str(self.frame_width) + "," + str(self.frame_height) + "," + \
               str(self.columns) + "," + str(self.rect)


class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def setx(self, x):
        self.__x = x
    x = property(getx, setx)

    def gety(self):
        return self.__y

    def sety(self, y):
        self.__y = y
    y = property(gety, sety)

    def __str__(self):
        return "{X:" + "{:.0f}".format(self.__x) + ",Y:" + "{:.0f}".format(self.__y) + "}"


def print_text(font, x, y, text, color=(255, 255,255), shadow=True):
    imgText = font.render(text, True, color)
    screen = pygame.display.get_surface()
    screen.blit(imgText, (x, y))


