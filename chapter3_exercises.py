# Exercises for chapter 3:

# Name: Patrick Byrnes (PMByrnes)

#Exercise 3.1 - error is "NameError: name 'repeat_lyrics' is not defined
#Exercise 3.2 - runs fine

#Exercise 3.3
import string
def right_justify(s):
	string.rjust(s, 70, )

right_justify(s)

#Exercise 3.4
def do_twice(funct):
	funct()
	funct()

def print_spam():
	print 'spam'

do_twice(print_spam)
def do_twice(funct, val):
	funct(val)
	funct(val)

def print_twice(string):
	print string
	print string

do_twice(print_twice, 'spam')
def do_four(funct, val):
	do_twice(funct, val)
	do_twice(funct, val)

do_four(print_twice, 'spam')
