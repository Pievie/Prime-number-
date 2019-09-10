# Prime-number-
Retrieve prime number in a given range.

---Variables---

   n = is the max range for looking prime.   
   For example , if n=100, the algortihm will look for prime number between 1 and 100. 


---Functionning ---

   For each prime , we build a modulo counter in an array . 
   For each number in range , we add 1 to counters
   When the modulo counter reset to 0 , it means that the reached number is just a multiple of the prime number.

   However if no modulo counter has reset to 0 , it means that the number is not the multiple of any prime , so this is a new prime . Then    we need to add it to the array and intitiate a modulo counter for this number.

 


---Output---

   The output is an array called "prime" . 
   The array is also saved as a text file : "prime.txt" in the workspace you have choosen. 
