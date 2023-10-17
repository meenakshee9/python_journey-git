def placequeen(i,board): # Trying row i
 for each c such that (i,c) is available:
 place queen at (i,c) and update board
 if i == n-1:
 return(True) # Last queen has been placed
 else:
 extendsoln = placequeen(i+1,board)
 if extendsoln:
 return(True) # This solution extends fully
 else:
 undo this move and update board
 else:
 return(False) #
