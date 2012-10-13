#!/usr/bin/python
# coding:utf-8
from builder import Builder
class TextBuilder( Builder ):
    def __init__( self ):
        self._strBuffer = []
    def makeTitle( self, str ):
        self._strBuffer.append("------------\n")
        self._strBuffer.append(str + "\n")
    def makeString( self, str ):
        self._strBuffer.append("*" + str +"\n")
    def makeItems( self, str ):
        for i in str:
            self._strBuffer.append( i + "\n" )
    def close( self ):
        self._strBuffer.append("------------\n")
    def getResult( self ):
        return self._strBuffer

