a = random(1, 99)
guess = int(input("Enter an integer from 1 to 99: "))
while a != "guess":
    print
    if (guess < a):
        print "guess is low"
        guess = int(input("Enter an integer from 1 to 99: "))
    elif (guess > a):
        print "guess is high"
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print "you guessed it!"
     
    print