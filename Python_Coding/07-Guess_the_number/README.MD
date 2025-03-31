BEGIN
    GENERATE a random number between 1 and 10 (random_number)
    
    REPEAT
        PRINT "Guess the number: "
        READ guess
        
        IF guess is equal to random_number THEN
            PRINT "Correct! 🎉"
        ELSE
            PRINT "Wrong, try again!"
        END IF
    UNTIL guess is equal to random_number
END