import pygame
import neat
import time
import os
import random

WIN_WIDTH = 600
WIN_HEIGHT = 800

BIRD_IMGS = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
PIPR_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

class Bird:
	IMGS = BIRD_IMGS
	MAX_ROTATION = 25 #How much the bird is gonna tilt, when it's going up we have to tilt it up sightly, same for down.
	ROT_VEL = 20   #How much we are gonna rotate in each frame
	ANIMATION_TIME = 5   #How long we show each bird animation

	def __init__(self, x, y): #x,y represent the starting positions of our birds
		self.x = x 
		self.y = y 
		self.tilt = 0  #We will know how much the image is tilted, first it's going to be flat so zero
		self.tick_count = 0 
		self.vel = 0
		self.height = self.y 
		self.img_count = 0
		self.img = self.IMGS[0]

	def jump(self):
		self.vel = -10.5 #At top left corner x,y coordinates are 0,0. So when bird needs to move upwards it should have -ve velocity, down +ve vel , left -ve and right +ve velocity 
		self.tick_count = 0  #Keeps track of when we last jumped 
		self.height = self.y 

	def move(self):
		