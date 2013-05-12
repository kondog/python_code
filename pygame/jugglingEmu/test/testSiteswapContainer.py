# -*- coding:utf-8 -*-

import pygame
import sys,os
sys.path.append( os.pardir )
import unittest
from siteswapContainer import SiteSwapContainer

class TestFunctions( unittest.TestCase ):
    def testMakeContainer(self):
        ssc = SiteSwapContainer()
        ssc.makeContainer(1)
        self.assertTrue( ssc.siteswap == [5,5,5] )
    def testPull(self):
        ssc = SiteSwapContainer()
        ssc.makeContainer( 1 )
        self.assertTrue( ssc.pull() == 5 )
        self.assertTrue( ssc.siteswap == [5,5] )
        ssc.pull()
        ssc.pull()
        print "★ 何か値が出てればいい★ "
        print ssc.siteswap

if __name__ == "__main__":
    unittest.main()

