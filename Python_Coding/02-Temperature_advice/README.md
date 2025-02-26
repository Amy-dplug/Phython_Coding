BEGIN
    PRINT "Enter the temperature in Celsius:"
    INPUT temperature
    
    IF temperature < 10 THEN
        PRINT "It's cold outside. Wear a jacket!"
    ELSE IF temperature >= 10 AND temperature <= 25 THEN
        PRINT "It's a nice day. Wear short-sleeves!"
    ELSE
        PRINT "It's hot outside. Stay cool!"
    END IF
END