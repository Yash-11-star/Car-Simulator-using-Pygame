#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket                
  
# Create a socket object 
s = socket.socket()          
  
# Define the port on which you want to connect 
port=1234      
  
# connect to the server on local computer 
s.connect(('127.0.0.1', port))     
recieve=s.recv(1024)
print (recieve.decode('utf-8')) 

chat=1

while(chat): 
    # receive data from the server
    msg=input("Enter your message  ")
    s.send(msg.encode('utf-8'))
    recieve=s.recv(1024)
    print (recieve.decode('utf-8')) 
    chat=int(input("Continue chatting 0/1:  "))
    # close the connection 
s.close()


# In[ ]:





# In[ ]:




