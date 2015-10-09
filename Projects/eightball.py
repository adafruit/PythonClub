
# Model

import sys
from termcolor import colored, cprint
import random

class Eightball(object):
	"""docstring for Eightball"""
	def __init__(self):
		self.name = ""
		self.answers = [
			"It is certain",
			"It is decidedly so",
			"Without a doubt",
			"Yes, definitely",
			"You may rely on it",
			"As I see it, yes",
			"Most likely",
			"Outlook good",
			"Yes",
			"Signs point to yes",
			"Reply hazy try again",
			"Ask again later",
			"Better not tell you now",
			"Cannot predict now",
			"Concentrate and ask again",
			"Don't count on it",
			"My reply is no",
			"My sources say no",
			"Outlook not so good",
			"Very doubtful"
			]	
	def welcome(self):
		print 75 * "*"
		print colored("Magic Ball here, what is your name? Please put it in strings so I can understand", "red", attrs=['bold'])
		name = raw_input()
		self.name = name
		print "Welcome {name!s}.".format(**locals())

	def play(self):
		print colored("Go ahead ask me any true or false questions....", "green", attrs=['bold'])
		print colored("Don't forget to put it strings! Thanks. = )", "yellow", attrs=['bold'])
		print 75 * "*"
		question = raw_input()
		print "Thinking about your question:" , question
		print "Answer is...........", 
		print colored((random.choice(self.answers)), "cyan", attrs=['blink'])
		print 75 * "*"
		print "Thank you for playing" , self.name




# Controller

# This should be in a separate file

from eightball import Eightball

game1 = Eightball()

game1.welcome()
game1.play()

game2 = Eightball()



#Great Game!!
