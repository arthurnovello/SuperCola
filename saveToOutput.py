from AppKit import *
import os, sys

def save():
	#Confere a quantidade de linhas presentes no arquivo
	with open('output.txt') as f:
		lines = sum(1 for _ in f)

	print("lines: ", lines, "\n")

	#Le o que está no clipboard
	pb = NSPasteboard.generalPasteboard()
	pbstring = pb.stringForType_(NSStringPboardType)
	print ("Pastboard string: ", pbstring,"\n")
	
	#Salva o que esta no clipboard na primeira linha do arquivo input.txt; 
	#adiciona o que já esta no output.txt no input.txt; 
	#por fim copia tudo de volta para o output.txt.
	inP = open('input.txt', 'w', encoding='utf-8')
	outP = open('output.txt', 'r', encoding='utf-8')
	inP.write(repr(pbstring))
	inP.write("\n")
	oldOutP = outP.readlines()
	inP.writelines([item for item in oldOutP])
	inP.close()
	outP.close()
	inP = open('input.txt', 'r', encoding='utf-8')
	f = open('output.txt', 'w', encoding='utf-8')
	f.writelines([item for item in inP.readlines()])
	f.close()
	inP.close()
	os.remove("input.txt")

	#Se o output.txt tiver +20 linhas, apaga a mais antiga
	if lines >= 20:
		print("+20 linhas, deleta ultima linha\n")
		readFile = open("output.txt")

		lines = readFile.readlines()

		readFile.close()
		w = open("output.txt",'w')

		w.writelines([item for item in lines[:-1]])
		w.close()
	
	#Mostra o que está no output.txt
	f2 = open('output.txt', 'r', encoding='utf-8')
	filestring = f2.read()
	print ("arquivo:\n")
	print (filestring)
	f2.close()