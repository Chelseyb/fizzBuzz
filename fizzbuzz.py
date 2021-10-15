
"""
Fizz Buzz Interview Question
Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.


"""
print("Fizzbuzz challenge")


#zero index so 101
for numslist in range(101):

    #fizbuzz has to be at the top to catch both
    if numslist % 5 == 0 & numslist % 3 ==0:
        print("FizzBuzz")
        #need the contiues so it goes all the way through
        continue
        
    
    if numslist % 3 == 0:
        print("Fizz")        
        continue
    
    if numslist % 5 == 0:
        print("Buzz")
        continue
        

    print(numslist)
            
              
    


    
    
