from socket import *
import ssl
import base64

subject = "I love computer networks!"
contenttype = "text/plain"
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = ("smtp.gmail.com", 587)#Fill in start #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
# Send HELO command and print server response. 
heloCommand = 'HELO Alice\r\n' 
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server. (recv1)')

tls = "STARTTLS\r\n"
clientSocket.send(tls.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv[:3] != '220':
    print('220 reply not received from server.')
clientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23)

heloCommand = 'HELO Alice\r\n' 
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server. (recv1)')

# login info
fromaddress = "" # put your src email here
password = "" # put your src password here

toaddress = "" # put the dest. email here

#login
authMsg = "AUTH PLAIN\r\n"
clientSocket.send(authMsg.encode())
base64_str = ("\x00"+fromaddress+"\x00"+password).encode()
auth = base64.b64encode(base64_str) + "\r\n".encode()
clientSocket.send(auth)
recv1 = clientSocket.recv(1024).decode()
print(recv1)

# Fill in start
mailFromCommand = "MAIL FROM:<tong.johnson.28@gmail.com>\r\n"
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
# Fill in end

# Send RCPT TO command and print server response.
# Fill in start
clientSocket.send(('RCPT TO: <' + toaddress + '>\r\n').encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
# Fill in end

# Send DATA command and print server response.
# Fill in start
clientSocket.send(('DATA\r\n').encode())
recv = clientSocket.recv(1024).decode()
print(recv)
# Fill in end

# Send message data.
# Fill in start
message = 'from:' + fromaddress + '\r\n'
message += 'to:' + toaddress + '\r\n'
message += 'subject:' + subject + '\r\n'
message += 'Content-Type:' + contenttype + '\r\n'
message += '\r\n' + msg
clientSocket.sendall(message.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.sendall(endmsg.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quit = "QUIT\r\n"
clientSocket.send(quit.encode())
recv5 = clientSocket.recv(1024)
print(recv5.decode())
clientSocket.close()
# Fill in end