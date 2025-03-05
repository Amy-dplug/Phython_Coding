# Define the emotions dictionary once (outside the loop)
emotions = {
    1: "😓 Feeling rough, huh? Hang in there!",
    2: "😞 Hope things get better soon.",
    3: "😟 A little down, but you got this!",
    4: "😐 Meh... tomorrow's a new day!",
    5: "🙂 Right in the middle, not bad!",
    6: "😊 A bit of a smile—nice!",
    7: "😀 Sounds like a good day!",
    8: "😃 Now we're talking!",
    9: "🥳 Awesome! Keep it up!",
    10: "🥰 Living your best life!"
}

while True:  # Keeps running until a valid number is entered
    try:
        scale = int(input("On a scale of 1 - 10, how do you feel today? (1:😓, 10:🥰) "))
        if 1 <= scale <= 10:
            break  # Exit loop if input is valid
        else:
            print("Please enter a number between 1 and 10.")
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 10.")

# Display the emotion message after getting a valid input
print(emotions[scale])
