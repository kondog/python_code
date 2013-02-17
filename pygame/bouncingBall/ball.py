# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *

class BallObj():
    def __init__(self):
        self._initSpeed     = -5
        self._speed         = [0,0]
        self._ballObj       = None
        self._ballrect      = None
        self._initSpeed_MAX = -10
        self._initSpeed_MIN = 0

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
        print "ballMove      : " + str( self._ballrect )
        self._ballrect = self._ballrect.move( self._speed )

    def decideBallPosition( self, keyList, size):
        self.moveAs2Key( keyList )
        if self._ballrect.left < 0 or self._ballrect.right > size[0]:
            self._speed[0] = -self._speed[0]
        if self._ballrect.bottom >= size[1]:
            self._speed[1] = self._initSpeed
        else:
            self._speed[1] = self._speed[1] + 1 

    def moveAs2Key( self, keyList ):
        print self._initSpeed
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

