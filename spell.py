import os
import re
# import argparse as ap


# parser=ap.ArgumentParser(description="Please put the 6 characters followed by the main character")

# parser.add_argument('--letters',required=True,type=str,help="please put the 6 letters of the puzzle")
# parser.add_argument('-center',required=True,type=str,help="please put the center letter")
# args=parser.parse_args()
# centerLetter=args. ##can also do it via argument parsing instead of asking for user input
def inputFunc(noChar):
    while True:

        charList=input(f"Please put the {noChar} letters: ")
        charList=''.join(set(filter(str.isalpha,charList)))
        if len(charList)!=noChar:
             print(f"Please enter {noChar} unique alphabets")
             continue
        else:
             return charList


wordlist=[]
filePath=os.path.join(os.getcwd(),"words.txt")
if not os.path.exists(filePath):
    print("Dictionary file is not present, exiting now")
    exit()
with open(filePath,'r') as f:
    for line in f:
        wordlist.append((str(line).lower()).strip())



surroundLetter=inputFunc(6)
centerLetter=inputFunc(1) 

# surroundLetter='yateln' #test conditions
# centerLetter='m' #test conditions
allLetters=surroundLetter+centerLetter
wordlist = [i for i in wordlist if len(i)>3]
finalList=[]
regex=r"^["+re.escape(surroundLetter)+re.escape(centerLetter)+r"]+$"
perfPanagram=[]
panagram=[]
for word in wordlist:
    if centerLetter in word:      
        if re.search(regex,word):
            if word.count(allLetters)==1:
                perfPanagram.append(word)
            elif all([char in word for char in allLetters]):
                panagram.append(word)
            else:
                finalList.append(word)
            # elif re.search(regexPerf,)
if len(perfPanagram)>0:
    for word in perfPanagram:
        print(f"{word} Perfect Panagram")
for word in panagram:
    print(f"{word}"+'\033[3m'+" Panagram"+'\033[0m')

finalList=sorted(finalList,key=lambda s: (-len(s),s))
for word in finalList:
    print(word)