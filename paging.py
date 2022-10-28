#Author: Bonolo

from random import randrange
import sys

def FIFO(s, p):
    size = s
    pages = p
    
    frames = [] # memory to hold pages
    fault = 0 # fault count
    first = 0 # First element in list for FIFO
    
    for i in pages:
        if i not in frames:
            if len(frames) < size:
                frames.append(i)
            else:
                frames[first] = i
                first = (first + 1) % size
                
            fault += 1
        for j in frames:
            print "%-4r" % j,
        if len(frames) < size:
            for q in range(len(frames), size):
                y = -1
                print "%-4r" % y,
        print " "
    return fault

def LRU(s, p):
    size = s
    pages = p
    
    frames = [] #memory to hold pages
    fault = 0
        
    for i in pages:
        if i not in frames:
            if len(frames) < size:
                frames.append(i)
            else:
                frames.pop(0)
                frames.append(i)
            fault += 1
        
        #We move it away from the index 0:
        else:
            frames.remove(i)
            frames.append(i)
        for j in frames:
            print "%-4r" % j,
            
        if len(frames) < size:
            for q in range(len(frames), size):
                y = -1
                print "%-4r" % y,
        print " "
    return fault

def OPT(s, p):
    size = s
    pages = p
    
    frames = []
    fault = 0
    occurance = [None for i in range(size)]
    
    for i in pages:
        if i not in frames:
            if len(frames) < size:
                frames.append(i)
            else:
                
                for j in frames:
                    k = frames.index(j)
                    if j not in pages[pages.index(i)+1:]:
                        frames[k] = pages[pages.index(i)]
                        break
                    else:
                        occurance[k] = pages[pages.index(i)+1:].index(j)
                        
                else:
                    frames[occurance.index(max(occurance))] = pages[pages.index(i)]
            fault += 1 
        for j in frames:
            print "%-4r" % j,
            
        if len(frames) < size:
            for q in range(len(frames), size):
                y = -1
                print "%-4r" % y,
        print " "
    return fault
    
def main():
    pages = [8, 5, 6, 2, 5, 3, 5, 4]
    
    #This was used for testing purposes.
    #generating an array of ranfom page strings
    '''pages = []
    for i in range(0, 10):
        pages.append(randrange(10))'''
        
    size = int(sys.argv[1])
    #size = 3
    
    print "FIFO\n", FIFO(size, pages), "page faults.\n"
    print "LRU\n", LRU(size, pages), "page faults.\n"
    print "OPT\n", OPT(size, pages), "page faults."
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print 'Usage: python paging.py [number of pages]'
    else:
        main()
