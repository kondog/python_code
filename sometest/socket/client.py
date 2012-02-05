import socket

host = socket.gethostbyname( "localhost" )
port = 10000

so = socket.socket()
so.connect((host,port))

so.send( "test." )

data = so.recv( 8192 )

so.close()

print data

