import socket

def receive():
    s=socket.socket()
    host='127.0.0.1'
    
    s.connect((host,7001))
    f=open('received.txt','wb')
        
    while True:
        print ("Receiving data from clients :\n")
        data=s.recv(1024)
        print("\n"+str(data)+"\n")
        if not data:
            break
        f.write(data)
            
    f.close()
    print("\nConnection closed ")
    s.close()
    
    
