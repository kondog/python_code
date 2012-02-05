#! /usr/bin/python

def fib( input ):
    if( 0 == input ):
        return 0
    elif( 1 == input ):
        return 1
    else:
        return fib( input-1 ) + fib( input-2 )

print fib( 1 )
print fib( 2 )
print fib( 3 )

