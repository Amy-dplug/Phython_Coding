START

WHILE True DO:
    TRY:
        DISPLAY "On a scale of 1 - 10, how do you feel today? (1:😓, 10:🥰)"
        GET user_input
        CONVERT user_input TO INTEGER (scale)
        
        IF scale IS BETWEEN 1 AND 10 THEN:
            BREAK LOOP  # Exit if valid input
        ELSE:
            DISPLAY "Please enter a number between 1 and 10."

    CATCH ValueError:
        DISPLAY "Invalid input! Please enter a number between 1 and 10."

DISPLAY "You entered: " + scale

END