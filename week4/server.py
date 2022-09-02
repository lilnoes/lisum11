from flask import Flask, request, jsonify
import pickle


targets = ["setosa", "versicolor", "virginica"]


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def status():
    return jsonify({"status": "online"})


@app.route("/predict", methods = ["GET", "POST"])
def predict():
    model = pickle.load(open("model.pickle", "rb"))

    slength = float(request.args.get("slength"))
    swidth = float(request.args.get("swidth"))

    plength = float(request.args.get("plength"))
    pwidth = float(request.args.get("pwidth"))
    
    res = model.predict([[slength, swidth, plength, pwidth]])
    return targets[res[0]]

if __name__ == "__main__":
    app.run(debug = True)