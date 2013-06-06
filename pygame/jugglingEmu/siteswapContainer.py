# -*- coding:utf-8 -*-

import pygame
from systemData    import SysData

class SiteSwapContainer():
    def __init__( self ):
        self._siteswap = [5,5,5]
        
        # ボールの初速度はサイトスワップの配列
        self._initSpeed = { 3: 10
                           ,5: 20
                           ,7: 35
                           ,9: 43 }
        
        # vxはサイトスワップとボール着地点の2次元配列
        # TODO: 2桁使って着弾点をより細かくしたい。。
        self._vx = [[0 for j in range(2)] for i in range(10) ]
        self._vx[3][0] = 15
        self._vx[3][1] = 23
        self._vx[5][0] = 8
        self._vx[5][1] = 12
        self._vx[7][0] = 5
        self._vx[7][1] = 7
        self._vx[9][0] = 4
        self._vx[9][1] = 6

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
            self._siteswap = [7,3]
        elif option == 3:
            self._siteswap = [9,3,3]
        #簡易テスト用
        #if option == 1:
        #    self._siteswap = [3,3,3]
        #elif option == 2:
        #    self._siteswap = [3,3]
        #elif option == 3:
        #    self._siteswap = [3,3,3]
    
    # サイトスワップリストからpullする
    # リストがなくなった場合補充する
    def pull( self ):
        returnValue = self._siteswap[0]
        del self._siteswap[0]
        if len(self._siteswap) == 0:
            import random
            self.makeContainer( random.randint( 1, 3 ))
        return returnValue

