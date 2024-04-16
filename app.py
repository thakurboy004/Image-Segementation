from flask import Flask, render_template, request
from model import predict

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def first_project():
  return render_template("home.html")


@app.route("/predicting", methods=["GET", "POST"])
def predicting():
  if request.method == "POST":
    input_data = [
        float(request.form["REGION-CENTROID-COL"]),
        float(request.form["REGION-CENTROID-ROW"]),
        # float(request.form["REGION-PIXEL-COUNT"]),
        float(request.form["SHORT-LINE-DENSITY-5"]),
        float(request.form["SHORT-LINE-DENSITY-2"]),
        float(request.form["VEDGE-MEAN"]),
        float(request.form["VEDGE-SD"]),
        float(request.form["HEDGE-MEAN"]),
        float(request.form["HEDGE-SD"]),
        float(request.form["INTENSITY-MEAN"]),
        float(request.form["RAWRED-MEAN"]),
        float(request.form["RAWBLUE-MEAN"]),
        float(request.form["RAWGREEN-MEAN"]),
        float(request.form["EXRED-MEAN"]),
        float(request.form["EXBLUE-MEAN"]),
        float(request.form["EXGREEN-MEAN"]),
        float(request.form["VALUE-MEAN"]),
        float(request.form["SATURATION-MEAN"]),
        float(request.form["HUE-MEAN"])
    ]
    prediction = predict(input_data)
    return render_template("home.html", prediction_text=prediction)
  else:
    return render_template("home.html")
