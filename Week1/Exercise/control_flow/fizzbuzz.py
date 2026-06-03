

def fizzbuzz(n):

    """
    Implement fizzbuzz(n) that prints numbers 1 through n with these rules:

    Divisible by 3: print "Fizz"
    Divisible by 5: print "Buzz"
    Divisible by 7: print "Boom"
    Divisible by 3 AND 5: print "FizzBuzz"
    Divisible by 3 AND 7: print "FizzBoom"
    Divisible by 5 AND 7: print "BuzzBoom"
    Divisible by 3 AND 5 AND 7: print "FizzBuzzBoom"
    Otherwise: print the number

    """

    for i in range(1,n+1):
        
        if i%3==0 and i%5==0 and i%7==0:
            print("FizzBuzzBoom") 
        elif i%3==0 and i%5==0: 
            print( "FizzBuzz")
        elif i%3==0 and i%7==0:
            print("FizzBoom")
        elif i%5==0 and i%7==0:
            print("BuzzBoom")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 7 == 0:
            print("Boom")
        else:
            print(i)
        

fizzbuzz(105)
        



