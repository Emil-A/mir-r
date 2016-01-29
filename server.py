# Import modules
import socket, os, subprocess, time   
from os.path import expanduser      

def runHost(files):
  # Initialize and wait for connection
  s = socket.socket()         
  host = socket.gethostname() 
  port = 5000           
  bufsize = 4096
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  s.bind((host, port))       
  print "running host!"
  s.listen(5)
  while True:
    # Establish connection with client.
    c, addr = s.accept()    
    print 'Got connection from', addr
    print files
    # Send command and print recieved output
    #files = []
    c.send(str(len(files)))
    print c.recv(1024)
    for f in files:
      print "sending"
      print f
      fName = os.path.basename(f)
      if os.path.isfile(f):
        c.send(fName)
        print c.recv(1024)

        bytes = open(f).read()
        c.send(bytes)
        c.send(":endT:")
        print c.recv(1024)
      else:
        print "File does not exist"
  

  # Close the connection
  c.close()

def getOpenData(output):
  #.docx
  output.extend(subprocess.check_output("lsof | awk '/.docx$/ {print $9}'", shell=True).strip().splitlines())
  #.png
  #output.extend(subprocess.check_output("lsof +D '/Users/' | awk '/.png/ {print $9}'", shell=True).strip().splitlines())
  #.txt
  #output.extend(subprocess.check_output("lsof | awk '/.txt$/ {print $9}'", shell=True).strip().splitlines())
  #.docx
  #output.extend(subprocess.check_output("lsof | awk '/.docx$/ {print $9}'", shell=True).strip().splitlines())
  #.jpg
  #output.extend(subprocess.check_output("lsof | awk '/.jpg$/ {print $9}'", shell=True).strip().splitlines())
  #.gif
  #output.extend(subprocess.check_output("lsof | awk '/.gif$/ {print $9}'", shell=True).strip().splitlines())
  #.mp3
  output.extend(subprocess.check_output("lsof | awk '/.mp3$/ {print $9}'", shell=True).strip().splitlines())
  #.mp4
  output.extend(subprocess.check_output("lsof | awk '/.MOV$/ {print $9}'", shell=True).strip().splitlines())
  #.ppt
  #output.extend(subprocess.check_output("lsof | awk '/.ppt$/ {print $9}'", shell=True).strip().splitlines())
  #.xlsx
  #output.extend(subprocess.check_output("lsof | awk '/.xlsx$/ {print $9}'", shell=True).strip().splitlines())
  #.pdf
  output.extend(subprocess.check_output("lsof +D '/Users/' | awk '/.pdf/ {print $9}'", shell=True).strip().splitlines())
  #browser tabs
  os.system("./hello")
  home = expanduser("~")
  output.append(home+"/Desktop/foo.txt")

def getIP():
  return socket.gethostbyname(socket.gethostname())

