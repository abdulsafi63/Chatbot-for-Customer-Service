from flask import Flask, render_template, request
from chatbot import get_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    response = ""

    if request.method == "POST":

        user_message = request.form["message"]

        response = get_response(user_message)

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)