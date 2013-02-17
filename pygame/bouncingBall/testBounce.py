# -*- coding:utf-8 -*-

import unittest
import pygame
from pygame.locals import *

from bounce import PygScreen
from ball import BallObj
from bar  import BarObj
from objMediator import Mediator

class TestFunctions( unittest.TestCase ):
    def test_decideBallPosition(self):
        pygame.init()
        screen = PygScreen()
        screen.setSize(100,100)
        ballObj = BallObj()
        ballObj.setObj("img/ball.bmp")
        ballObj.setRect()

        # $B%\!<%k$N(BX$BCM$,%9%/%j!<%s%5%$%:%*!<%P$N;~%9%T!<%I$N(BX$BCM$,5UE>(B
        ballObj.setBallrectRight(500)
        ballObj.setSpeed(1,1)
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        ballObj.decideBallPosition( pressed_keys_cp, screen.getSize() )
        self.assertTrue( ballObj.getSpeedX() == -1 )

        # $B%\!<%k$N(BY$BCM$,%9%/%j!<%s%5%$%:%*!<%P$N;~%9%T!<%I$N(BY$BCM$,=iB.(B
        ballObj.setBallrectBottom(240)
        ballObj.setSpeed(1,1)
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        ballObj.decideBallPosition( pressed_keys_cp, screen.getSize() )
        self.assertTrue( ballObj.getSpeedY() == -5 )

        # $B%\!<%k$N(BY$BCM$,%9%/%j!<%s%5%$%:Fb$N;~%9%T!<%I$N(BY$BCM$,8:B.(B
        ballObj.setBallrectBottom(1)
        ballObj.setSpeed(1,-3)
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        ballObj.decideBallPosition( pressed_keys_cp, screen.getSize() )
        self.assertTrue( ballObj.getSpeedY() == -2 )

        # $B%\!<%k$N(BY$BCM$,%9%/%j!<%s%5%$%:Fb$N;~%9%T!<%I$N(BY$BCM$,8:B.(B
        # $B$+$D1&%-!<$,2!$5$l$F$$$?;~%9%T!<%I$N(BX$BCM$,A}Bg(B
        ballObj.setBallrectRight(5)
        ballObj.setBallrectLeft(5)
        ballObj.setBallrectBottom(1)
        ballObj.setSpeed(1,-3)
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        pressed_keys_cp[K_RIGHT] = 1
        ballObj.decideBallPosition( pressed_keys_cp, screen.getSize() )
        self.assertTrue( [2,-2] == ballObj.getSpeed() )

    # $B;n83MQ$K0l<0$N(Btuple$B$r:n@.$9$k(B
    def makeListFromKeyTuple( self, keyTuple ):
        pressed_keys_cp = []
        for keyList in keyTuple:
            pressed_keys_cp.append( keyList )
        return pressed_keys_cp
            
    def test_moveAs2Key(self):
        pygame.init()

        screen = PygScreen()
        screen.setSize(10,10)
        ballObj = BallObj()
        ballObj.setObj("img/ball.bmp")
        ballObj.setRect()

        # Left$B%-!<$,2!$5$l$?;~(BspeedX$B$,(B1$B8:;;(B
        ballObj.setSpeed( 1,1 )
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        pressed_keys_cp[K_LEFT] = 1
        ballObj.moveAs2Key( pressed_keys_cp )
        self.assertTrue( [0,1] == ballObj.getSpeed() )

        # Right$B%-!<$,2!$5$l$?;~(BspeedX$B$,(B1$B2C;;(B
        ballObj.setSpeed( 1,1 )
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        pressed_keys_cp[K_RIGHT] = 1
        ballObj.moveAs2Key( pressed_keys_cp )
        self.assertTrue( [2,1] == ballObj.getSpeed() )

        # Up$B%-!<$,2!$5$l$?;~(BinitSpeed$B$,(B1$B2C;;(B
        ballObj.setInitSpeed( 5 )
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        pressed_keys_cp[K_UP] = 1
        ballObj.moveAs2Key( pressed_keys_cp )
        self.assertTrue( 6 == ballObj.getInitSpeed() )

        # Up$B%-!<$,2!$5$l$?;~(BinitSpeed$B$,(B1$B2C;;(B
        ballObj.setInitSpeed( 20 )
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        pressed_keys_cp[K_UP] = 1
        ballObj.moveAs2Key( pressed_keys_cp )
        self.assertTrue( 20 == ballObj.getInitSpeed() )

        # Down$B%-!<$,2!$5$l$?;~(BinitSpeed$B$,(B1$B2C;;(B
        ballObj.setInitSpeed( 1 )
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        pressed_keys_cp[K_DOWN] = 1
        ballObj.moveAs2Key( pressed_keys_cp )
        print "test initspeed "+str(ballObj.getInitSpeed())
        self.assertTrue( 0 == ballObj.getInitSpeed() )

        # Down$B%-!<$,2!$5$l$?;~(BinitSpeed$B$,(B1$B2C;;(B
        # initSpeed$B$O(B0$B0J2<$K$J$i$J$$(B
        ballObj.setInitSpeed( 0 )
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        pressed_keys_cp[K_DOWN] = 1
        ballObj.moveAs2Key( pressed_keys_cp )
        print "test initspeed "+str(ballObj.getInitSpeed())
        self.assertTrue( 0 == ballObj.getInitSpeed() )

    def test_barInit(self):
        bar = BarObj()
        bar.setObj( "img/bar.bmp" )
        bar.setRect_pos( 150, 120 )

    def test_BallAndBarObj( self ):
        screen = PygScreen()
        screen.setSize(10,10)
        ball = BallObj()
        ball.setObj("img/ball.bmp")
        bar = BarObj()
        bar.setObj( "img/bar.bmp" )
        mediator = Mediator()

        self.setPosition( 
                ball, 150, 120, 
                bar,  150, 120 )
        self.assertTrue( True == mediator.isBallAndBarConflict( 
            ball.getBallrect(), bar.getRect() ) )

        self.setPosition( 
                ball, 120, 10, 
                bar,  120, 40,)
        self.assertTrue( True == mediator.isBallAndBarConflict( 
            ball.getBallrect(), bar.getRect() ) )

        self.setPosition( 
                ball, 120, 70, 
                bar,  120, 40,)
        self.assertTrue( True == mediator.isBallAndBarConflict( 
            ball.getBallrect(), bar.getRect() ) )

        self.setPosition( 
                ball, 120, 80, 
                bar,  120, 40,)
        self.assertTrue( False == mediator.isBallAndBarConflict( 
            ball.getBallrect(), bar.getRect() ) )

        ball.setSpeed( 1,1 )
        self.setPosition( 
                ball, 80, 120, 
                bar,  80, 120 )
        mediator.judgeConflictBallAndBar( 
            ball, bar )
        self.assertTrue( [1, -5] == ball.getSpeed() )

    def setPosition( self, 
            ball, ballY, ballX,
            bar,  barY,  barX):
        ball.setRect_pos( ballX, ballY )
        bar.setRect_pos(  barX,  barY )

if __name__ == "__main__":
    unittest.main()

