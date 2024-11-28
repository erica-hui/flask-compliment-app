from flask import Flask, render_template, request
import random

app = Flask(__name__)
# List of compliments
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

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name")  # Get user input from the form
        random_compliment = random.choice(compliments)
        return render_template("index.html", name=name, compliment=random_compliment)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
