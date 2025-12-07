from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "change-me"  # anything random

# grocery items: filename must match images in static/foods
items = [
    {"filename": "01_eggs.png",             "name": "Eggs",               "price": 2.99},
    {"filename": "02_milk.png",             "name": "Milk",               "price": 2.32},
    {"filename": "03_orange_juice.png",     "name": "Orange Juice",       "price": 4.30},
    {"filename": "04_bread.png",            "name": "Bread",              "price": 3.64},
    {"filename": "05_vitamin_d.png",        "name": "Vitamin D Pills",    "price": 6.38},
    {"filename": "06_steak.png",            "name": "Sirloin Steak",      "price": 13.45},
    {"filename": "07_red_apple.png",        "name": "Red Apple",          "price": 4.87},
    {"filename": "08_whipped_cream.png",    "name": "Whipped Cream",      "price": 4.54},
    {"filename": "09_shredded_chicken.png", "name": "Shredded Chicken",   "price": 7.24},
    {"filename": "10_apple_pie.png",        "name": "Frozen Apple Pie",   "price": 5.63},
    {"filename": "11_maccaroni_pasta.png",  "name": "Macaroni Pasta Mix", "price": 8.38},
]

def pick_two():
    return random.sample(items, 2)

@app.route("/", methods=["GET", "POST"])
def index():
    if "score" not in session:
        session["score"] = 0

    score = session["score"]
    message = ""

    if request.method == "POST":
        guess = request.form.get("guess")          # "higher" or "lower"
        correct_answer = session.get("answer")     # what was right last round

        if guess == correct_answer:
            score += 1
            message = "Correct!"
            if score >= 10:
                message = "You got all 10 correct – you win!"
                score = 0
        else:
            message = "Wrong!"
            score = 0

        session["score"] = score

    # pick new pair for the next question
    item1, item2 = pick_two()

    answer = "higher" if item1["price"] > item2["price"] else "lower"
    session["answer"] = answer

    return render_template(
        "index.html",
        item1=item1,
        item2=item2,
        score=score,
        message=message,
    )

@app.route("/about")
def about():
    # simple about page if you want it later
    return "<h1>About this game</h1><p>Guess which grocery item costs more.</p>"

if __name__ == "__main__":
    app.run(debug=True)


