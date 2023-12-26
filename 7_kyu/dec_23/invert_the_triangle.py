"""
Each time the function is called it should invert the passed triangle. Make upside down the given triangle and invert the chars in the triangle.

if a char = " ", make it = "#"
if a char = "#", make it = " "

    #    
   ###   
  #####  
 ####### 
######### // normal


         // inverted
#       #
##     ##
###   ###
#### ####

#### #### 
###   ###
##     ##
#       #
         // normal


######### // inverted
 ####### 
  #####  
   ###   
    #    

maketri() is at your disposal.
"""

def invert_triangle(triangle):
    return triangle[::-1].translate(str.maketrans(" #", "# "))
