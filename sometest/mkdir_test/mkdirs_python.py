import os

cnt = 0

while ( cnt < 10 ):
    print( cnt )
    os.mkdir( "test"+str(cnt) );
    cnt += 1

