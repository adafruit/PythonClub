import pygame
from pygame.locals import *

class App:
	def __init__(self):
		self._running = True
		self._display_surf = None
		self.size = self.weight, self.height = 640, 400

	def on_init(self):
		pygame.init()
		self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		self._running = True
		self.font = pygame.font.Font(None, 36)
		pygame.mouse.set_visible(False)

	def on_event(self, event):
		if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
			self._running = False

	def on_loop(self):
		pass

	def on_render(self):
		text = self.font.render("Hello There", 1, (255, 255, 10))
		textpos = text.get_rect()
		textpos.centerx = self._display_surf.get_rect().centerx
		self._display_surf.blit(text, textpos)
		pygame.display.flip()

	def on_cleanup(self):
		pygame.quit()

	def on_execute(self):
		if self.on_init() == False:
			self._running = False

		while(self._running):
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			self.on_render()
		self.on_cleanup()

if __name__ == "__main__":
	theApp = App()
	theApp.on_execute()
