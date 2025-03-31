BEGIN
    FOR num FROM 1 TO 10 DO
        IF num MOD 2 == 0 THEN
            CONTINUE  # Skip even numbers
        END IF

        PRINT num
    END FOR
END 