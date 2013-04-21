# -*- coding:utf-8 -*-

from ball import BallObj
from bar  import BarObj

class Mediator():
    def __init__(self):
        pass
    # ボールとバーが衝突した際の動作を定義
    def isBallAndBarConflict(self, ball, bar ):
        # ボールとバーの距離算出
        distanceXBarBall = abs(ball.center[0] - bar.center[0])
        distanceYBarBall = abs(ball.center[1] - bar.center[1])
        lengthXBarEnd2Center = (bar.right - bar.left) / 2
        lengthYBarEnd2Center = (bar.bottom - bar.top) / 2
        # 接触しているかどうか判定
        if distanceXBarBall <= lengthXBarEnd2Center and \
           distanceYBarBall <= lengthYBarEnd2Center:
            return True
        else:
            return False
    
    # ボールとバーが衝突したかどうかを判定し動作を決定する。
    def judgeConflictBallAndBar( self, ball, bar ):
        if self.isBallAndBarConflict( ball.getBallrect(), bar.getRect() ):
            ball.changeState( )



