from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"


@app.route("/get-data")
def get_data():
	return jsonify({'name':'jafar', 'sure':'damirchilo'})

if __name__ == "__main__":
	app.run()
