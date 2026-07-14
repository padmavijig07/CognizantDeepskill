from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({"message": "Flask app is running"})


@app.route("/greet/<name>")
def greet(name: str):
    return jsonify({"message": f"Hello, {name}!"})


@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json()
    return jsonify({"received": data})


if __name__ == "__main__":
    app.run(debug=True)
