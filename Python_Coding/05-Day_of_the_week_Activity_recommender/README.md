BEGIN
    DISPLAY "Enter the current day of the week:"
    READ day
    CONVERT day TO LOWERCASE

    IF day == "monday" THEN
        DISPLAY "Start your week with a workout!"
    ELSE IF day == "tuesday" THEN
        DISPLAY "It's a great day to read a book!"
    ELSE IF day == "wednesday" THEN
        DISPLAY "Mid week movie night!"
    ELSE IF day == "thursday" THEN
        DISPLAY "Try a new recipe!"
    ELSE IF day == "friday" THEN
        DISPLAY "Relax and enjoy the weekend!"
    ELSE IF day == "saturday" THEN
        DISPLAY "Go for a hike!"
    ELSE IF day == "sunday" THEN
        DISPLAY "Prepare for the week ahead with some self-care."
    ELSE
        DISPLAY "Invalid input. Please enter a valid day of the week."
    ENDIF
END
