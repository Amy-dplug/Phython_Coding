BEGIN
    PRINT "Enter a number:"
    INPUT number
    
    IF number MOD 2 == 0 THEN
        PRINT "The number is even."
    ELSE
        PRINT "The number is odd."
    END IF
END
