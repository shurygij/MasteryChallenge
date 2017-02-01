#!/usr/bin/python
def enc(inputString):
	outputString = ""
	for char in inputString:
		outputString += chr(ord(char) + 42)
	return str(outputString)
	
def dec(inputString):
	outputString = ""
	for char in inputString:
		outputString += chr(ord(char) - 42)
	return str(outputString)
	
strVal = "Hello World"
print strVal
encoded = enc(strVal)
print encoded
decoded = dec(encoded)
print decoded