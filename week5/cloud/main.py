import functions_framework
import pickle

targets = ["setosa", "versicolor", "virginica"]


@functions_framework.http
def hello_world(request):
    model = pickle.load(open("model.pickle", "rb"))

    slength = float(request.args.get("slength"))
    swidth = float(request.args.get("swidth"))

    plength = float(request.args.get("plength"))
    pwidth = float(request.args.get("pwidth"))
    
    res = model.predict([[slength, swidth, plength, pwidth]])
    return targets[res[0]]

