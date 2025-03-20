START

SET counter TO 1

WHILE counter IS LESS THAN 11 DO:
    DISPLAY counter
    DISPLAY "You're doing great"
    INCREMENT counter BY 1

DISPLAY a blank line
DISPLAY another blank line

IMPORT random number generator

GENERATE secret_number BETWEEN 1 AND 20
SET guess TO None
SET tries TO 0

DISPLAY "Alright, genius. I'm thinking of a number between 1 and 20."
DISPLAY "Bet you can't guess it!"

WHILE guess IS NOT EQUAL TO secret_number DO:
    TRY:
        PROMPT user FOR input "Your guess: "
        CONVERT input TO INTEGER AND STORE IN guess
        INCREMENT tries BY 1

        IF guess IS LESS THAN secret_number THEN:
            DISPLAY "Pfft. Too low. Are you even trying?"
        
        ELSE IF guess IS GREATER THAN secret_number THEN:
            DISPLAY "Whoa there, too high! Overshooting much?"
        
        ELSE:
            DISPLAY "Well, well, well... You got it! Took you [tries] tries though. U suck still nevertheless."
    
    CATCH invalid input (non-integer):
        DISPLAY "Bruh, that's not even a number. Focus!"

END