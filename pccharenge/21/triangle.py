#! /usr/bin/python

def triangle( sticks ):
    array_length = len( sticks )
    print array_length

    if (  array_length < 3 | array_length > 100 ) :
        return 0
    
    else:
        sticks.sort()
        print sticks
        counter = -1
        while counter + array_length > 1:
            print counter
            if sticks[ counter ] < ( sticks[ counter -1 ] + sticks[ counter -2 ]):
                print str(sticks[counter]) + str(sticks[counter-1])+str(sticks[counter-2])
                return sticks[ counter ] + sticks[ counter -1 ] + sticks[ counter -2]
            else:
                counter = counter -1
        print "triangle cannot make"
        return 0

print triangle( [ 4,5,10,20] )
