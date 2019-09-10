# -*- coding: utf-8 -*-
#%%
def percentage(percent, decimal=0):
    # definition of a fucntion that returns  a % in str format'
    # percent is the number to put in %
    # decimal, is the number of digit after coma ( by defaut : 0)
    return str(int(percent * 10 ** (decimal + 2)) / (10 ** (decimal))) + '%'
    percentage(0.123456789, 1)


from celery import Celery # for future version , use multicore to improve performance 
import numpy as np
import time
import pandas  as pd 
import numpy as np
import matplotlib.pyplot as plt
import numpy as np


n=1000 # Define max range 
start = time.time()# measure starting time 


prime =np.array([2]) # initialize prime list (array)with 2 
counter=np.array([-1]) # intialize the counter to -1 

# For each prime , we build a modulo counter in an array .  For each number in range , we add 1 to counters
# When the modulo counter reset to 0 , it means that the reached number is just a multiple of the prime number.
# However if no modulo counter has reset to 0 , it means that the number is not the multiple of any prime , so this is a new prime . Then we need to add it to the array and intitiate a modulo counter for this number.
# In the meantime , we also save prime in a file.


for i in range(2,n):

    counter = counter +1
    if (np.array(np.where(counter == 0))).size == 0 : # Condition to check if no counter has reset to 0 meaning  that this value is not counted in the counter , so we found one prime.
       
        prime = np.append(prime,i) #
        counter = np.append(counter,-i)
        
    else : #if counter has reset to 0 , it means this values has been found , and counter should be rest to to orginal value
        p=np.where(counter==0 )
        counter[p]=counter[p]-prime[p] # Reset the counter for this specific to 0 
        
        
end = time.time() 
print(end - start) 
np.savetxt('prime.txt ', prime,fmt='%d')

