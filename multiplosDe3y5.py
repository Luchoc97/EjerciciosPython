for i in range (1, 51):
    #print (i)
    if i % 3 == 0:
        print (str(i) + " fizz es 3")
    
    if i % 5 == 0:
        print (str(i) + " buzz es 5")
        
    if i % 3 == 0 and i % 5 == 0:
        print (str(i) + " fizzbuzz")