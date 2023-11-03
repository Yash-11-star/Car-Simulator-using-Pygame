#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket             
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
#AF_INET= IPv4, SOCK_STREM=TCP
print("Socket successfully created")

port = 1234               

s.bind(('', port))         
print ("socket binded to %s" %(port)) 
   
s.listen(10)      
print ("socket is listening")            
  
# a forever loop to keep it live 24*7
count=0
while True: 
    c, addr = s.accept()
    count=count+1
    print ('Got connection from', addr)
    message='Thank you for connecting, Client no. %s' %(count)
    c.send(message.encode('utf-8'))
    while True:
        recieve= c.recv(1024)
        print(recieve.decode('utf-8'))
        message=input("Enter your reply   ")
        c.send(message.encode('utf-8'))


# In[ ]:





# In[ ]:




