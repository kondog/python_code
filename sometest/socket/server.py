import socket

host = socket.gethostbyname( "localhost" )
port = 10000

so = socket.socket()
so.bind( ( host, port ) )
so.listen( 1 )

while True:
    conn, address = so.accept
    print address

    data = conn.recv( 8192 )
    print data

    conn.send( data )
    conn.close()

