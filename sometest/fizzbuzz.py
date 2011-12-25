#! /usr/bin/python

def fizzbuzz( limit ):
	fizz = 3
	buzz = 5

	print "start fizzbuzz."

	for counter in range( limit ):
		if  ( 0 == counter % fizz ) & ( 0 == counter % buzz ) :
			print "fizzbuzz\n"
		elif 0 == counter % fizz: 
			print "fizz\n"
		elif 0 == counter % buzz:
			print "buzz\n"
		else:
			print str(counter)+"\n"

fizzbuzz(30)
