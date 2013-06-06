# -*- coding:utf-8 -*-

class SysData():
    def __init__(self):
        self._ballInitSpeed     = -20
        self._ballSpeed         = [0,0]
        self._ballInitSpeed_MAX = -15
        self._ballInitSpeed_MIN = 0
        self._leftBarX          = 60*2
        self._rightBarX         = 340*2
        self._screenSizeY       = 650
        self._barY              = self._screenSizeY*2 - 50
        self._screenColor       = 255,255,255
        self._screenSizeX       = 400
        self._ballBmp           = "img/ball.bmp"
        self._barBmp            = "img/bar.bmp"
        self._warpBMP           = "img/warp.bmp"
        self._waitTime          = 100
        self._accele            = 0.9
        # 状態設定値
        self._stateIdle         = 0
        self._stateWait         = 1
        self._stateLeft2Right   = 2
        self._stateRight2Left   = 3
    def getBallInitSpeed(self):
        return self._ballInitSpeed
    def getBallSpeed(self):
        return self._ballSpeed
    def getBallSpeedMax(self):
        return self._ballInitSpeed_MAX
    def getBallSpeedMin( self):
        return self._ballInitSpeed_MIN
    def getLeftBarX( self):
        return self._leftBarX
    def getRightBarX( self):
        return self._rightBarX
    def getBarY( self):
        return self._barY
    def getScreenColor( self ):
        return self._screenColor
    def getScreenSizeX( self ):
        return self._screenSizeX
    def getScreenSizeY( self ):
        return self._screenSizeY
    def getBallBmp( self ):
        return self._ballBmp
    def getBarBmp( self ):
        return self._barBmp
    def getWarpBmp( self ):
        return self._warpBMP
    def getScreenWait( self ):
        return self._waitTime
    def getAccele( self ):
        return self._accele
    def getStateIdle( self ):
        return self._stateIdle
    def getStateWait( self ):
        return self._stateWait
    def getStateLeft2Right( self ):
        return self._stateLeft2Right
    def getStateRight2Left( self ):
        return self._stateRight2Left
    ballInitSpeed     = property( getBallInitSpeed )
    ballSpeed         = property( getBallSpeed )
    ballInitSpeed_MAX = property( getBallSpeedMax )
    ballInitSpeed_MIN = property( getBallSpeedMin )
    leftBarX          = property( getLeftBarX )
    rightBarX         = property( getRightBarX )
    barY              = property( getBarY )
    screenColor       = property( getScreenColor )
    screenSizeX       = property( getScreenSizeX )
    screenSizeY       = property( getScreenSizeY )
    ballBmp           = property( getBallBmp )
    barBmp            = property( getBarBmp )
    warpBmp           = property( getWarpBmp)
    waitTime          = property( getScreenWait )
    accele            = property( getAccele )
    stateIdle         = property( getStateIdle )
    stateWait         = property( getStateWait )
    stateLeft2Right   = property( getStateLeft2Right )
    stateRight2Left   = property( getStateRight2Left )

