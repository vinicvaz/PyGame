import pygame
import time
from random import randrange
from Screen import *
from Snake import *
from Food import *


class GameClass:

	def __init__(self,screen,snake,food, game_number):

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
		self.game_number = game_number

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
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						exit = False
						self.game_over = False
						pygame.quit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_RETURN:
							highscores.append(food.score)
							print("Highscores:",highscores)
							self.snake.reset()
							self.food.reset()
							player = GameClass(screen, snake, food, self.game_number+1)
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
			self.food.draw_food(self.window, self.game_number) ## Draw Food

			pygame.display.update()



highscores = []

screen = ScreenClass()
snake = SnakeClass(screen)
food = FoodClass(screen, snake)
player = GameClass(screen, snake, food, 1)
player.game_loop()