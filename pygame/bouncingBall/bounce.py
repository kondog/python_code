# -*- coding:utf-8 -*-

import sys, pygame
import unittest
import time
from pygame.locals import *

from ball          import BallObj
from bar           import BarObj
from warp          import WarpObj
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

    ball = BallObj()
    ball.setSpeed( 0, -5 )
    ball.setObj( sysData.ballBmp )
    ball.setRect_pos( 50, 240 )

    bar = BarObj()
    bar.setObj( sysData.barBmp)
    bar.setRect_pos( 150, 200 )

    warp = WarpObj()
    warp.setObj( sysData.warpBmp )
    warp.setRect_pos( 230, 150 )

    mediator = Mediator()

    while True:
        time.sleep(sysData.waitTime)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        ball.ballMove( )
        ball.decideBallPosition(pygame.key.get_pressed(), screen.getSize() )

        # ボールとバーが衝突した際の動作
        mediator.judgeConflictBallAndBar( ball, bar )
        mediator.judgeConflictBallAndWarp( ball, warp, 50 )

        screen.displayFill( white )
        screen.displayBlit( ball.getObj(), ball.getBallrect() )
        screen.displayBlit( bar.getObj(),  bar.getRect() )
        screen.displayBlit( warp.getObj(),  warp.getRect() )
        pygame.display.flip()

