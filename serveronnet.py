import socket                   # Import socket module
import time
port = 6000                   # Reserve a port for your service.
s = socket.socket()             # Create a socket object
#host = socket.gethostname()     # Get local machine name
s.bind(('', port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'

conn, addr = s.accept() 
while True:
        # Establish connection with client.
    print 'Got connection from', addr
    data = conn.recv(1024)
    print('Server received', repr(data))

    with open('input.txt', 'wb') as f:
        print('receiving data...')
        #data = conn.recv(1024)
        #print('data=%s', (data))
        if not data:
            break
        # write data to a filese
        f.write(data)

    print('Done receiving')
    f.close()

    sf=open('output.txt','rb')
    print('done sending')
    l=sf.read(1024)
    conn.send(l)
    sf.close()

    time.sleep(5)
