from Button import Button
from ui import UI
from game_data import level_0
from level import *

class Game:
	def __init__(self, screen):

		# game attributes
		self.display_surface = screen
		self.max_health = 100;

		self.cur_health = 100;
		self.coins = 50
		self.mushrooms = 0
		self.youAreDead = False

		self.level = Level(screen, level_0,self.change_coins, self.change_health,self.change_mushrooms)
		self.ui = UI(screen)

		#State
		self.game_state = False
		self.menu_active = False
		self.game_active = False
		self.shop_active = False
		self.buy_active = False

		#Main - IMG
		self.start_img = pygame.image.load('../graphics/ui/start.jpg').convert_alpha()
		self.shop_img = pygame.image.load('../graphics/ui/shop.jpg').convert_alpha()

		self.pic1 = pygame.image.load('../graphics/ui/mainmenu.png').convert_alpha()
		self.pic2 = pygame.image.load('../graphics/ui/mainmenu1.png').convert_alpha()

		# Shop - IMG, Font
		self.font = pygame.font.SysFont(None, 40)

		self.mushrooms_img = pygame.image.load('../graphics/ui/mushroom.png').convert_alpha()
		self.buy_img = pygame.image.load('../graphics/ui/buy.jpg').convert_alpha()
		self.return_img = pygame.image.load('../graphics/ui/return.jpg')
		self.lost = self.font.render('I am sorry you lost! Try again! ', True, (255, 255, 255))
		self.win = self.font.render('You won! Good job! ', True, (255, 255, 255))
		# Buttons
		self.start_button = Button(300, 100, self.start_img, self.display_surface)
		self.shop_button = Button(300, 400, self.shop_img, self.display_surface)
		self.buy_button = Button(700, 100, self.buy_img, self.display_surface)
		self.return_button = Button(700, 400, self.return_img, self.display_surface)


	def change_coins(self, amount):
		self.coins += amount

	def change_health(self, amount):
		if self.cur_health + amount > self.max_health:
			self.cur_health = self.max_health
		else:
			self.cur_health += amount

	def change_mushrooms(self, amount):
		if self.mushrooms - 1 >=0:
			self.mushrooms += amount


	def buy(self):
		self.mushrooms += 1
		self.coins -= 50
		self.buy_active = False

	def shop(self):

		self.display_surface.fill((225, 198, 153))
		self.display_surface.blit(self.mushrooms_img, (150, 100))

		# Displays current count of coins and bombs on the screen.
		self.currCoins = self.font.render('Current coins: {0}'.format(self.coins), True, (255, 255, 255))
		self.currBombs = self.font.render('Mushrooms: {0}'.format(self.mushrooms), True, (255, 255, 255))


		self.display_surface.blit(self.currBombs, (950, 20))
		self.display_surface.blit(self.currCoins, (20, 20))

		if self.shop_button.clicked:
			self.buy_button.clicked = False
			if self.buy_button.draw():
				self.buy_active = True
				self.buy_button.clicked = True


		if self.return_button.draw():
			self.shop_active = False
			self.return_button.clicked = False
			self.shop_button.clicked = False
			self.start_button.clicked = False
			self.buy_button.clicked = False

		if self.buy_active and self.coins - 50 >= 0:
			self.buy()

		return self.shop_active

	def open_menu(self) :

		# Sets up the screen
		self.display_surface.fill((225, 198, 153))
		self.display_surface.blit(self.pic1, (10, 20))
		self.display_surface.blit(self.pic2, (1000, 400))

		# Checks if the button is pressed
		# Option 1 - Start -> starts the game

		if self.start_button.draw():
			self.game_active = True
			self.start_button.clicked = True
			self.shop_button.clicked = True

		# Checks if the button is pressed
		# Option 2 - Shop -> takes to the shop

		if self.shop_button.draw():
			self.shop_active = True
			self.shop_button.clicked = True
			self.buy_button.clicked = True
			self.start_button.clicked = True

		if self.game_active:
			if self.run() == False:
				self.game_active = False
				self.start_button.clicked = False
				self.shop_button.clicked = False
				self.menu_active = False


		if self.shop_active:
			return self.shop()


	def run(self):

		self.game_state = self.level.run()

		if self.game_state == False:

			self.display_surface.blit(self.lost,(300, 300))
			if self.return_button.draw():
				self.level = Level(self.display_surface, level_0,self.change_coins, self.change_health,self.change_mushrooms)
				self.return_button.clicked = False
				return False

		if self.game_state == True:

			self.display_surface.blit(self.win, (300, 300))
			if self.return_button.draw():
				self.level = Level(self.display_surface, level_0, self.change_coins, self.change_health,  self.change_mushrooms)
				self.return_button.clicked = False
				return False


		self.ui.show_health(self.cur_health, self.max_health)
		self.ui.show_coins(self.coins)
		self.ui.show_mushrooms(self.mushrooms)


