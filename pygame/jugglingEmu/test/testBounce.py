# -*- coding:utf-8 -*-

import unittest
import pygame
from pygame.locals import *

from main        import PygScreen
from ball        import BallObj
from bar         import BarObj
from objMediator import Mediator
from systemData  import SysData

class TestFunctions( unittest.TestCase ):
    sysData = SysData()

    # ボールの位置とスピードが正しく移行するかどうか
    def isCorrectSpeedChange( self, position, speed_before, key, speed_after ):
        # init object.
        pygame.init()
        screen = PygScreen()
        screen.setSize(100,100)
        ball = BallObj()
        ball.setObj( self.sysData.ballBmp )
        ball.setRect()

        # 判定処理
        ball.setBallrectLeft( position[0] )
        ball.setBallrectBottom( position[1] )
        ball.setSpeed( speed_before[0], speed_before[1] )
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        if key != None:
            pressed_keys_cp[key] = 1

        ball.decideBallPosition( pressed_keys_cp, screen.getSize() )
        return speed_after == ball.getSpeed()

    def test_decideBallPosition(self):
        # ボールのX値がスクリーンサイズオーバの時スピードのX値が逆転
        self.assertTrue( self.isCorrectSpeedChange( 
                [500,50],   [1,1],         None,
               #ボール位置, 試験対象speed, 押下キー
                [-1,1+self.sysData.accele],))
               #試験後のspeed

        # ボールのY値がスクリーンサイズオーバの時スピードのY値が初速
        self.assertTrue( self.isCorrectSpeedChange( 
                [50,200], [1,1], None,
                [1,self.sysData.ballInitSpeed],))

        # ボールのY値がスクリーンサイズ内の時スピードのY値が減速
        self.assertTrue( self.isCorrectSpeedChange( 
                [50,50], [2,-3], None,
                [2,-3+self.sysData.accele],))

        # ボールのY値がスクリーンサイズ内の時スピードのY値が減速
        # かつ右キーが押されていた時スピードのX値が増大
        self.assertTrue( self.isCorrectSpeedChange( 
                [50,50], [1,-3], K_RIGHT,
                [1,-3+self.sysData.accele],))

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
        self.assertTrue( 0 == ballObj.getInitSpeed() )

        # Downキーが押された時initSpeedが1加算
        # initSpeedは0以下にならない
        ballObj.setInitSpeed( 0 )
        pressed_keys_cp = \
            self.makeListFromKeyTuple( pygame.key.get_pressed() )
        pressed_keys_cp[K_DOWN] = 1
        ballObj.moveAs2Key( pressed_keys_cp )
        self.assertTrue( 0 == ballObj.getInitSpeed() )

    def test_barInit(self):
        bar = BarObj()
        bar.setObj( "img/bar.bmp" )
        bar.setRect_pos( 150, 120 )

    # ボールとバーのテスト
    def test_BallAndBarObj( self ):
        screen = PygScreen()
        screen.setSize(10,10)
        ball = BallObj()
        ball.setObj("img/ball.bmp")
        bar = BarObj()
        bar.setObj( "img/bar.bmp" )
        mediator = Mediator()

        # 衝突した際の動作
        self.setPosition( ball, 150, 120,  bar,  150, 120 ) #center
                         #ObjA,   X,   Y, ObjB,    X,   Y
        self.assertTrue( True == mediator.isBallAndBarConflict( 
            ball.getBallrect(), bar.getRect() ) )
        self.setPosition( ball, 120, 10,   bar,  120, 40,)  #left
        self.assertTrue( True == mediator.isBallAndBarConflict( 
            ball.getBallrect(), bar.getRect() ) )
        self.setPosition( ball, 120, 70,   bar,  120, 40,)  #right
        self.assertTrue( True == mediator.isBallAndBarConflict( 
            ball.getBallrect(), bar.getRect() ) )
        self.setPosition( ball, 120, 80,   bar,  120, 40,)  #none
        self.assertTrue( False == mediator.isBallAndBarConflict( 
            ball.getBallrect(), bar.getRect() ) )
        ball.setState( self.sysData.stateIdle )         #状態が変化するか idel->L2R
        self.setPosition( ball, 80, 120,   bar,  80, 120 )
        mediator.judgeConflictBallAndBar( ball, bar )
        self.assertTrue( self.sysData.stateLeft2Right == ball.getState() )
        ball.setState( self.sysData.stateLeft2Right )         #状態が変化するか L2R->R2L
        self.setPosition( ball, 80, 120,   bar,  80, 120 )
        mediator.judgeConflictBallAndBar( ball, bar )
        self.assertTrue( self.sysData.stateRight2Left == ball.getState() )

    def setPosition( self, 
            ball, ballY, ballX, bar,  barY,  barX):
        ball.setRect_pos( ballX, ballY )
        bar.setRect_pos(   barX,  barY )

if __name__ == "__main__":
    unittest.main()

