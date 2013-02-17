# -*- coding:utf-8 -*-

from ball import BallObj
from bar  import BarObj

class Mediator():
    def __init__(self):
        pass
    def isBallAndBarConflict(self, ball, bar ):
        distanceXBarBall = abs(ball.center[0] - bar.center[0])
        distanceYBarBall = abs(ball.center[1] - bar.center[1])
        lengthXBarEnd2Center = (bar.right - bar.left) / 2
        lengthYBarEnd2Center = (bar.bottom - bar.top) / 2
        if distanceXBarBall <= lengthXBarEnd2Center and \
           distanceYBarBall <= lengthYBarEnd2Center:
            return True
        else:
            return False
    def judgeConflictBallAndBar( self, ball, bar ):
        if self.isBallAndBarConflict( ball.getBallrect(), bar.getRect() ):
            ball.setSpeedY( -ball.getInitSpeed() )
            print ball.getSpeed()
