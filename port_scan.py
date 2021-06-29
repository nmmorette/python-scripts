#-*- coding: utf-8 -*-
#!/usr/bin/python
import socket,sys

for porta in range (1,65535):
    meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if meusocket.connect_ex((sys.argv[1],porta)) == 0:
        
        banner = meusocket.recv(1024)
        print "Porta",porta, "[ABERTA]\n", "SERVIÇO",banner
        meusocket.close()

