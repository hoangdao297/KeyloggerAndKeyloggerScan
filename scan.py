import wmi
 
f = wmi.WMI()
 
print("Process id   Process name") 
threat=[] #create an array in order to contain name of threats
for process in f.Win32_Process(): #use Win32_Process class
    if (process.Name[0:7]=="pythonw"): #detect .pythonw file extension program
     	print("\n-------THREAT DETECTED---------\n\n")
     	threat.append(process.Name)
     	process.Terminate() #Stop this threat
    print(f"{process.ProcessId:<10} {process.Name}\n")
if (len(threat)==0):
	print("No threat found")
else:
	print("\nThreats found: ",len(threat))
	print("\n------------------------------List---------------------------\n\n")
	print(threat)
	print("Stopped threats")
