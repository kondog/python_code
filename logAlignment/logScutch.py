#!/usr/bin/python
# coding:utf-8
import sys
import re
import datetime
import time
#入力：日時型を整理したいファイル
#出力：日時型が整理されファイル名が最後についた文字列
tuple4StrToDatetime = (
    "%a %b %d %H:%M:%S %Y",
)

str4DatetimeFormat = "%Y/%m/%d %H:%M:%S"

def scutchDatetime( inputStr ):
    for strToDatetime in tuple4StrToDatetime:
        try:
            myDatetime = datetime.datetime(
                *time.strptime( inputStr, strToDatetime )[:-3] )
        except ValueError:
            print "DEBUG:" + str( strToDatetime ) +" is not match for " +inputStr+ "."
    return myDatetime.strftime( str4DatetimeFormat )

def testScutchDatetime( inputStr, outputStr ):
    if scutchDatetime( inputStr ) == outputStr:
        print "OK";return True

def testAll():
    assert testScutchDatetime( "Sun Mar 2 06:30:04 2008", "2008/03/02 06:30:04" )

if __name__ == "__main__":
    testAll()
