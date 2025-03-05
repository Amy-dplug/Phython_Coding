def get_scale():
    """Asks the user for a number between 1-10 and validates input using recursion."""
    try:
        scale = int(input("On a scale of 1 - 10, how do you feel today? (1:😓, 10:🥰) "))
        if 1 <= scale <= 10:
            return scale  # Valid input, return it
        else:
            print("Please enter a number between 1 and 10.")
            return get_scale()  # Recursively ask again
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 10.")
        return get_scale()  # Recursively ask again

# Get user details
myName = input("Who are you? ")
if myName.lower() == "joshua":  # Case insensitive check
    print("Well Hi")
else:
    print("Hmm, IDK you anyways...")

# Get achievement goal
achieve = input("What do you want to achieve? ")
if achieve.lower() in ["be the best", "teach people how to code!"]:
    print("Noice!")
else:
    print("Hmm, well that's good!")

# Emotion mapping
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

# Get and display emotional state
scale = get_scale()
print(emotions[scale])

# Advice section (fixed ANSI escape codes for color formatting)
advice = """
\033[36mHey word of advice:\033[0m 
Don't be a d**k and keep your head up. 
TODAY, you're going to understand why Amy's seatmate is on something! 
Anyways, you're also going to teach people how to code :D 
in the most amazing way, simply by not being a d**k - YOU ROCK! 'ig'
"""
print(advice)
