from flask import Flask

app = Flask(__name__)

app.route("/")
def home():
	print("Server received request for 'Home' page...")
	return "Welcome to my 'Home' page!"

@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


if __name__ == "__main__":
	app.run(debug=True)