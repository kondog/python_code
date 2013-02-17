# -*- coding:utf-8 -*-

import sys, pygame
import unittest
import time
from pygame.locals import *

from ball import BallObj
from bar  import BarObj
from objMediator import Mediator

class PygScreen():
    def __init__(self):
        self._size      = [0,0]
        self._screen    = None
    def setSize( self, sizeX, sizeY ):
        self._size = [sizeX, sizeY]
    def setDisplay( self ):
        self._screen = pygame.display.set_mode( self._size )
    def getSize( self ):
        return self._size
    def displayFill( self, color ):
        self._screen.fill( color )
    def displayBlit( self, ballObj, ballRect ):
        self._screen.blit( ballObj, ballRect )
    def displayFlip( self ):
        self._screen = pygame.display.set_mode( self._size )

if __name__ == "__main__":
    white = 255, 255, 255

    pygame.init()

    screen = PygScreen()
    screen.setSize( 320, 240 )
    screen.setDisplay( )

    ball = BallObj()
    ball.setSpeed( 0, -5 )
    ball.setObj( "img/ball.bmp" )
    ball.setRect_pos( 150, 240 )
    #ball.setRect( )

    bar = BarObj()
    bar.setObj( "img/bar.bmp" )
    bar.setRect_pos( 150, 200 )

    mediator = Mediator()

    while 1:
        time.sleep(0.05)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        ball.ballMove( )
        ball.decideBallPosition(pygame.key.get_pressed(), screen.getSize() )
        mediator.judgeConflictBallAndBar( ball, bar )

        screen.displayFill( white )
        screen.displayBlit( ball.getObj(), ball.getBallrect() )
        screen.displayBlit( bar.getObj(),  bar.getRect() )
        pygame.display.flip()


