from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "My name is Duaa Fatima and I am a student of BSDS."

if __name__ == "__main__":
    app.run(debug=True)
