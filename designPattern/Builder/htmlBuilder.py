#!/usr/bin/python
# coding:utf-8

from builder import Builder

class HTMLBuilder( Builder ):
    strBuffer = []
    def makeTitle( self, str ):
        self.strBuffer.append(str + ".html\n")
        self.strBuffer.append("<html><head><title>" +str+ "</title></head><body>")
    def makeString( self, str ):
        self.strBuffer.append("<p>" +str+ "</p>")
    def makeItems( self, str ):
        for i in str:
            self.strBuffer.append("<li>"+i+ "</li>" )
    def close( self ):
        self.strBuffer.append("</body></html>")
    def getResult( self ):
        return self.strBuffer

