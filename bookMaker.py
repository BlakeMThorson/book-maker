from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as Soup
import random
import json
import pickle
import glob, os
import shutil
import re

#old code

#regex replace
#article = re.sub(r'(?is)</html>.+', '</html>', article)

# set the filepath and load in a shapefile

map_df = gpd.read_file(fp)
# check data type so we can see that this is not a normal dataframe, but a GEOdataframe
map_df.head()



def test1(A,n):
    n = n - 1 
    base = ( n * ( n + 1 ) ) / 2
    
    total = sum(A)
    return total - base


def test(L, A):
    n = len(L)
    if len(A) == 0:
        return n
    else:
        newList = []
        for t in range(0,n):
            newList.append(L[t])
            newList.append( [A[0],L[t]] )
        A = A[1:]
        print(newList)
        print(A)
        print("_________")
        return test(newList,A)


def reRev(A):
    if A == "":
        return ""
    return A[-1] + reRev(A[:-1])


def threeWayInPlace(A):
    LI = 0
    RI = len(A)-1
   
    while LI != RI:
        #if we can swap them do it
        if A[LI] != "r" and A[RI] == "r":
            temp = A[LI]
            A[LI] = A[RI] 
            A[RI] = temp
        #if our left indice tracker isn't over something that needs to be swapped increase it
        elif A[LI] == "r":
            LI += 1
        else:
            RI -= 1
    
    RI = len(A)-1
    
    print([LI,RI])
    
    print(A)
    
    while LI != RI:
        #if we can swap them do it
        if A[LI] != "w" and A[RI] == "w":
            temp = A[LI]
            A[LI] = A[RI] 
            A[RI] = temp
        #if our left indice tracker isn't over something that needs to be swapped increase it
        elif A[LI] == "w":
            LI += 1
        else:
            RI -= 1    
    
    
    return A    



def lics(A):
    oldMax = [[],0]
    currentMax = [[A[0]],A[0]]
    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            currentMax[0].append(A[i])
            currentMax[1] += A[i]
        else:
            if currentMax[1] > oldMax[1]:
                oldMax[0] = currentMax[0]
                oldMax[1] = currentMax[1]
            currentMax = [[A[i]],A[i]]
    return oldMax
            


                



def swapInPlace(A):
    mid = A[0]
    
    #swap A[0] and the middle value
    A[0] = A[ round(len(A)/2) ]
    A[ round(len(A)/2) ] = mid
    
    #left and right indice tracker
    LI = 0
    RI = len(A)-1
    
     
    while LI != RI:
        #if we can swap them do it
        if A[LI] >= mid and A[RI] < mid:
            temp = A[LI]
            A[LI] = A[RI] 
            A[RI] = temp
        #if our left indice tracker isn't over something that needs to be swapped increase it
        elif A[LI] < mid:
            LI += 1
        else:
            RI -= 1
    return A
            
            
        
    

    
    



def licLen(A):
    lastElement = [1]*len(A)
    
    for i in range(1, len(A)):
        if A[i] > A[i-1]:
            lastElement[i] = lastElement[i-1] + 1
        else:
            pass
    return max(lastElement)

#def schedule(A,T):
    #A.sort()
    #time = 0
    #total = 0
    #for i in A:
        #if time >= T:
            #return total
        #else:
            #time += i
            #total += 1
    #return total
    






def makeDoc():
    newBook = open("Book.txt","w")
    toWrite = ""    
    
    for i in range(250):
        print(i)
        toWrite += makeBook() + "\n\n ***** \n\n"
    
    newBook.write(toWrite)
    
    newBook.close()
    


def makeBook():
    import markovify
    
    # Get raw text as string.
    with open("newBook.txt") as f:
        text = f.read()
    
    # Build the model.
    text_model = markovify.Text(text)
    
    return text_model.make_short_sentence(1800)






def getFiles():
    os.chdir(r"C:\Users\white\Desktop\Book Maker\unread")
    books = glob.glob('*.txt')
    return books

def smallFormat(myString):
    #get rid of those foreign characters
    x = ''.join([i if ord(i) < 128 else ' ' for i in myString])
    
    #fuck capitalizations and shit
    x = x.lower()
    
    try:
        #fuck numbers
        x = re.sub(r'[\d*:\d*]', '', x)
        
        #get rid of the end disclaimer
        x = x[:x.index("end of")]
        
        #get rid of starting credit
        x = x[x.index("***\n"):]
    except:
        pass
        
    return x
    


def massFormat(books):
    
    #if book exist
    try:
        newBook = open("newBook.txt","r+")
        toWrite = newBook.read()
    except:
        newBook = open("newBook.txt","w")
        toWrite = ""
    
    for book in books:
        print(book)
        try:
            unformBook = open(r"C:\Users\white\Desktop\Book Maker\unread\{}".format(book),encoding="utf8")
        except:
            unformBook = open(r"C:\Users\white\Desktop\Book Maker\unread\{}".format(book))
        formBook = smallFormat(unformBook.read())
        toWrite += "\n" + formBook
    newBook.write(toWrite)
    newBook.close()
            
        

def massMove(books):
    for book in books:
        shutil.move(r"C:\Users\white\Desktop\Book Maker\unread\{}".format(book), r"C:\Users\white\Desktop\Book Maker\read\{}".format(book))

def main():
    #get all the books as text files
    allBooks = getFiles()
    #throw all the books into a text file
    massFormat( allBooks )
    massMove( allBooks ) 
    
    
  