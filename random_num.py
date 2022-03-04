import random

def ran( x ) :
    a = 10 ** (x - 1 )
    b= 10 ** (x )
    print( random.randint ( a , b ) )

n = int(input("Enter number of digit : "))

ran(n)
