#!/usr/bin/python
# coding:utf-8

import datetime
import sys

while(True):
    line = sys.stdin.readline()
    if line != "":
        print str( datetime.datetime.today() ) + line
