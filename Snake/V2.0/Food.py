from random import randrange
import pygame

class FoodClass:

	def __init__(self, screen, snake):

		self.window = screen
		self.size = 10
		self.colors = {'white': (255,255,255), 'black':(0,0,0), 'red':(255,0,0), 'green': (0,255,0), 'blue':(0,0,255)} ##colors dictionary
		#################################
		## POSITION INIT
		#################################
		self.apple_x = randrange(10,(self.window.shape[0]-self.size), 10)
		self.apple_y = randrange(10,(self.window.shape[1]-self.size), 10)
		self.snake = snake
		self.score = 0



	def draw_food(self,surface, jogo):

		if self.snake.pos_x != self.apple_x or self.snake.pos_y != self.apple_y:
			pygame.draw.rect(surface, self.colors['red'], [self.apple_x,self.apple_y,self.size, self.size])
		else:
			self.snake.snake_length +=1
			self.score += 1
			print("Score do jogo ",jogo,":",self.score)
			self.apple_x = randrange(10,(self.window.shape[0]-self.size), 10)
			self.apple_y = randrange(10,(self.window.shape[1]-self.size), 10)

	def reset(self):
		self.apple_x = randrange(10,(self.window.shape[0]-self.size), 10)
		self.apple_y = randrange(10,(self.window.shape[1]-self.size), 10)
		self.score=0



