# -*- coding:utf-8 -*-

class SysData():
    def __init__(self):
        self._ballInitSpeed     = -5
        self._ballSpeed         = [0,0]
        self._ballInitSpeed_MAX = -15
        self._ballInitSpeed_MIN = 0
        self._screenColor       = 255,255,255
        self._screenSizeX       = 320
        self._screenSizeY       = 240
        self._ballBmp           = "img/ball.bmp"
        self._barBmp            = "img/bar.bmp"
        self._waitTime    = 0.05
    def getBallInitSpeed(self):
        return self._ballInitSpeed
    def getBallSpeed(self):
        return self._ballSpeed
    def getBallSpeedMax(self):
        return self._ballInitSpeed_MAX
    def getBallSpeedMin( self):
        return self._ballInitSpeed_MIN
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
    def getScreenWait( self ):
        return self._waitTime
    ballInitSpeed     = property( getBallInitSpeed )
    ballSpeed         = property( getBallSpeed )
    ballInitSpeed_MAX = property( getBallSpeedMax )
    ballInitSpeed_MIN = property( getBallSpeedMin )
    screenColor       = property( getScreenColor )
    screenSizeX       = property( getScreenSizeX )
    screenSizeY       = property( getScreenSizeY )
    ballBmp           = property( getBallBmp )
    barBmp            = property( getBarBmp )
    waitTime          = property( getScreenWait )

