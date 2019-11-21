import pygame
import time
from random import randrange

class ScreenClass:

	def __init__(self):

		self.shape = (480,340) ##width, height
		self.title = "Snake 2.0" ## window title
		self.colors = {'white': (255,255,255), 'black':(0,0,0), 'red':(255,0,0), 'green': (0,255,0), 'blue':(0,0,255)} ##colors dictionary
		self.window = None


	def create_window(self):
		self.window = pygame.display.set_mode(self.shape) ## CREATE WINDOW GAME
		pygame.display.set_caption(self.title) ## DISPLAY TITLE


	
	def text(self, msg, color, size, position):
		font = pygame.font.SysFont(None,size)
		text = font.render(msg,True,color)	
		self.window.blit(text, position)



	def game_menu(self):
		msg = "Choose your mode"
		self.text(msg, self.colors['blue'], 80, (self.shape[0]/9, self.shape[1]/8))
		self.text('F1 - No edges', self.colors['blue'], 40, (self.shape[0]/3.5, self.shape[1]/3))
		self.text('F2 - Square', self.colors['blue'], 40, (self.shape[0]/3.5, self.shape[1]/2))
		