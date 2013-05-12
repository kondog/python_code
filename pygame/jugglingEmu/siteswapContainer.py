# -*- coding:utf-8 -*-

import pygame
from systemData    import SysData

class SiteSwapContainer():
    def __init__( self ):
        self._siteswap = [5]
        
        # ボールの初速度はサイトスワップの配列
        self._initSpeed = { 3:  5.0
                           ,5: 10.0
                           ,7: 15.0
                           ,9: 20.0 }
        
        # vxはサイトスワップとボール着地点の2次元配列
        self._vx = [[0 for j in range(2)] for i in range(10) ]
        self._vx[3][0] = 8.0
        self._vx[3][1] = 5.0
        self._vx[5][0] = 4.0
        self._vx[5][1] = 3.0
        self._vx[7][0] = 3.0
        self._vx[7][1] = 2.0
        self._vx[9][0] = 2.0
        self._vx[9][1] = 1.5

    def getSiteswap(self):
        return self._siteswap
    siteswap = property( getSiteswap )
    def getInitSpeed( self, siteswap ):
        return self._initSpeed[siteswap]
    def getVx( self, siteswap, landingFlag ):
        return self._vx[siteswap][landingFlag]

    # サイトスワップリストを作成する
    def makeContainer(self, option):
        if option == 1:
            self._siteswap = [5,5,5]
        elif option == 2:
            #self._siteswap = [5,5,5]
            self._siteswap = [7,3]
        elif option == 3:
            #self._siteswap = [5,5,5]
            self._siteswap = [9,3,3]
    
    # サイトスワップリストからpullする
    # リストがなくなった場合補充する
    def pull( self ):
        returnValue = self._siteswap[0]
        del self._siteswap[0]
        if len(self._siteswap) == 0:
            import random
            self.makeContainer( random.randint( 1, 3 ))
        return returnValue

