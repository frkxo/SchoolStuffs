import socket

website = input("Enter website URL: ")
print("IP of the website is: ", socket.gethostbyname(website))
