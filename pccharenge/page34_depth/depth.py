#!/usr/bin/python

def isAddable( num, array, dst ):
    if( 0 == dst ):
        return 0
    elif( 0 != dst ):
        return 1

    if( 0 == isAddable( num-1, array[num -2], dst-array[num-1])):
        return 0
    else:
        return isAddable( num-1, array[num-2], dst)

