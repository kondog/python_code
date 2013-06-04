# -*- coding:utf-8 -*-

import sys, pygame
import unittest
import time
from pygame.locals import *

from ball          import BallObj
from bar           import BarObj
from screen        import PygScreen
from objMediator   import Mediator
from systemData    import SysData

if __name__ == "__main__":
    sysData = SysData()
    white   = sysData.screenColor

    pygame.init()

    screen = PygScreen()
    screen.setSize( sysData.screenSizeX,sysData.screenSizeY)
    screen.setDisplay( )
    screen.setDrawSurfaceSize( 
            sysData.screenSizeX*2,sysData.screenSizeY*2)
    screen.setDrawSurface()

    balls = []

    barLeft = BarObj()
    barLeft.setObj( sysData.barBmp)
    barLeft.setRect_pos( sysData.leftBarX, sysData.barY )

    barRight = BarObj()
    barRight.setObj( sysData.barBmp)
    barRight.setRect_pos( sysData.rightBarX, sysData.barY )

    mediator = Mediator()

    ballMakeTiming  = 0
    ballShootTiming = 0

    clock = pygame.time.Clock()
    while True:
        clock.tick(sysData.waitTime)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        # ボール生成部分
        # TODO: ボール生成個数とボール射出タイミングはsysDataに移動
        if len(balls) < 3:
            ballMakeTiming = ballMakeTiming + 1
            if ballMakeTiming > 22:
                ball = BallObj()
                ball.setSpeed( 0, 0 )
                ball.setObj( sysData.ballBmp )
                ball.setRect_pos( 60,-100 )
                balls.append( ball )
                ballMakeTiming = 0

        # ボールの次のフレームの動作
        for ball in balls:
            ball.ballMove()
            ball.decideBallPosition(pygame.key.get_pressed(), 
                                    screen.getSize() )
        #print balls[0].getBallrect()

        # ボールとバーが衝突した際の動作
        for ball in balls:
            mediator.judgeConflictBallAndBar( ball, barRight )
            mediator.judgeConflictBallAndBar( ball, barLeft )

        # ボールの射出間隔調整
        for ball in balls:
            if ball.getState() == sysData.stateWait:
                ball.shootTimingIncliment()
                break

        # キーが押されたときバーを移動
        barLeft.moveAs2Key( pygame.key.get_pressed())

        # 表示
        screen.displayFill( white )
        for ball in balls:
            screen.displayBlit( ball.getObj(), ball.getBallrect() )
        screen.displayBlit( barRight.getObj(), barRight.getRect() )
        screen.displayBlit( barLeft.getObj(),  barLeft.getRect() )
        pygame.display.flip()

