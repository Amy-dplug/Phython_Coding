BEGIN
    PRINT "Enter the student's score (0-100):"
    INPUT score 

    IF score >= 90 THEN
        grade = "A"
    ELSE IF score >= 80 THEN
        grade = "B"
    ELSE IF score >= 70 THEN
        grade = "C"
    ELSE IF score >= 60 THEN 
        grade = "D" 
    ELSE
        grade = "F"
    END IF 

    PRINT "The student's grade is:", grade
END