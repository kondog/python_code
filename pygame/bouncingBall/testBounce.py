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

        # ボールのX値がスクリーンサイズオーバの時スピードのX値が逆転
        ballObj.setBallrectRight(500)
        ballObj.setSpeed(1,1)
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        ballObj.decideBallPosition( pressed_keys_cp, screen.getSize() )
        self.assertTrue( ballObj.getSpeedX() == -1 )

        # ボールのY値がスクリーンサイズオーバの時スピードのY値が初速
        ballObj.setBallrectBottom(240)
        ballObj.setSpeed(1,1)
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        ballObj.decideBallPosition( pressed_keys_cp, screen.getSize() )
        self.assertTrue( ballObj.getSpeedY() == -5 )

        # ボールのY値がスクリーンサイズ内の時スピードのY値が減速
        ballObj.setBallrectBottom(1)
        ballObj.setSpeed(1,-3)
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        ballObj.decideBallPosition( pressed_keys_cp, screen.getSize() )
        self.assertTrue( ballObj.getSpeedY() == -2 )

        # ボールのY値がスクリーンサイズ内の時スピードのY値が減速
        # かつ右キーが押されていた時スピードのX値が増大
        ballObj.setBallrectRight(5)
        ballObj.setBallrectLeft(5)
        ballObj.setBallrectBottom(1)
        ballObj.setSpeed(1,-3)
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        pressed_keys_cp[K_RIGHT] = 1
        ballObj.decideBallPosition( pressed_keys_cp, screen.getSize() )
        self.assertTrue( [2,-2] == ballObj.getSpeed() )

    # 試験用に一式のtupleを作成する
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

        # Leftキーが押された時speedXが1減算
        ballObj.setSpeed( 1,1 )
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        pressed_keys_cp[K_LEFT] = 1
        ballObj.moveAs2Key( pressed_keys_cp )
        self.assertTrue( [0,1] == ballObj.getSpeed() )

        # Rightキーが押された時speedXが1加算
        ballObj.setSpeed( 1,1 )
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        pressed_keys_cp[K_RIGHT] = 1
        ballObj.moveAs2Key( pressed_keys_cp )
        self.assertTrue( [2,1] == ballObj.getSpeed() )

        # Upキーが押された時initSpeedが1加算
        ballObj.setInitSpeed( 5 )
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        pressed_keys_cp[K_UP] = 1
        ballObj.moveAs2Key( pressed_keys_cp )
        self.assertTrue( 6 == ballObj.getInitSpeed() )

        # Upキーが押された時initSpeedが1加算
        ballObj.setInitSpeed( 20 )
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        pressed_keys_cp[K_UP] = 1
        ballObj.moveAs2Key( pressed_keys_cp )
        self.assertTrue( 20 == ballObj.getInitSpeed() )

        # Downキーが押された時initSpeedが1加算
        ballObj.setInitSpeed( 1 )
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        pressed_keys_cp[K_DOWN] = 1
        ballObj.moveAs2Key( pressed_keys_cp )
        print "test initspeed "+str(ballObj.getInitSpeed())
        self.assertTrue( 0 == ballObj.getInitSpeed() )

        # Downキーが押された時initSpeedが1加算
        # initSpeedは0以下にならない
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

