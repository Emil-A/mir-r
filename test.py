import subprocess, os, webbrowser
def getOpenData(fk):
	output = []
	#.pages
	output.extend(subprocess.check_output("lsof | awk '/.pages$/ {print $9}'", shell=True).split('\n')[:1])
	#.png
	output.extend(subprocess.check_output("lsof +D '/Users/' | awk '/.png/ {print $9}'", shell=True).split('\n')[:1])
	#.txt
	output.extend(subprocess.check_output("lsof | awk '/.txt$/ {print $9}'", shell=True).split('\n')[:1])
	#.docx
	output.extend(subprocess.check_output("lsof | awk '/.docx$/ {print $9}'", shell=True).split('\n')[:1])
	#.jpg
	output.extend(subprocess.check_output("lsof | awk '/.jpg$/ {print $9}'", shell=True).split('\n')[:1])
	#.gif
	output.extend(subprocess.check_output("lsof | awk '/.gif$/ {print $9}'", shell=True).split('\n')[:1])
	#.mp3
	output.extend(subprocess.check_output("lsof | awk '/.mp3$/ {print $9}'", shell=True).split('\n')[:1])
	#.mp4
	output.extend(subprocess.check_output("lsof | awk '/.mp4$/ {print $9}'", shell=True).split('\n')[:1])
	#.pdf
	output.extend(subprocess.check_output("lsof +D '/Users/' | awk '/.pdf/ {print $9}'", shell=True).split('\n')[:1])
	return output
#print getOpenData("")

def openFiles(fk):
	os.chdir("./recieved")
	for f in os.listdir(os.getcwd()):
	    if f != "foo.txt": 
			os.system("open "+f)

def openTabs(fk):
	with open('./foo.txt') as f:
		for line in f:
			print line
			webbrowser.open_new_tab(line)

#openFiles("")
openTabs("")