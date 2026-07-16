#gun water game
from flask import Flask, render_template, request, session
import random
import webbrowser
import threading

app = Flask(__name__)
app.secret_key = "snake_game_secret"

@app.route("/", methods=["GET", "POST"])
def index():
    if "user_score" not in session:
        session["user_score"] = 0
        session["computer_score"] = 0

    result = ""
    user_choice = ""
    computer_choice = ""
    sound = ""

    if request.method == "POST":
        user_choice = request.form["choice"]

        youDict = {"snake": 1, "water": -1, "gun": 0}
        reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

        computer = random.choice([-1, 0, 1])
        you = youDict[user_choice]

        if computer == you:
            result = "😐 Draw"
            sound = "click"
        elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
            result = "🎉 You Win!"
            session["user_score"] += 1
            sound = "win"
        else:
            result = "💀 You Lose!"
            session["computer_score"] += 1
            sound = "lose"

        user_choice = reverseDict[you]
        computer_choice = reverseDict[computer]

    return render_template(
        "index.html",
        result=result,
        user_choice=user_choice,
        computer_choice=computer_choice,
        user_score=session["user_score"],
        computer_score=session["computer_score"],
        sound=sound
    )

# 🔥 AUTO-OPEN BROWSER FUNCTION
def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    # Run browser in separate thread
    threading.Timer(1, open_browser).start()

    # Run Flask app
    app.run(debug=True)
