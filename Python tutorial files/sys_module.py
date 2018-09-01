#"sys" module provides access to variables and functions related
# system and python interpreter
#argv
#getwindowsversion()
#maxsize
#stdin
#stdout
import sys
def printData():
	print(sys.argv)
def printSum():
	print(int(sys.argv[1])+int(sys.argv[2]))
printData()
printSum()
print(sys.version)
print(sys.path)# interpreter will search for packages in these paths
#print(sys.maxint)
print(sys.maxsize)
print(type(sys.stdin))
print(sys.stdout)