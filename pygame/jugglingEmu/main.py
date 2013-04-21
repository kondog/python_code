# -*- coding:utf-8 -*-

import sys, pygame
import unittest
import time
from pygame.locals import *

from ball          import BallObj
from bar           import BarObj
from objMediator   import Mediator
from systemData    import SysData

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
    sysData = SysData()
    white   = sysData.screenColor

    pygame.init()

    screen = PygScreen()
    screen.setSize( sysData.screenSizeX,
                    sysData.screenSizeY)
    screen.setDisplay( )

    ball1 = BallObj()
    ball1.setSpeed( 0, 0 )
    ball1.setObj( sysData.ballBmp )
    ball1.setRect_pos( 60, -100 )

#    ball2 = BallObj()
#    ball2.setSpeed( 0, 0 )
#    ball2.setObj( sysData.ballBmp )
#    ball2.setRect_pos( 340, 100 )
#
#    ball3 = BallObj()
#    ball3.setSpeed( 0, 0 )
#    ball3.setObj( sysData.ballBmp )
#    ball3.setRect_pos( 60, 350 )

    balls = [
             ball1
#            ,ball2
#            ,ball3
            ]

    barLeft = BarObj()
    barLeft.setObj( sysData.barBmp)
    barLeft.setRect_pos( sysData.leftBarX, sysData.barY )

    barRight = BarObj()
    barRight.setObj( sysData.barBmp)
    barRight.setRect_pos( sysData.rightBarX, sysData.barY )

    mediator = Mediator()

    while True:
        time.sleep(sysData.waitTime)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        for ball in balls:
            ball.ballMove( )
            ball.decideBallPosition(pygame.key.get_pressed(), screen.getSize() )
        #print balls[0].getBallrect()
        # ボールとバーが衝突した際の動作
        for ball in balls:
            mediator.judgeConflictBallAndBar( ball, barRight )
            mediator.judgeConflictBallAndBar( ball, barLeft )

        screen.displayFill( white )
        for ball in balls:
            screen.displayBlit( ball.getObj(), ball.getBallrect() )
        screen.displayBlit( barRight.getObj(), barRight.getRect() )
        screen.displayBlit( barLeft.getObj(),  barLeft.getRect() )
        pygame.display.flip()

