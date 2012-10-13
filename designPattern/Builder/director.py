#!/usr/bin/python
# coding:utf-8

from builder import Builder

class Director():
    def __init__( self, builder ):
        self.__builder = builder
    def construct(self):
        self.__builder.makeTitle("title")
        self.__builder.makeString("string")
        self.__builder.makeItems(["morning","noon","night"])
        self.__builder.close()
        return self.__builder.getResult()

