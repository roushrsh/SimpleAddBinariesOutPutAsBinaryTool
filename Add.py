# SimpleAddBinariesOutPutAsBinaryTool
import sys #import needed tools

line = sys.stdin.readline()  #Take in line as input
binaries = line.split(',') #split into list of two
sum = bin(int(binaries[0],2) + int(binaries[1], 2))[2:]  #int(,2) takes it as base 2, add them together, bin converts it back. Having [2:] removes the 0b at the beginning

print(sum) #print statement
