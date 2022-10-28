#FIFO Page replacement algorithm

class FIFO(object):
    def __init__(s, p):
        size = s #Number of frames
        pages = p #Array of pages
        
        frames = [] # memory to hold pages
        fault = 0 #To count the number of misses
        first = 0 #The first element in memory
        
        """We want to set the elements
        in the array to -1"""
        
        for k in range(0,size):
            frames[k] = -1
        
        for i in pages:
            if i not in frames:
                if len(frames)<size:
                    frames.append(i)
                    
                else:
                    frames[first] = i
                    first = (first+1)%size
                    
                fault+=1
                
            else:
                
        