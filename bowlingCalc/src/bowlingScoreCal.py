#!/usr/bin/python
#-*- conding: utf-8 -*-

class BowlingScoreCal():
    def readInputArray( self, inputArray ):
        n = 0
        oneFramePoint_ = inputArray[0][0] + inputArray[0][1]
        if len( inputArray ) == 1:
            return oneFramePoint_
        if oneFramePoint_ == 10:
            return oneFramePoint_ +\
                   inputArray[1][0]*2 + inputArray[1][1] +\
                   self.readInputArray( inputArray[2:] )
        else:
            oneFrameArray = inputArray[0]
            oneFramePoint = oneFrameArray[0] + oneFrameArray[1]
            return oneFramePoint + self.readInputArray( inputArray[1:] )



