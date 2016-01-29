# Import modules
import socket, os, atexit, webbrowser

'''def quit():
	print "Error 13: unexpected dc"
	s.send("Error 13: unexpected dc")
	s.close  

atexit.register(quit)'''

def openFiles():
	os.chdir("./recieved")
	for f in os.listdir(os.getcwd()):
	    if f != "foo.txt": 
			os.system("open "+f)

def openTabs():
	with open('./foo.txt') as f:
		for line in f:
			urls = line.split(',')
			for url in urls: 
				webbrowser.open_new_tab(url)

def runClient(ip):
	s = socket.socket()         

	# Initialize and wait for connection
	host = ip
	#host = socket.gethostname() 
	#host = '172.17.192.115'
	port = 5001           
	bufsize = 4096
	print "running client!"
	print host
	s.connect((host, port))

	print "Welcome to the server :)"

	numFiles = s.recv(1024)
	s.send('rec')

	print numFiles
	numFiles = int(numFiles)
	print numFiles

	for i in range(1,numFiles):
		fName = s.recv(1024)
		s.send('rec')
		print "recieving " + fName 
		data = "" 

		while True:
		  # Loop to recieve all buffered data until end message recieved
		  if (":endT:" in data): break
		  data += s.recv(bufsize)
		  #print 'writing file ...'

		# Open and write data to new file excluding end message  
		myfile = open("./recieved/"+fName, 'w')
		myfile.write(data[:-6])
		# Close file and send success message
		myfile.close()
		s.send('success')

	openFiles()
	openTabs()

	# Close the socket when done
	s.close   