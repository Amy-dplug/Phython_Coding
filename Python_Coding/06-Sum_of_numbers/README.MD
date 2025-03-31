BEGIN
    PRINT "Enter a number: "
    READ n

    SET sum = 0

    FOR i FROM 1 TO n DO
        sum = sum + i
    END FOR

    PRINT "Sum =", sum
END
