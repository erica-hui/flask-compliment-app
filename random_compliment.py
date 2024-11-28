import random

# Ask for the user's name
name = input("What's your name? ")
print(f"{name}, you're doing amazing, keep it up! 🌟")

# List of compliments and motivational quotes
compliments = [
    "You're doing amazing, keep it up! 🌟",
    "Your smile lights up the room! 😄",
    "You're a natural problem solver—nothing can stop you! 💪",
    "You have the courage to keep going, and that's inspiring! 🌈",
    "Your creativity knows no bounds. 🎨✨",
    "You bring out the best in everyone around you. 💖",
    "You're smarter than you give yourself credit for! 🧠",
    "The way you handle challenges is truly admirable. 👏",
    "You are enough, just as you are. 💚",
    "You have the power to achieve your dreams. Keep going! 🌟"
]

# Select a random compliment
random_compliment = random.choice(compliments)

# Print the compliment with the user's name
print(f"\n🌟 Here's a random compliment for you, {name}: 🌟")
print(random_compliment)
