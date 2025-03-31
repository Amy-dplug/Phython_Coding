BEGIN
    SET countdown = 10

    WHILE countdown > 0 DO
        PRINT countdown
        DECREMENT countdown by 1
        
        PRINT "Enter 'stop' to cancel or press Enter: "
        READ user_input
        
        IF user_input is "stop" THEN
            PRINT "Countdown stopped!"
            BREAK
        END IF
    END WHILE
END