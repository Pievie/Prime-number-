# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 11:23:35 2019

@author: btpbd
"""

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


n=1000000000 # Define max range 
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
        #writefile.write(str(y))+writefile.write(',')+writefile.write(str(i))+writefile.write(',')+ writefile.write('\n')#write it in the file
        prime = np.append(prime,i) #
        counter = np.append(counter,-i)
        #y=y+1
        #df_prime.loc[y] =y 
        #df_prime.loc[df_prime.index==y,'prime'] = i
    
        #print(percentage(i/n,2))
    else : #if counter has reset to 0 , it means this values has been found , and counter should be rest to to orginal value
        p=np.where(counter==0 )
        counter[p]=counter[p]-prime[p] # Reset the counter for this specific to 0 
        
        
end = time.time() 
print(end - start) 
np.savetxt('prime.txt ', prime,fmt='%d')

#%%
df_prime= pd.DataFrame(prime) 
df_prime['prime'] = df_prime[0]
    #%%
#%matplotlib qt 
df_bar = pd.DataFrame()

cat = 100
df_bar['cat'] =  (df_prime['prime']/cat).apply(np.floor).drop_duplicates()
df_bar['acc'] =  df_bar.index-2
df_bar['count'] = (df_bar['acc']-df_bar['acc'].shift(periods=-1))*(-1)
df_bar['ma'] =1
for i in range(1,100) :
    df_bar['ma'] = df_bar['ma']+ df_bar['count'].shift(periods=i) /(len ( range(1,100)))

plt.fill_between( df_bar['cat'], df_bar['count'], color="skyblue", alpha=0.4)
plt.fill_between( df_bar['cat'], df_bar['ma'], color="green", alpha=0.4)
plt.show()
plt.show()


#if i%1000 == 0 :
#            df_bar.loc[i/1000] = i/1000
#            df_bar.loc[df_bar.index ==i/1000,'acc']=df_prime['prime'].count()
#            df_bar['count'] =df_bar['acc']-df_bar['acc'].shift(periods=1)

#plt.bar(df_bar.index, df_bar['acc'])
#plt.show()

    #%%


#%%
