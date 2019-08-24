import socket

def sent(filename):

    s=socket.socket()
    host='127.0.0.1'
    port=7001
    s.bind((host,port))
    s.listen(2)
    
    c,addr=s.accept()
    
    #filename='a1.py'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
        c.send(l)
        print('Sent ',repr(l))
        l=f.read(1024)
    f.close()
    
    print("Done Sending ")
    s.close()
    
