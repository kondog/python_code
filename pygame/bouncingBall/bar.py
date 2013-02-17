# -*- coding:utf-8 -*-

import pygame

class BarObj():
    def __init__( self ):
        self._initSpeed     = 0
        self._speed         = [0,0]
        self._barObj        = None
        self._barrect       = None
        self._initSpeed_MAX = None
        self._initSpeed_MIN = None

    def setObj( self, objPath ):
        self._barObj = pygame.image.load( objPath )
    def getObj( self ):
        return self._barObj
    def setRect( self ):
        self._barrect = self._barObj.get_rect()
    def getRect( self ):
        return self._barrect
    def setRect_pos( self, posx, posy ):
        self._barrect = self._barObj.get_rect( center = (posx, posy ))


