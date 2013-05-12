# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *

from systemData import SysData

class BallObj():
    def __init__(self):
        self.sysData        = SysData()
        self._initSpeed     = self.sysData.ballInitSpeed
        self._speed         = self.sysData.ballSpeed
        self._ballObj       = None
        self._ballrect      = None
        self._initSpeed_MAX = self.sysData.ballInitSpeed_MAX
        self._initSpeed_MIN = self.sysData.ballInitSpeed_MIN
        self._state         = self.sysData.stateIdle
        self._shootTiming   = 0
    # Obj
    def setObj( self, imgStr ):
        self._ballObj = pygame.image.load( imgStr )
    def getObj( self ):
        return self._ballObj

    # InitSpeed
    def setInitSpeed( self, initSpeed ):
        self._initSpeed = -1 * initSpeed
    def getInitSpeed( self ):
        return - self._initSpeed

    # Speed
    def setSpeed( self, speedX, speedY ):
        self._speed = [speedX, speedY]
    def setSpeedY( self, speedY ):
        self._speed[1] = speedY
    def getSpeed( self ):
        return self._speed
    def getSpeedX( self ):
        return self._speed[0]
    def getSpeedY( self ):
        return self._speed[1]

    # Rectunglar
    def getBallrect( self ):
        return self._ballrect
    def setRect( self ):
        self._ballrect = self._ballObj.get_rect()
    def setRect_pos( self, posx, posy ):
        self._ballrect = self._ballObj.get_rect( center = (posx, posy ))
    def setBallrectRight( self, rightVal ):
        self._ballrect.right = rightVal
    def setBallrectLeft( self, leftVal ):
        self._ballrect.left = leftVal
    def setBallrectBottom( self, bottomVal ):
        self._ballrect.bottom = bottomVal
    def ballMove( self ):
        self._ballrect = self._ballrect.move( self._speed )

    # State
    def setState( self, stateNum ):
        self._state = stateNum
    def getState( self ):
        return self._state
    def changeState( self, ssContainer ):
        # 通常状態
        if self.sysData.stateIdle == self._state:
            self.setState( self.sysData.stateLeft2Right )
            self.setSpeedY( 0 )
            self.setRect_pos( self.sysData.rightBarX
                            , self.sysData.barY - 10 )
        # 左から右
        elif self.sysData.stateLeft2Right == self.getState():
            self._shootTiming = 0
            self.setState( self.sysData.stateWait )
            # 衝突した時に左手から右手にワープ(Todo:ワープは変更したい)
            self.setSpeed( 0,0 )
            self.setRect_pos( self.sysData.rightBarX + 20
                            , self.sysData.barY - 20 )
        # 待機状態
        elif self.sysData.stateWait == self.getState():
            if self._shootTiming > 25:
                self._shootTiming = 0
                self.setState( self.sysData.stateRight2Left )
                self.setRect_pos( self.sysData.rightBarX
                                , self.sysData.barY - 10 )
        # 右から左
        elif self.sysData.stateRight2Left == self.getState():
            self.moveRight2Left( ssContainer )

    #shootTiming
    def getShootTiming( self ):
        return self._shootTiming
    def setShootTiming( self ):
        self._shootTiming = self._shootTiming+1
    shootTiming = property( getShootTiming, setShootTiming )
    def shootTimingIncliment( self ):
        self._shootTiming = self._shootTiming+1

    def moveRight2Left( self, ssContainer ):
        import random
        import time
        self.setState( self.sysData.stateLeft2Right )
        # HACK:横に飛ぶスピードを決定する
        # 発射時の初速度をサイトスワップに従って決定
        siteswap = ssContainer.pull()
        initSpeed = ssContainer.getInitSpeed( siteswap )

        # ボールの着地点を決定
        landingFlag = random.randint(0,1) 

        # 初速度とボールの着地点から横軸の速度を算出
        xSpeed = ssContainer.getVx( siteswap, landingFlag )
        self.setSpeed( -1.0*xSpeed ,-1.0*initSpeed )
        print "moveRight2Left siteswap, xSpeed, initSpeed"
        print str(siteswap) + ", " + str(xSpeed) + ", " + str(initSpeed)

    # 次のスクリーンのボールの位置を決定する
    def decideBallPosition( self, keyList, size):
        # キー押下時の位置を決定する
#        self.moveAs2Key( keyList )

        # 壁に衝突した時の動作
        if self._ballrect.left < 0 or self._ballrect.right > size[0]:
            self._speed[0] = -self._speed[0]
        if self._ballrect.bottom >= size[1]:
            self._speed[1] = self._initSpeed
        # 待機状態の時はボールを動かさない
        if self.sysData.stateWait == self.getState():
            pass
        # デフォルト動作
        else:
            self._speed[1] = self._speed[1] + self.sysData.accele 

    # キー押下時の動作
    def moveAs2Key( self, keyList ):
        if keyList[K_LEFT]:
            self._speed[0] = self._speed[0]-1
        if keyList[K_RIGHT]:
            self._speed[0] = self._speed[0]+1
        if keyList[K_UP]:
            if self._initSpeed > self._initSpeed_MAX:
                self._initSpeed = self._initSpeed - 1
        if keyList[K_DOWN]:
            if self._initSpeed < self._initSpeed_MIN:
                self._initSpeed = self._initSpeed + 1

