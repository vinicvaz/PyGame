import pygame
import time
from random import randrange

class Game:

	def __init__(self):
		##################################################
		####### SHAPES AND WINDOW CONFIGURATION ##########
		##################################################
		self.shape = (640,480) ##width, height
		self.size = 10 ##SNAKE SIZE
		self.title = "Snake 1.0" ## window title
		self.colors = {'white': (255,255,255), 'black':(0,0,0), 'red':(255,0,0), 'green': (0,255,0), 'blue':(0,0,255)} ##colors dictionary
		self.window = pygame.display.set_mode(self.shape) ## CREATE WINDOW GAME
		pygame.display.set_caption(self.title)			  ## WINDOW TITLE

		#################################
		## CONTROL VARIABLES
		#################################		
		self.game_over = False
		self.select = 1
		self.menu = True


		#################################
		## POSITION INIT
		#################################
		self.pos_x = randrange(10,(self.shape[0]-self.size),10)
		self.pos_y = randrange(10,(self.shape[1]-self.size), 10)
		self.apple_x = randrange(10,(self.shape[0]-self.size), 10)
		self.apple_y = randrange(10,(self.shape[1]-self.size), 10)
		self.snake = []
		self.head = []
		self.snake_length = 1


		#################################
		##SNAKE SPEED INIT
		#################################
		self.speed_x = 0
		self.speed_y = 0
		self.control = 10

		#################################
		##CLOCK AND FPS INIT
		#################################
		self.clock = pygame.time.Clock()  ##init clock
		self.FPS = 20 ##FPS RATE

	def text(self, msg, color, size, position):
		font = pygame.font.SysFont(None,size)
		text = font.render(msg,True,color)	
		self.window.blit(text, position)

	def game_menu(self):
		msg = "Choose your mode"
		self.text(msg, self.colors['blue'], 80, (self.shape[0]/9, self.shape[1]/8))
		self.text('F1 - No edges', self.colors['blue'], 40, (self.shape[0]/3.5, self.shape[1]/3))
		self.text('F2 - Square', self.colors['blue'], 40, (self.shape[0]/3.5, self.shape[1]/2))



		


	def game(self):
		## control variables
		exit = True
		try:
			pygame.init()
		except:
			print("Fail")
	
		while exit:

		#################################
		########## MENU LOOP ###########
		#################################
			while self.menu:
				self.window.fill(self.colors['black'])
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						exit = False
						self.game_over = False
						pygame.quit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_F1:
							self.select = 1
							self.menu = False
						if event.key == pygame.K_F2:
							self.select = 2
							self.menu = False
				self.game_menu()
				pygame.display.update()


		#################################
		######## GAME OVER LOOP ########
		#################################
			while self.game_over: 
				self.window.fill(self.colors['black'])
				self.text("GAME OVER! Press ENTER to continue or ESC to quit.", self.colors['blue'], 25, (self.shape[0]/8, self.shape[1]/2))
				pygame.display.update()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						exit = False
						self.game_over = False
						pygame.quit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_RETURN:
							self.game_over = False
							player = Game()
							player.game()
						if event.key == pygame.K_ESCAPE:
							exit = False
							self.game_over = False
							pygame.quit() 

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit = False
					pygame.quit()
				if event.type == pygame.KEYDOWN:
					self.direction(event)

			#print(event)
			self.clock.tick(self.FPS) 
			
			self.window.fill(self.colors['black'])
			self.draw_snake()
			pygame.display.update()

	def draw_walls(self):
		pygame.draw.rect(self.window, self.colors['green'],[0,0,640,480],10 )


	def check_condition(self):

		if self.select == 1:
			if self.pos_x + self.size > self.shape[0]: 
				self.pos_x = 0
			if self.pos_x < 0:
				self.pos_x = self.shape[0] - self.size
			if self.pos_y + self.size > self.shape[1]:
				self.pos_y = 0
			if self.pos_y < 0:
				self.pos_y = self.shape[1] - self.size
		elif self.select == 2:
			if self.pos_x + self.size > self.shape[0]: 
				self.game_over = True
			if self.pos_x < 0:
				self.game_over = True
			if self.pos_y + self.size > self.shape[1]:
				self.game_over = True
			if self.pos_y < 0:
				self.game_over = True
			self.draw_walls()



	def draw_snake(self):

		self.pos_x += self.speed_x
		self.pos_y += self.speed_y

		## SCREEN CROSS CONDITION
		self.check_condition()

		self.draw_apple()


		self.head = []
		self.head.append(self.pos_x) ## add to snakes head the X position on screen
		self.head.append(self.pos_y) ## add to snakes head the Y position on screen
		self.snake.append(self.head) ## add head to snake list

		for position in self.snake:
			pygame.draw.rect(self.window, self.colors['white'], [position[0], position[1],self.size, self.size]) ## redraw snake using list

		if len(self.snake) > self.snake_length:
			del self.snake[0] ## delete the tail
		if any(block ==  self.head for block in self.snake[:-1]): ## verify if snake knocks her body
			self.game_over = True




	def draw_apple(self):
		if self.pos_x != self.apple_x or self.pos_y != self.apple_y:
			pygame.draw.rect(self.window, self.colors['red'], [self.apple_x,self.apple_y,self.size, self.size])
		else:
			self.snake_length +=1
			self.apple_x = randrange(10,(self.shape[0]-self.size), 10)
			self.apple_y = randrange(10,(self.shape[1]-self.size), 10)
			



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


player = Game()
player.game()
pygame.quit()



