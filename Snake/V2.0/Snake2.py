from random import randrange
import pygame


class SnakeClass:

	def __init__(self, screen):
		##################################################
		####### SHAPES AND WINDOW CONFIGURATION ##########
		##################################################
		self.size = 10 ##SNAKE SIZE
		self.colors = {'white': (255,255,255), 'black':(0,0,0), 'red':(255,0,0), 'green': (0,255,0), 'blue':(0,0,255)} ##colors dictionary
		self.window = screen
		self.game_over = False

		#################################
		## POSITION INIT
		#################################
		self.pos_x = randrange(10,(self.window.shape[0]-self.size),10)
		self.pos_y = randrange(10,(self.window.shape[1]-self.size), 10)
		self.snake = []
		self.head = []
		self.snake_length = 1


		#################################
		##SNAKE SPEED INIT
		#################################
		self.speed_x = 0
		self.speed_y = 0
		self.control = 10

	def direction(self,event):
		if event.key == pygame.K_LEFT and self.speed_x != self.size and self.speed_x != -self.size:
			self.speed_x -= self.control
			self.speed_y = 0
		if event.key == pygame.K_RIGHT and self.speed_x != -self.size and self.speed_x != self.size:
			self.speed_x += self.control
			self.speed_y = 0
		if event.key == pygame.K_UP and self.speed_y != self.size and self.speed_y != -self.size:
			self.speed_y -= self.control
			self.speed_x = 0
		if event.key == pygame.K_DOWN and self.speed_y != -self.size and self.speed_y != self.size:
			self.speed_y += self.control
			self.speed_x = 0
		if event.key == pygame.K_SPACE:
			self.snake_length +=1


	def draw_snake(self, surface):

		self.pos_x += self.speed_x
		self.pos_y += self.speed_y

		self.check_condition()

		self.head = []
		self.head.append(self.pos_x) ## add to snakes head the X position on screen
		self.head.append(self.pos_y) ## add to snakes head the Y position on screen
		self.snake.append(self.head) ## add head to snake list

		for position in self.snake:
			pygame.draw.rect(surface, self.colors['white'], [position[0], position[1],self.size, self.size]) ## redraw snake using list

		if len(self.snake) > self.snake_length:
			del self.snake[0] ## delete the tail
		if any(block ==  self.head for block in self.snake[:-1]): ## verify if snake knocks her body
			self.game_over = True

	def reset(self):

		self.pos_x = randrange(10,(self.window.shape[0]-self.size),10)
		self.pos_y = randrange(10,(self.window.shape[1]-self.size), 10)
		self.snake = []
		self.head = []
		self.snake_length = 1
		self.game_over = False


		#################################
		##SNAKE SPEED INIT
		#################################
		self.speed_x = 0
		self.speed_y = 0
		self.control = 10

	def check_condition(self):

		if self.pos_x + self.size > self.window.shape[0]: 
			self.pos_x = 0
		if self.pos_x < 0:
			self.pos_x = self.window.shape[0] - self.size
		if self.pos_y + self.size > self.window.shape[1]:
			self.pos_y = 0
		if self.pos_y < 0:
			self.pos_y = self.window.shape[1] - self.size



