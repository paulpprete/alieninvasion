#Making our ship!
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

	def __init__(self, ai_settings, screen):
		super(Ship, self).__init__()

		#initializing
		self.screen = screen
		self.ai_settings = ai_settings

		#Loading the spaceship into the game
		self.image = pygame.image.load('images/rocket.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		#Positioning the spaceship
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		self.center = float(self.rect.centerx)

		#Moving the spaceship
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.rect.centerx += self.ai_settings.ship_speed_factor
		elif self.moving_left and self.rect.left > self.screen_rect.left:
			self.rect.centerx -= self.ai_settings.ship_speed_factor
		elif self.moving_up and self.rect.top < self.screen_rect.top:
			self.rect += self.ai_settings.ship_speed_factor
		elif self.moving_down and self.rect.bottom > self.screen_rect.bottom:
			self.rect -= self.ai_settings.ship_speed_factor

	def blitme(self):
		#getting the ship into the game
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		self.center = self.screen_rect.centerx