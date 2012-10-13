#!/usr/bin/python
# coding:utf-8
import sys
from textBuilder import TextBuilder
from htmlBuilder import HTMLBuilder
from director    import Director

def doConstruct( builder ):
    director = Director( builder )
    for i in director.construct():
        print i

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: argument must be print or html."
        quit()
    if sys.argv[1] == "print":
        doConstruct( TextBuilder() )
    if sys.argv[1] == "html":
        doConstruct( HTMLBuilder() )

