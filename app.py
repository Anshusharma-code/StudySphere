from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "StudySphere Flask App is Running!"

if __name__ == "__main__":
    app.run(debug=True)
