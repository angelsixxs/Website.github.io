from flask import Flask, render_template, request
import os
import random

app = Flask(__name__)

## Food pricing
food_prices = {
    "01_eggs.png": 2.99,
    "02_milk.png": 2.32,
    "03_orange_juice.png": 4.30,
    "04_bread.png": 3.64,
    "05_vitamin_d.png": 6.38,
    "06_steak.png": 13.45,
    "07_red_apple.png": 4.87,
    "08_whipped_cream.png": 4.54,
    "09_shredded_chicken.png": 7.24,
    "10_apple_pie.png": 5.63,
    "11_maccaroni_pasta.png": 8.38
}

@app.route("/", methods=["GET", "POST"])
def game():
    if request.method == "POST":
        chosen = request.form.get("choice")
        correct = request.form.get("correct_answer")

        if chosen == correct:
            result = "Correct!"
        else:
            result = "Wrong!"

        return render_template("index.html", result=result)

    ## Pick 2 foods
    foods = list(food_prices.keys())
    food1, food2 = random.sample(foods, 2)

    ## Compare prices to find the more expensive one
    correct_answer = food1 if food_prices[food1] > food_prices[food2] else food2

    return render_template(
        "index.html",
        food1=food1,
        food2=food2,
        correct_answer=correct_answer,
        result=None
    )

if __name__ == "__main__":
    app.run(debug=True)
    

