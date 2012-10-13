#!/usr/bin/python
# coding:utf-8
import abc

class Builder():
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def makeTitle():
        pass
    @abc.abstractmethod
    def makeString():
        pass
    @abc.abstractmethod
    def makeItems():
        pass
    @abc.abstractmethod
    def close():
        pass
    @abc.abstractmethod
    def getResult():
        pass
