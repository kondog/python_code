# -*- coding:utf-8 -*-

import pygame

class WarpObj():
    def __init__(self):
        self._warpObj        = None
        self._warprect       = None
    def setObj( self, objPath ):
        # ここらへんの処理は各オブジェクトで共通化可能
        self._warpObj = pygame.image.load( objPath )
    def getObj( self ):
        return self._warpObj
    def setRect_pos( self, posx, posy ):
        self._warprect = self._warpObj.get_rect( center = (posx, posy ) )
    def getRect( self ):
        return self._warprect
