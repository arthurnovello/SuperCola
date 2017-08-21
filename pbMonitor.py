import time, sys, os
from AppKit import *
from saveToOutput import *

try:
    #Salva o que já esta no clipboard
    pb = NSPasteboard.generalPasteboard()
    pbstring = pb.stringForType_(NSStringPboardType)
   
    while True:
    	
    	newpb = NSPasteboard.generalPasteboard()
    	newpbstring = newpb.stringForType_(NSStringPboardType)
    	#Compara se houve mudança no clipboard
    	if pbstring != newpbstring:
    		#chama saveToOutput.py
    		save()
    		pbstring = newpbstring
    	#Pausa a execução do script
    	time.sleep(0.75)

except KeyboardInterrupt:
    
    print ("Interrupted")
    
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)