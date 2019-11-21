import pygame
import time
from random import randrange
from Screen import *
from Snake2 import *
from Food import *



class GameClass:

	def __init__(self,screen,snake,food):

		#################################
		## CONTROL VARIABLES
		#################################		
		self.game_over = snake.game_over
		self.select = 1
		self.menu = True
		self.snake = snake
		self.food = food
		self.screen = screen
		self.title = 'Snake 2.0'

		self.window = pygame.display.set_mode(self.screen.shape)
		pygame.display.set_caption(self.title) ## DISPLAY TITLE

		#################################
		##CLOCK AND FPS INIT
		#################################
		self.clock = pygame.time.Clock()  ##init clock
		self.FPS = 20 ##FPS RATE


	def game_loop(self):
		exit = True
		try:
			pygame.init()
		except:
			print("Fail")
		while exit:

			while snake.game_over: 
				self.window.fill(screen.colors['black'])
				print("game over")
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						exit = False
						self.game_over = False
						pygame.quit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_RETURN:
							snake.game_over = False
							self.snake.reset()
							player = GameClass(screen, snake, food)
							player.game_loop()
						if event.key == pygame.K_ESCAPE:
							exit = False
							snake.game_over = False
							pygame.quit()


			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit = False
					pygame.quit()
				if event.type == pygame.KEYDOWN:
					self.snake.direction(event)

			self.clock.tick(self.FPS)
			self.window.fill(self.screen.colors['black'])

			self.snake.draw_snake(self.window) ## Draw Snake
			self.food.draw_food(self.window) ## Draw Food

			pygame.display.update()


screen = ScreenClass()
snake = SnakeClass(screen)
food = FoodClass(screen, snake)
player = GameClass(screen, snake, food)
player.game_loop()