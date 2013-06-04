# -*- coding:utf-8 -*-
import sys, pygame

class PygScreen():
    def __init__(self):
        self._size              = [0,0]
        self._drawSurfaceSize   = [0,0]
        self._screen            = None
        self._drawScreen        = None
    def setSize( self, sizeX, sizeY ):
        self._size = [sizeX, sizeY]
    def setDrawSurfaceSize( self, sizeX, sizeY ):
        self._drawSurfaceSize = [sizeX, sizeY]
    def getDisplay( self ):
        return self._screen
    def setDisplay( self ):
        self._screen = pygame.display.set_mode( self._size )
        pygame.display.set_caption( "Gatto Game" )
    def setDrawSurface( self ):
        self._drawScreen = pygame.transform.smoothscale(
                           self._screen,self._drawSurfaceSize)
    def getSize( self ):
        return self._drawSurfaceSize
    def displayFill( self, color ):
        self._drawScreen.fill( color )
    def displayBlit( self, ballObj, ballRect ):
        self._drawScreen.blit( ballObj, ballRect )
        self._screen.blit(
                pygame.transform.scale(self._drawScreen,self._size )
                ,(0,0))


